import tensorflow

def delta_limits(delta):
    return tensorflow.math.logical_and(delta >= 0.198, delta <= 0.4)

def pped_limits(pped):
    return tensorflow.math.logical_and(pped >= 0.0, pped <= 500.0)

def wped_limits(wped):
    return tensorflow.math.logical_and(wped >= 0.0, wped <= 0.2)

manifest = [
    {'function' : delta_limits,  'args' : ['delta'  ] },
    {'function' : pped_limits,   'args' : ['pped'   ] },
    {'function' : wped_limits,   'args' : ['wped'   ] }
]
