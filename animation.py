import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
# from scipy.stats._continuous_distns import t_gen
import numpy as np

import settings as sets

class Animation():
    def __init__(self):
        ## plot 初期化
        # グラフ仕様設定
        # print("Initialization...")
        # self.fig = plt.figure(figsize=(3,15))

        # 軸
        # 最大値と最小値⇒軸の範囲設定
        self.max_x = 40
        self.min_x = -10
        self.max_y = 5
        self.min_y = -5
        # self.fig = plt.figure(figsize=(2,6))
        self.fig, self.ax0 = plt.subplots(figsize=(2,6))
        self.fig.canvas.draw()
        self.fig.show()
    
    def plot_rectangle(self, Car0, Car1, Car2, Car3, Car4):
        # Axes インスタンス作成
        # ax0 = self.fig.add_subplot(111)
        ax0 = self.ax0

        # Limitation of x-axis and y-axis 
        # 描画時，x-y軸は逆転させる
        ax0.set_ylim(self.min_x + Car0.X, self.max_x + Car0.X)
        ax0.set_xlim(self.min_y + Car0.Y, self.max_y + Car0.Y)
        # ax0.set_xlim(self.min_x, self.max_x)
        # ax0.set_ylim(self.min_y, self.max_y)

        # x軸（自車中心座標y軸方向）の正負を逆転
        ax0.invert_xaxis()

        # # 軸の縦横比, 正方形，単位あたりの長さを等しくする
        ax0.set_aspect('equal')
        # self.change_aspect_ratio(ax, 1/5) # 横を1/5倍長く（縦を5倍長く）設定

        # 軸の名前設定
        ax0.set_xlabel('Y [m]')
        ax0.set_ylabel('X [m]')

        # その他グラフ仕様
        ax0.grid(True) # グリッド
        # 凡例
        # ax0.legend()

        # rectangle
        # rect_0 = patches.Rectangle((Car0.Y-Car0.length/2, Car0.X-Car0.width/2),Car0.width,Car0.length,angle=Car0.theta,ec='r', fill=False)
        # rect_1 = patches.Rectangle((Car1.Y-Car1.length/2, Car1.X-Car1.width/2),Car1.width,Car1.length,angle=Car1.theta,ec='b', fill=False)
        # rect_2 = patches.Rectangle((Car2.Y-Car2.length/2, Car2.X-Car2.width/2),Car2.width,Car2.length,angle=Car2.theta,ec='b', fill=False)
        # rect_3 = patches.Rectangle((Car3.Y-Car3.length/2, Car3.X-Car3.width/2),Car3.width,Car3.length,angle=Car3.theta,ec='b', fill=False)
        # rect_4 = patches.Rectangle((Car4.Y-Car4.length/2, Car4.X-Car4.width/2),Car4.width,Car4.length,angle=Car4.theta,ec='b', fill=False)
        rect_0 = patches.Rectangle((Car0.Y-Car0.width/2, Car0.X-Car0.length/2),Car0.width,Car0.length,angle=-Car0.theta*180/np.pi, ec='r', fill=False)
        rect_1 = patches.Rectangle((Car1.Y-Car1.width/2, Car1.X-Car1.length/2),Car1.width,Car1.length,angle=-Car1.theta*180/np.pi, ec='b', fill=False)
        rect_2 = patches.Rectangle((Car2.Y-Car2.width/2, Car2.X-Car2.length/2),Car2.width,Car2.length,angle=-Car2.theta*180/np.pi, ec='b', fill=False)
        rect_3 = patches.Rectangle((Car3.Y-Car3.width/2, Car3.X-Car3.length/2),Car3.width,Car3.length,angle=-Car3.theta*180/np.pi, ec='b', fill=False)
        rect_4 = patches.Rectangle((Car4.Y-Car4.width/2, Car4.X-Car4.length/2),Car4.width,Car4.length,angle=-Car4.theta*180/np.pi, ec='b', fill=False)
        ax0.add_patch(rect_0)
        ax0.add_patch(rect_1)
        ax0.add_patch(rect_2)
        ax0.add_patch(rect_3)
        ax0.add_patch(rect_4)
        plt.pause(sets.Ts)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events() # <-これがないと画面に描画されない。

        # self.fig.delaxes(ax0)
        self.ax0.clear()


    def change_aspect_ratio(self, ax, ratio):
        '''
        This function change aspect ratio of figure.
        Parameters:
            ax: ax (matplotlit.pyplot.subplots())
                Axes object
            ratio: float or int
                relative x axis width compared to y axis width.
        '''
        aspect = (1/ratio) *(ax0.get_xlim()[1] - ax0.get_xlim()[0]) / (ax0.get_ylim()[1] - ax0.get_ylim()[0])
        ax0.set_aspect(aspect)

    def close_figure(self):
        # plt.cla()
        # plt.clf()
        plt.close(self.fig)