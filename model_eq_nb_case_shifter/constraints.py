import tensorflow
import math

def fbs(ip, ibs):
    return ibs/ip < 1.0

def aratio(r, a):
    return tensorflow.math.logical_and(2.34 <= r/a, r/a <= 3.5)

def q95_input(r, a, bt, ip, kappa, delta):
    eps = a/r
    q95 = 5.0*(a*eps*bt/ip)*((1.0+kappa*kappa*(1.0+2.0*delta*delta-1.2*delta*delta*delta))/2.0)*((1.17-0.65*eps)/(tensorflow.math.pow(1.0-tensorflow.math.pow(eps,2.5),2)))
    return tensorflow.math.logical_and(q95 >= 3.0, q95 <= 7.0)

def q95(q95_value):
    return tensorflow.math.logical_and(q95_value >= 3.0, q95_value <= 7.0)

def greenwald(ip,a,ne):
    limit = ip/(math.pi*a*a)
    return ne < limit

def r_limits(r):
    return tensorflow.math.logical_and(r >= 1.4, r <= 2.2)

def a_limits(a):
    return tensorflow.math.logical_and(a >= 0.4, a <= 0.94)

def kappa_limits(kappa):
    return tensorflow.math.logical_and(kappa >= 1.7, kappa <= 2.0)

def delta_limits(delta):
    return tensorflow.math.logical_and(delta >= 0.5, delta <= 0.65)

def bt_limits(bt):
    return tensorflow.math.logical_and(bt >= 3.0, bt <= 7.0)

def ip_limits(ip):
    return tensorflow.math.logical_and(ip >= 0.74, ip <= 12.0)

def fgw_ped_limits(fgw_ped):
    return tensorflow.math.logical_and(fgw_ped >= 0.2, fgw_ped <= 1.0)

def nepeak_limits(nepeak):
    return tensorflow.math.logical_and(nepeak >= 1.5, nepeak <= 2.0)

def betan_limits(betan):
    return tensorflow.math.logical_and(betan >= 2.5, betan <= 4.5)

def betan_ped_limits(betan_ped):
    return tensorflow.math.logical_and(betan_ped >= 0.5, betan_ped <= 1.2)

def ibs_limits(ibs):
    return tensorflow.math.logical_and(ibs >= 0.0, ibs <= 12.0)

def inb_limits(inb):
    return tensorflow.math.logical_and(inb >= 0.0, inb <= 12.0)

def irf_limits(irf):
    return tensorflow.math.logical_and(irf >= 0.0, irf <= 12.0)

def zeff_axis_limits(zeff_axis):
    return tensorflow.math.logical_and(zeff_axis >= 1.0, zeff_axis <= 10.0)

def pfuse_limits(pfuse):
    return tensorflow.math.logical_and(pfuse >= 0.0, pfuse <= 20.0)

def pfusi_limits(pfusi):
    return tensorflow.math.logical_and(pfusi >= 0.0, pfusi <= 20.0)

def prfe_limits(prfe):
    return tensorflow.math.logical_and(prfe >= 0.0, prfe <= 50.0)

def prfi_limits(prfi):
    return tensorflow.math.logical_and(prfi >= 0.0, prfi <= 20.0)

def pnbe_limits(pnbe):
    return tensorflow.math.logical_and(pnbe >= 0.0, pnbe <= 20.0)

def pnbi_limits(pnbi):
    return tensorflow.math.logical_and(pnbi >= 0.0, pnbi <= 20.0)

def prad_limits(prad):
    return tensorflow.math.logical_and(prad >= 0.0, prad <= 20.0)

def tau98_limits(tau98):
    return tensorflow.math.logical_and(tau98 >= 0.0, tau98 <= 2.0)

def bptor_limits(bptor):
    return tensorflow.math.logical_and(bptor >= 0.0, bptor <= 20.0e6)

manifest = [
    {'function' : fbs,              'args' : ['ip','ibs']                        },
    {'function' : aratio,           'args' : ['r','a']                           },
    {'function' : q95_input,        'args' : ['r','a','bt','ip','kappa','delta'] },
    {'function' : q95,              'args' : ['q95_input']                       },
    {'function' : greenwald,        'args' : ['ip','a','nepeak']                 },
    {'function' : r_limits,         'args' : ['r']                               },
    {'function' : a_limits,         'args' : ['a']                               },
    {'function' : kappa_limits,     'args' : ['kappa']                           },
    {'function' : delta_limits,     'args' : ['delta']                           },
    {'function' : bt_limits,        'args' : ['bt']                              },
    {'function' : ip_limits,        'args' : ['ip']                              },
    {'function' : fgw_ped_limits,   'args' : ['fgw_ped']                         },
    {'function' : nepeak_limits,    'args' : ['nepeak']                          },
    {'function' : betan_limits,     'args' : ['betan']                           },
    {'function' : betan_ped_limits, 'args' : ['betan_ped']                       },
    {'function' : ibs_limits,       'args' : ['ibs']                             },
    {'function' : inb_limits,       'args' : ['inb']                             },
    {'function' : irf_limits,       'args' : ['irf']                             },
    {'function' : zeff_axis_limits, 'args' : ['zeff_axis']                       },
    {'function' : pfuse_limits,     'args' : ['pfuse']                           },
    {'function' : pfusi_limits,     'args' : ['pfusi']                           },
    {'function' : prfe_limits,      'args' : ['prfe']                            },
    {'function' : prfi_limits,      'args' : ['prfi']                            },
    {'function' : pnbe_limits,      'args' : ['pnbe']                            },
    {'function' : pnbi_limits,      'args' : ['pnbi']                            },
    {'function' : prad_limits,      'args' : ['prad']                            },
    {'function' : tau98_limits,     'args' : ['tau98']                           },
    {'function' : bptor_limits,     'args' : ['bptor']                           }
]
