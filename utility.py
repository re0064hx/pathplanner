import numpy as np

import settings as sets

class Vehicle():
    def __init__(self, init_x, init_y, vx, vy, init_delta, theta, YR, beta, length, width, dt):
        self.time = 0.0
        self.X = init_x
        self.Y = init_y
        self.Vx = vx
        self.Vy = vy
        self.V = np.sqrt(np.power(self.Vx, 2) + np.power(self.Vy, 2))
        self.theta = theta
        self.YR = YR
        self.beta = beta
        self.delta = init_delta
        self.length = length
        self.width = width
        self.dt = dt

        self.Kf = 40000
        self.Kr = 70000
        self.I = 3500
        self.lf = 2.2
        self.lr = self.length - self.lf
        self.m = 2000

    def state_update(self, Vx, Vy, YR, delta_ctrl):
        self.time += sets.Ts
        self.delta = delta_ctrl
        self.Vx = Vx
        self.Vy = Vy
        self.V = np.sqrt(np.power(self.Vx, 2) + np.power(self.Vy, 2))
        # kinematic model
        # self.kinematic_model()
        # dynamic model
        self.dynamic_model()
        

    def dynamic_model(self):
        beta_dot = -2*(self.Kf+self.Kr)/(self.m*self.V) * self.beta - (self.m*self.V + 2*(self.lf*self.Kf-self.lr*self.Kr)/self.V)/(self.m*self.V)*self.YR + (2*self.Kf)/(self.m*self.V)*self.delta
        YR_dot = -2*(self.lf*self.Kf-self.lr*self.Kr)/self.I*self.beta - 2*(np.power(self.lf,2)*self.Kf+np.power(self.lr,2)*self.Kr)/(self.I*self.V)*self.YR + (2*self.lf*self.Kf)/self.I*self.delta
        
        self.beta += beta_dot*self.dt
        self.YR += YR_dot*self.dt
        self.theta += + self.YR * self.dt
        self.X += self.V*np.cos(self.theta + self.beta) * self.dt # longitudinal coordinate value
        self.Y += self.V*np.sin(self.theta + self.beta) * self.dt # lateral coordinate value

    def kinematic_model(self):
        # kinematic model
        self.X += self.V*np.cos(self.theta) * self.dt # longitudinal coordinate value
        self.Y += self.V*np.sin(self.theta) * self.dt # lateral coordinate value
        self.theta += self.YR * self.dt

