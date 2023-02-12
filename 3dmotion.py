import math
def range_float(start, stop, step):
    x=start
    while x<= stop:
        yield x
        x += step;

