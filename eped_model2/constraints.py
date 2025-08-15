import tensorflow

def ip_limits(ip):
    return tensorflow.math.logical_and(ip >= 5.0, ip <= 10.0)

def bt_limits(bt):
    return tensorflow.math.logical_and(bt >= 5.0, bt <= 15.0)

def r_limits(r):
    return tensorflow.math.logical_and(r >= 3.0, r <= 4.5)

def a_limits(a):
    return tensorflow.math.logical_and(a >= 0.6, a <= 2.8)

def kappa_limits(kappa):
    return tensorflow.math.logical_and(kappa >= 1.7, kappa <= 2.0)

def delta_limits(delta):
    return tensorflow.math.logical_and(delta >= 0.3, delta <= 0.7)

def neped_limits(neped):
    return tensorflow.math.logical_and(neped >= 9.0, neped <= 15.0)

def zeff_limits(zeff):
    return tensorflow.math.logical_and(zeff >= 1.5, zeff <= 2.5)

def pped_limits(pped):
    return tensorflow.math.logical_and(pped >= 0.0, pped <= 500.0)

def wped_limits(wped):
    return tensorflow.math.logical_and(wped >= 0.0, wped <= 0.2)

def aratio_limits(r, a):
    return tensorflow.math.logical_and(r/a >= 1.7, r/a <= 2.0)

manifest = [
    {'function' : ip_limits,     'args' : ['ip'     ] },
    {'function' : bt_limits,     'args' : ['bt'     ] },
    {'function' : r_limits,      'args' : ['r'      ] },
    {'function' : a_limits,      'args' : ['a'      ] },
    {'function' : kappa_limits,  'args' : ['kappa'  ] },
    {'function' : delta_limits,  'args' : ['delta'  ] },
    {'function' : neped_limits,  'args' : ['neped'  ] },
    {'function' : zeff_limits,   'args' : ['zeff'   ] },
    {'function' : pped_limits,   'args' : ['pped'   ] },
    {'function' : wped_limits,   'args' : ['wped'   ] },
    {'function' : aratio_limits, 'args' : ['r', 'a' ] }
]

