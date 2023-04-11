#! /usr/bin/env python3
#
# Compute the transport using a slab mixed layer model
#
# June-2022, Jamie Hilditch

import numpy as np
from scipy.integrate import cumtrapz
from numpy.typing import ArrayLike

from airsea import windstress as ws

def transport(t: ArrayLike, windSpeed: ArrayLike, windDirection: ArrayLike,*,
    f: float = 2*np.pi/89820, damping: float = 0.1, rho: float = 1025.,
    height: float = 10., wind_max: float = 30.) -> np.ndarray:
    """
    Compute the transport using a slab mixed layer model

    This function solves the slab mixed layer equations for the zonal U
    and meridional V transport.
        dU/dt - fV + rU = tau_x/rho
        dV/dt + fU + rV = tau_y/rho
    Where f is the Coriolis parameter, r is a Rayleigh damping coefficient,
    tau is the wind stress and rho is the density of the mixed layer.
    Wind stress is calculated using Large and Pond (1981) from the
    airsea package (https://github.com/pyoceans/python-airsea).

    Wind speeds larger than wind_max are filtered out before the integration.
    The resulting gaps in the transport time series are filled in by linear
    interpolation.

    Arguments:
        t: ArrayLike             - time in seconds e.g. POSIX time timestamp
        windSpeed: ArrayLike     - wind speed in metres per second
        windDirection: ArrayLike - wind direction in degrees as a bearing

    Key-word arguments:
        f: float        = 2*pi/89820 - Coriolis parameter in inverse seconds
        damping: float  = 0.1        - Damping factor such that r = damping*f
        rho: float      = 1025.      - Mixed layer density in kg/m^3
        height: float   = 10.        - Height in metres of wind measurements
        wind_max: float = 30.        - Wind speeds larger than wind_max are
                                       filtered out

    Outputs:
        U: np.ndarray - zonal transport in m^2/s
        V: np.ndarray - meridional transport in m^2/s
    """

    r = damping*f
    t = np.asarray(t)
    windSpeed = np.asarray(windSpeed)
    windDirection = np.asarray(windDirection)

    #filter out wind speeds greater than wind_max
    idx = windSpeed <= wind_max

    t0 = t[idx] - t[0] # time translation to keep exponentials in check
    stress = ws.stress(windSpeed[idx],height)/rho
    theta = -np.pi/2 - np.pi*windDirection[idx]/180
    sin_integral = cumtrapz(stress*np.exp(r*t0)*np.sin(f*t0 + theta),t0,initial=0)
    cos_integral = cumtrapz(stress*np.exp(r*t0)*np.cos(f*t0 + theta),t0,initial=0)
    U = np.exp(-r*t0)*np.cos(f*t0)*cos_integral + np.exp(-r*t0)*np.sin(f*t0)*sin_integral
    V = np.exp(-r*t0)*np.cos(f*t0)*sin_integral - np.exp(-r*t0)*np.sin(f*t0)*cos_integral
    U = np.interp(t,t0 + t[0],U)
    V = np.interp(t,t0 + t[0],V)
    return U,V

def __test_slabMixedLayer():
    t = np.linspace(0,100,20)
    windSpeed = 10*np.random.rand(20)
    windDirection = 360*np.random.rand(20)
    U,V = transport(t,windSpeed,windDirection)
    print(f"{U = }")
    print(f"{V = }")

if __name__ == "__main__":
    __test_slabMixedLayer()
