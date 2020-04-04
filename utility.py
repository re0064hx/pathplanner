import numpy as np

class Vehicle():
    def __init__(self, init_x, init_y, vx, vy, theta, length, width, Ts):
        # self.time = utils.time
        self.X = init_x
        self.Y = init_y
        self.Vx = vx
        self.Vy = vy
        self.V = np.sqrt(np.power(vx, 2) + np.power(vy, 2))
        self.theta = theta
        self.delta = delta
        self.length = length
        self.width = width
        self.dt = Ts

    def state_update(self, V, YR):
        #座標系に注意
        self.x += V*np.sin(self.theta) * self.dt # longitudinal coordinate value
        self.y += V*np.cos(self.theta) * self.dt # lateral coordinate value
        self.theta += YR * self.dt

