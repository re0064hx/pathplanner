import math
import numpy as np
import utility as utils

class Controller():
    def __init__(self):
        self.e1 = 0.0
        self.e2 = 0.0
        self.e3 = 0.0
        print("Controller sucsessfully initialized.")

    def calc_error(self):
        self.e1 = self.X
        self.e2 = self.Y
        self.e3 = self.theta

    def kanayama_method(self):
        '''
        This function is calculate lateral control input
        based on Kanayama's method.
        '''
        K2 = 0.05
        K3 = 0.2
        rho = 0
        # e2 = RefPath.Y[l-1, 0] - Car0.Y[l-1, 0]
        # e3 = RefPath.theta[l-1, 0] - Car0.theta[l-1, 0]

        term1 = (Car0.Kf*Car0.lf - Car0.Kr*Car0.lr)/(Car0.Kf*Car0.V[l-1, 0]) * Car0.YR[l-1, 0]
        term2 = (Car0.Kf + Car0.Kr)/(Car0.Kf) * Car0.beta[l-1, 0]
        term3 = (Car0.m * Car0.V[l-1, 0])/(2*Car0.Kf) * (rho*(Car0.V[l-1, 0]*np.cos(Car0.e3[l-1, 0]))/(1-Car0.e2[l-1, 0]*rho) - K2*Car0.e2[l-1, 0]*Car0.V[l-1, 0] - K3*np.sin(Car0.e3[l-1, 0]))

        self.delta = term1 + term2 + term3
        return self.delta

    def pure_pursuit(self, car, path, pidx):
        idx, Lf = path.search_target_index(car)

        if pidx >= idx:
            idx = pidx

        if idx < len(path.cx):
            tx = path.cx[idx]
            ty = path.cy[idx]
        else:  # toward goal
            tx = path.cx[-1]
            ty = path.cy[-1]
            idx = len(path.cx) - 1

        alpha = math.atan2(ty - car.Y, tx - car.X) - car.theta
        delta = math.atan2(2.0 * (car.length) * math.sin(alpha) / Lf, 1.0)

        return delta*np.pi/180.0, idx