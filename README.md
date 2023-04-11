# Slab-Mixed-Layer-Model
Compute the transport given the winds using a slab mixed layer model

Integrate over the Ekman layer, with unspecified depth $H$, to get the slab mixed layer equations forced by the wind stress $(\tau_x,\tau_y)$ and damped by Rayleigh damping with coefficient $r$.

$$ \frac{\mathrm{d} U}{\mathrm{d} t} - fV + rU = \tau_x $$

$$ \frac{\mathrm{d} V}{\mathrm{d} t} + fU + rV = \tau_x $$

## Exact Solution ##
Defining $\Phi = U + \mathrm{i} V$ we have 

$$ \frac{\mathrm{d} \Phi}{\mathrm{d} t} +\mathrm{i} f\Phi + r\Phi = \tau_x + \mathrm{i} \tau_y $$
$$ \frac{\mathrm{d}~}{\mathrm{d} t}\left(\Phi\mathrm{e}^{(r+\mathrm{i} f)t}\right) = (\tau_x + \mathrm{i} \tau_y)\mathrm{e}^{(r+\mathrm{i} f)t} $$

Writing $(\tau_x + \mathrm{i} \tau_y) = \tau \mathrm{e}^{\mathrm{i} \theta}$. N.B. here there is ample opportunity to mess up converting between the wind direction and theta.

$$ \Phi = \mathrm{e}^{-(r+\mathrm{i} f)t}\int \tau(t)\mathrm{e}^{(r+\mathrm{i} f)t + \mathrm{i}\theta (t)}\mathrm{d}t $$

In terms of real variables

$$ U = \mathrm{e}^{-rt}\cos(ft)\int \tau(t) \mathrm{e}^{rt}\cos(ft + \theta(t) )\mathrm{d}t + \mathrm{e}^{-r t}\sin(ft)\int \tau(t)\mathrm{e}^{rt}\sin(ft + \theta(t)) \mathrm{d}t $$

$$ V = \mathrm{e}^{-rt}\cos(ft)\int \tau(t) \mathrm{e}^{rt}\sin(ft + \theta(t) )\mathrm{d}t - \mathrm{e}^{-r t}\sin(ft)\int \tau(t)\mathrm{e}^{rt}\cos(ft + \theta(t)) \mathrm{d}t $$
