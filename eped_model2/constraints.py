import tensorflow

def ip_limits(ip):
    return tensorflow.math.logical_and(ip >= 0.518, ip <= 1.96)

def bt_limits(bt):
    return tensorflow.math.logical_and(bt >= 0.978, bt <= 2.165)

def r_limits(r):
    return tensorflow.math.logical_and(r >= 1.651, r <= 1.743)

def a_limits(a):
    return tensorflow.math.logical_and(a >= 0.527, a <= 0.611)

def kappa_limits(kappa):
    return tensorflow.math.logical_and(kappa >= 1.451, kappa <= 1.996)

def delta_limits(delta):
    return tensorflow.math.logical_and(delta >= 0.068, delta <= 0.726)

def neped_limits(neped):
    return tensorflow.math.logical_and(neped >= 1.227, neped <= 8.977)

def zeff_limits(zeffped):
    return tensorflow.math.logical_and(zeffped >= 1.08, zeffped <= 4.37)

def pped_limits(pped):
    return tensorflow.math.logical_and(pped >= 0.0, pped <= 500.0)

def wped_limits(wped):
    return tensorflow.math.logical_and(wped >= 0.0, wped <= 0.2)

def aratio_limits(r, a):
    return tensorflow.math.logical_and(r/a >= 2.7, r/a <= 3.3)

def betan_limits(betan):
    return tensorflow.math.logical_and(betan >= 0.88, betan <= 3.82)

manifest = [
    {'function' : ip_limits,     'args' : ['ip'      ] },
    {'function' : bt_limits,     'args' : ['bt'      ] },
    {'function' : r_limits,      'args' : ['r'       ] },
    {'function' : a_limits,      'args' : ['a'       ] },
    {'function' : kappa_limits,  'args' : ['kappa'   ] },
    {'function' : delta_limits,  'args' : ['delta'   ] },
    {'function' : neped_limits,  'args' : ['neped'   ] },
    {'function' : zeff_limits,   'args' : ['zeffped' ] },
    {'function' : pped_limits,   'args' : ['pped'    ] },
    {'function' : wped_limits,   'args' : ['wped'    ] },
    {'function' : aratio_limits, 'args' : ['r', 'a'  ] },
    {'function' : betan_limits,  'args' : ['betan'   ] }
]

