import tensorflow

def ec_freg_limits(ec_freq):
    return tensorflow.math.logical_and(ec_freq >= 1.5e11, ec_freq <= 2.5e11)

def ec_thet_limits(ec_thet):
    return tensorflow.math.logical_and(ec_thet >= -90.0, ec_thet <= 90.0)

def ec_phai_limits(ec_phai):
    return tensorflow.math.logical_and(ec_phai >= -90.0, ec_phai <= 90.0)

def ec_theta_limits(ec_theta):
    return tensorflow.math.logical_and(ec_theta >= -1.57, ec_theta <= 1.57)

def r_limits(r):
    return tensorflow.math.logical_and(r >= 1.5, r <= 4.0)

def bt_limits(bt):
    return tensorflow.math.logical_and(bt >= 4.0, bt <= 10.0)

def ip_limits(ip):
    return tensorflow.math.logical_and(ip >= 6.5, ip <= 15.0)

def h98_limits(h98):
    return tensorflow.math.logical_and(h98 >= 0.9, h98 <= 1.5)

def pinj_limits(pinj):
    return tensorflow.math.logical_and(pinj >= 50.0, pinj <= 150.0)

def kappa_limits(kappa):
    return tensorflow.math.logical_and(kappa >= 1.25, kappa <= 2.75)

def nepeak_limits(nepeak):
    return tensorflow.math.logical_and(nepeak >= 1.3, nepeak <= 2.2)

def aratio_limits(aratio):
    return tensorflow.math.logical_and(aratio >= 3.0, aratio <= 4.0)

manifest = [
    {'function' : ec_freg_limits,  'args' : ['ec_freq' ] },
    {'function' : ec_thet_limits,  'args' : ['ec_thet' ] },
    {'function' : ec_phai_limits,  'args' : ['ec_phai' ] },
    {'function' : ec_theta_limits, 'args' : ['ec_theta'] },
    {'function' : r_limits,        'args' : ['r'       ] },
    {'function' : bt_limits,       'args' : ['bt'      ] },
    {'function' : ip_limits,       'args' : ['ip'      ] },
    {'function' : h98_limits,      'args' : ['h98'     ] },
    {'function' : pinj_limits,     'args' : ['pinj'    ] },
    {'function' : kappa_limits,    'args' : ['kappa'   ] },
    {'function' : nepeak_limits,   'args' : ['nepeak'  ] },
    {'function' : aratio_limits,   'args' : ['aratio'  ] }
]
