# -*- coding: utf-8 -*-
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import matplotlib

import settings as sets
import utility as utils
import animation
import controller
import pathplanner

def main():
    ''' === Create instance === '''
    drawer = animation.Animation()
    ctrl = controller.Controller()
    planner = pathplanner.PathPlanner()

    '''
        Simulation
    '''
    for n in range(sets.Num_episodes):
        ''' === Initialization === '''
        # Set each vehicle's parameters
        Car0 = utils.Vehicle(0, 0, 18, 0, 0, 0, 0, 0, 4.8, 1.7, sets.Ts)
        Car1 = utils.Vehicle(10, 3.5, 18, 0, 0, 0, 0, 0, 4.75, 1.75, sets.Ts)
        Car2 = utils.Vehicle(-5, 3.5, 16, 0, 0, 0, 0, 0, 4.75, 1.75, sets.Ts)
        Car3 = utils.Vehicle(30, 0, 19, 0, 0, 0, 0, 0, 4.75, 1.75, sets.Ts)
        Car4 = utils.Vehicle(-10, 0, 18, 0, 0, 0, 0, 0, 4.75, 1.75, sets.Ts)
        # Load reference course
        planner.path_generation()
        target_idx, _ = planner.search_target_index(Car0)

        # Animation settings
        drawer.plot_lane(planner.path, target_idx)
        drawer.plot_rectangle(Car0, Car1, Car2, Car3, Car4)

        ''' === Main Procedure === '''
        # ここのFORループはアニメーション関数に全部委ねられる
        for m in range(sets.MaxLoopTimes):
            ''' 描画設定 '''
            drawer.plot_lane(planner.path, target_idx)
            # yaw角度変化を表示したい時
            drawer.plot_rectangle(Car0, Car1, Car2, Car3, Car4)
            # 描画を少し早くする時
            # drawer.plot_loop(Car0, Car1, Car2, Car3, Car4)

            ''' 制御演算 '''
            # 注視点更新
            planner.search_target_index(Car0)
            # 制御演算
            delta, target_idx = ctrl.pure_pursuit(Car0, planner, target_idx)
            # 車両状態更新
            Car0.state_update(18,0,0,delta)
            Car1.state_update(18.5,0,0,0)
            Car2.state_update(17,0,0,0)
            Car3.state_update(19,0,0,0)
            Car4.state_update(17,0,0,0)

            # print("\r[{0}] {1}/{2}".format("="*(m+1)+"-"*(sets.MaxLoopTimes-m-1) , m+1, sets.MaxLoopTimes), end="")
        
        ''' === Finalize === '''
        drawer.close_figure()
        print("")


if __name__ == "__main__":
    main()
