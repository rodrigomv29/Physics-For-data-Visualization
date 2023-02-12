import numpy as np
import warnings
import matplotlib.pyplot as plt
import math

class Kinematics:
    """
    Solve physics kinematic exercises; assume constant speed
    SI UNITS
        distance~ meters
        speed~ meters/second
        time~ seconds
    """
    def getDistance(velocity=0, time=0):
        if velocity == 0 and time == 0:
            raise Exception("A non-zero value needs to be inserted");
            return;
        return velocity * time
        
    def getSpeed(distance=0, time=0) :
        if distance == 0 and time == 0:
            raise Exception("A non-zero value needs to be inserted");
        return distance / time
    def getTime(speed=0, distance=0):
        if speed == 0 and distance == 0:
            raise Exception("A non-zero value needs to be inserted");
        return speed/distance

    """
        1D Kinematics: Displacement; Velocity; Acceleration
    """
    def getDisplacement(x1, x2):
        """
        A particle goes from x1 to x2; what is the total displacement"
        return x2-x1;
        """
        return x2-x1;
    def getAverageVelocity(x1, x2, t1, t2):
        """
A particle is in location x1 at time t1 and later goes to x2 at time t2
        """
        return (x2-x1)/(t2-t1)
    def getDisplacementFromAccNTime(acc, t):
        return 0.5 * acc * (t**2)

    def getChangeinVelocity(acc, t):
        return acc*t
    def printEquationsOfMotion():
        print("v = v0 + at")
        print("x = x0 +v0t + 1/2at^2")
        print("v^2 = v0^2 + 2a(x-x0)")
        print("x-x0 = ((v0 + v)/2)t")
    def eqOfMotion1(acc, t, v0=0):
        return v0 + getChangeinVelocity(acc, t)
    def eqOfMotion2(t, acc, x0=0,v0=0):
        return x0 + v0 + getDisplacementFromAccNTime(acc, t)
    def eqOfMotion3(acc, t, x, v0=0, x0=0):
        return v0**2 + 2*a*getDisplacement(x0, x)
    def eqOfMotion4(x2, v, t, v0=0, x1=0):
        return t*getAverageVelocity(x1, x2, t1, t2)

    def graphDisplacementVsTime(velocity, initialDisplacement=0):
        """
            assume velocity is constant
        """
        slope = velocity
        x = np.linspace(0, 10, 10 * slope)
        y=initialDisplacement + (slope*x)
        fig, ax = plt.subplots();
        ax.plot(x, y, linewidth=2.0)

        plt.show()
    def setArrays(slope):
        x= [i for i in range(1,11)]
        y=[i*slope for i in x];
        print(x)
        print(y)



print(Kinematics.getDisplacementFromAccNTime(4,2))
        
