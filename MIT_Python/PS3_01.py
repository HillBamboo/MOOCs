def f(x):
        import math
        return 60 * math.e ** (math.log(0.5) / 55.6 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    total = 0.0
    i = start
    while i < stop:
        total += step * f(i)
        i += step
    return total

print radiationExposure(0, 60, 0.5) 
