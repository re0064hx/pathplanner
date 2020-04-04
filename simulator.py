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
import animation as anim

def main():

    drawer = anim.Animation()

    ''' 描画インスタンス生成 '''
    for n in range(sets.Num_episodes):
        '''車両状態初期化'''
        Car0 = utils.Vehicle(0, 0, 18, 0, 0, 4.8, 1.7, sets.Ts)
        Car1 = utils.Vehicle(30, 1.75, 18, 0, 0, 4.75, 1.75, sets.Ts)
        Car2 = utils.Vehicle(-30, 1.75, 18, 0, 0, 4.75, 1.75, sets.Ts)
        Car3 = utils.Vehicle(15, -1.75, 18, 0, 0, 4.75, 1.75, sets.Ts)
        Car4 = utils.Vehicle(-15, -1.75, 18, 0, 0, 4.75, 1.75, sets.Ts)

        drawer.set_fig()
        # ここのFORループはアニメーション関数に全部委ねられる
        for m in range(sets.MaxLoopTimes):
            drawer.plot_rectangle(Car0, Car1, Car2, Car3, Car4)
            # drawer.close_figure()
            Car0.state_update(18,0)
            Car1.state_update(17,0)
            Car2.state_update(18,0)
            Car3.state_update(16,0)
            Car4.state_update(20,0)

            print("\r[{0}] {1}/{2}".format("="*(m+1)+"-"*(sets.MaxLoopTimes-m-1) , m+1, sets.MaxLoopTimes), end="")
        drawer.close_figure()
        print("")


if __name__ == "__main__":
    main()
