# Slab-Mixed-Layer-Model
Compute the transport given the winds using a slab mixed layer model

Integrate over the Ekman layer, with unspecified depth $H$, to get the slab mixed layer equations forced by the wind stress $(\tau_x,\tau_y)$ and damped by Rayleigh damping with coefficient $r$.

$$ \frac{\mathrm{d} U}{\mathrm{d} t} - fV + rU = \frac{\tau_x}{\rho_0} $$

$$ \frac{\mathrm{d} V}{\mathrm{d} t} + fU + rV = \frac{\tau_y}{\rho_0} $$

## Exact Solution ##
Defining $\Phi = U + \mathrm{i} V$ we have 

$$ \frac{\mathrm{d} \Phi}{\mathrm{d} t} +\mathrm{i} f\Phi + r\Phi = \rho_0^{-1}(\tau_x + \mathrm{i} \tau_y) $$

which can be written as

$$ \frac{\mathrm{d}~}{\mathrm{d} t}\left(\Phi\mathrm{e}^{(r+\mathrm{i} f)t}\right) = \rho_0^{-1}(\tau_x + \mathrm{i} \tau_y)\mathrm{e}^{(r+\mathrm{i} f)t} $$

Expressing the wind-stress in polar coordinates (N.B. here there is ample opportunity to mess up converting between the wind direction and theta) and normalising, $\rho_0^{-1}(\tau_x + \mathrm{i} \tau_y) = \bar{\tau} \mathrm{e}^{\mathrm{i} \theta}$, we have the solution. 

$$ \Phi = \mathrm{e}^{-(r+\mathrm{i} f)t} \int \bar{\tau}(t)\mathrm{e}^{(r+\mathrm{i} f)t + \mathrm{i}\theta (t)}\mathrm{d}t $$

In terms of real variables

$$ U = \mathrm{e}^{-rt}\cos(ft) \int \bar{\tau}(t) \mathrm{e}^{rt}\cos(ft + \theta(t) )\mathrm{d}t + \mathrm{e}^{-r t}\sin(ft) \int \bar{\tau}(t)\mathrm{e}^{rt}\sin(ft + \theta(t)) \mathrm{d}t $$

$$ V = \mathrm{e}^{-rt}\cos(ft) \int \bar{\tau}(t) \mathrm{e}^{rt}\sin(ft + \theta(t) )\mathrm{d}t - \mathrm{e}^{-r t}\sin(ft) \int \bar{\tau}(t)\mathrm{e}^{rt}\cos(ft + \theta(t)) \mathrm{d}t $$
