#-- coding: utf-8 --
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']      #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False        #用来正常显示负号

# 定义目标函数（拟合目标）
def aimFunction(x):
    y = pow(x,3)
    return y

# 获取插值点坐标值
def pointsGeneration(start,stop,pointsNum):
    x = np.linspace(start,stop,num=pointsNum)   #在指定区间内均匀地生成散点
    y = []
    for value in x:
        y.append(aimFunction(value))
    return x,y

# Lagrange差值
def lagrange(x,y,x_pre):
    num = len(x)    # 获取插值点个数
    # 计算基函数li(x)
    l_x = []
    for i in range( num ):
        tempResult1 = 1
        tempResult2 = 1
        for k in range(num):
            if i == k:
                continue
            else:
                tempResult1 *= x_pre - x[k]
                tempResult2 *= x[i] - x[k]
        l_x.append( tempResult1 / tempResult2 )
    # 计算Lagrange插值拟合的y值
    result = 0
    for i in range(num):
        result += y[i]*l_x[i]
    return result

if __name__ == '__main__':

    starPoint = -10     # 指定采样点起点坐标
    stopPoint = 10      # 指定采样点终点坐标
    pointsNum = 15      # 指定采样点个数
    x_points,y_points = pointsGeneration(starPoint,stopPoint,pointsNum)

    x,y_true,y_pre = [],[],[]
    for i in range(1,100,1):
        x.append(i)
        y_pre.append(lagrange(x_points,y_points,i))
        y_true.append(aimFunction(i))

    plt.title('拟合结果')
    plt.plot(x,y_true,label = '目标曲线')
    plt.plot(x,y_pre,label = '拟合曲线')
    plt.legend()
    plt.show()






