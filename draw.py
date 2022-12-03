import pandas as pd
import xlrd2
import imp
import pyecharts.options as opts
from pyecharts.charts import Timeline, Bar
from pyecharts.globals import CurrentConfig

if __name__ == '__main__':
    imp.reload(xlrd2)

# CurrentConfig.ONLINE_HOST = 'D:/python/pyecharts-assets-master/assets/'

# 提取编程语言名字
name = list(pd.read_excel('E:\\Pycharm\\2022\\language_data.xlsx')['Programing'].drop_duplicates())

data = xlrd2.open_workbook('E:\\Pycharm\\2022\\language_data.xlsx')
table = data.sheets()[0]

dic1 = {k: [] for k in name}
# 各编程语言对应每年里不同时间的热度
for i in range(1, table.nrows):
    x = table.row_values(i)
    dic1[x[0]].append((x[1], x[2]))

# 与编程语言顺序对应  每年编程语言对应的不同时间的热度
data_per = {k: [[] for x in range(10)] for k in range(2001, 2023)}
print(data_per)

count = 0
for k, v in dic1.items():
    for j in v:  # v (时间，热度)  热度数据添加进各年对应的列表里
        data_per[int(j[0][:4])][count].append(eval(j[1]))  # 一年里各编程语言不同时间时的热度  对应起来
    count += 1

# print(data_per)
data_per1 = {k: [] for k in list(data_per.keys())}

for k, v in list(data_per.items()):
    for x in v:
        if len(x) == 0:  # 这一年里该语言没有热度数据
            data_per1[k].append(0)
        else:
            avg = sum(x) / len(x)
            data_per1[k].append(avg)  # 这一年里的平均热度

# 得到TOBIE现在排Top20的编程语言从2001年开始每年的平均热度
print(data_per1)


def get_year_overlap_chart(year) -> Bar:
    sum_info = [(m, n) for m, n in zip(name, data_per1[year])]
    # 编程语言按每年平均热度排序
    sum_info.sort(key=lambda z: z[1], reverse=True)
    name_ = [m[0] for m in sum_info]
    datas = [m[1] for m in sum_info]
    # 每根柱子的颜色列表
    colors = ['#00BFFF', '#0000CD', '#000000', '#008000', '#FF1493', '#FFD700', '#FF4500', '#00FA9A', '#191970',
              '#9932CC']
    x = []
    for i in range(10):
        x.append(
            opts.BarItem(
                name=name_[i],
                value=datas[i],
                itemstyle_opts=opts.ItemStyleOpts(color=colors[i])  # 设置每根柱子的颜色
            )
        )
    # 绘制柱形图
    bar = Bar()
    bar.add_xaxis(name_)
    bar.add_yaxis(series_name='热度', y_axis=x, is_selected=True,
                  label_opts=opts.LabelOpts(is_show=False))
    bar.set_global_opts(title_opts=opts.TitleOpts(
        title="2009-2019编程语言热度"),
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="shadow"),
        xaxis_opts=opts.AxisOpts(name='编程语言'), yaxis_opts=opts.AxisOpts(name='热度'),
    )
    return bar


# 生成时间轴的图
timeline = Timeline(init_opts=opts.InitOpts(width="1200px", height="600px"))
for y in range(2009, 2020):
    timeline.add(get_year_overlap_chart(y), time_point=str(y))

timeline.add_schema(is_auto_play=True, play_interval=1000)
timeline.render("language_2009_2019.html")
