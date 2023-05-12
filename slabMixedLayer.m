function [ U,V ] = slabMixedLayer(t,windSpeed,windDirection,params)
% slabMixedLayer: Computes the zonal, U, and meridional, V, transport
% using a slab mixed layer model.
%   dU/dt - fV + rU = tau_x/rho
%   dV/dt + fU + rV = tau_y/rho
% Where f is the Coriolis parameter, r is a Rayleigh damping coefficient,
% tau is the wind stress and rho is the density of the mixed layer.
% Wind stress is calculated using Large and Pond (1981) from the
% air-sea-master toolbox.
%
% INPUTS:
%   t             - time in seconds e.g. POSIX time timestamp
%   windSpeed     - wind speed in metres per second
%   windDirection - wind direction in degrees as a bearing
%
% NAME-VALUE INPUTS:
%   f       = 2*pi/89820 - Coriolis parameter in inverse seconds
%   damping = 0.1        - Damping factor such that r = damping*f
%   rho     = 1025       - Mixed layer density in kg/m^3
%   height  = 10         - Height in metres of wind measurements
%
% OUTPUTS:
%   U - zonal transport in m^2/s
%   V - meridional transport in m^2/s
%
% Jamie Hilditch - June 2022

    arguments
        t double
        windSpeed double
        windDirection double
        params.f double = 2*pi/89820;
        params.damping double = 0.1;
        params.rho double = 1025;
        params.height double = 10
    end

    f = params.f;
    r = params.damping*f;
    rho = params.rho;
    height = params.height;

    t0 = t - t(1);
    stress = stresslp(windSpeed,height)/rho;
    theta = -pi/2 - pi*windDirection/180;
    sin_integral = cumtrapz(t0,stress.*exp(r*t0).*sin(f*t0 + theta));
    cos_integral = cumtrapz(t0,stress.*exp(r*t0).*cos(f*t0 + theta));
    U = exp(-r*t0).*cos(f*t0).*cos_integral + exp(-r*t0).*sin(f*t0).*sin_integral;
    V = exp(-r*t0).*cos(f*t0).*sin_integral - exp(-r*t0).*sin(f*t0).*cos_integral;
end
