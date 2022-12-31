import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']


def visible_python():
    # 从excel中提取数据形成dataframe
    language_df = pd.read_excel('language_data.xlsx')
    python_df = language_df.iloc[220:255,:]
  #  print(python_df);
    time = python_df["Date"]
    data = python_df["data_per"]

    fig ,ax = plt.subplots()
    plt.title('python2020-2022热度变化折线图')

    t1 = plt.plot(time,data)

    plt.xlabel("日期")
    plt.ylabel("热度值")
    plt.xticks(np.arange(0, len(time)),rotation=40)

    plt.savefig("python2020-2022热度变化折线图.png")
    plt.show()
visible_python();