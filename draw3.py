import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']


def visible_python():
    # 从excel中提取数据形成dataframe
    language_df = pd.read_excel('language_data.xlsx')
    python_df = language_df.iloc[220:255,:]
    c_df = language_df.iloc[475:510, :]
    cplus_df = language_df.iloc[730:765,:]
    java_df = language_df.iloc[985:1020, :]
  #  print(python_df);
    time = python_df["Date"]
    data = python_df["data_per"]

    time_c = c_df["Date"]
    data_c = c_df["data_per"]

    time_cp = cplus_df["Date"]
    data_cp = cplus_df["data_per"]

    time_j = java_df["Date"]
    data_j = java_df["data_per"]

    fig ,ax = plt.subplots()
    plt.title('python2020-2022热度变化折线图')

    t1 = plt.plot(time,data)
    t2 = plt.plot(time_c,data_c)
    t3 = plt.plot(time_cp,data_cp)
    t4 = plt.plot(time_j,data_j)

    plt.xlabel("日期")
    plt.ylabel("热度值")
    plt.xticks(np.arange(0, len(time)),rotation=45)
    plt.legend(["python","c","c++","java"])
    plt.savefig("主流编程语言2020-2022热度变化折线图.png")
    plt.show()
visible_python();