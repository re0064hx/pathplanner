import numpy as np
import pandas as pd
import settings as sets

# PathPlannerクラスの定義
class PathPlanner():
    def __init__(self):
        self.path = np.zeros([])
        self.cx = np.zeros([])
        self.cy = np.zeros([])
        self.theta_r = np.zeros([])
        self.rho_r = np.zeros([])

        self.old_nearest_point_index = None
        print("Path planner sucsessfully initialized.")

    def path_generation(self):
        # csv_input = pd.read_csv('reference_path.csv')
        csv_input = pd.read_csv('oval_course.csv')
        self.path = csv_input.values
        self.cx = self.path[:,0]
        self.cy = self.path[:,1]
        self.theta_r = np.arctan2(self.cy, self.cx)

    def search_target_index(self, car):
        # To speed up nearest point search, doing it at only first time.
        if self.old_nearest_point_index is None:
            # search nearest point index
            dx = [car.X - icx for icx in self.cx]
            dy = [car.Y - icy for icy in self.cy]
            d = np.hypot(dx, dy)
            idx = np.argmin(d)
            self.old_nearest_point_index = idx 
        else:
            idx = self.old_nearest_point_index
            distance_this_index = car.calc_distance(self.cx[idx], self.cy[idx])
            while True:
                distance_next_index = car.calc_distance(self.cx[idx + 1], self.cy[idx + 1])
                if distance_this_index < distance_next_index:
                    break
                idx = idx + 1 if (idx + 1) < len(self.cx) else idx
                distance_this_index = distance_next_index
            self.old_nearest_point_index = idx

        Lf = sets.THW_lat * car.V + sets.min_len_lat  # update look ahead distance

        # search look ahead target point index
        while Lf > car.calc_distance(self.cx[idx], self.cy[idx]):
            if (idx + 1) >= len(self.cx):
                break  # not exceed goal
            idx += 1

        print("Index:", idx, " Gaze length:", Lf, " path:", self.cx[idx], self.cy[idx])

        return idx, Lf
