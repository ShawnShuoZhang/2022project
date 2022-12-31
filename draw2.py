import pandas as pd
import wordcloud

# 读取数据
wb = pd.read_excel('language_data.xlsx')
# 关联数据
wb1 = wb.loc[1:, ['Programing', 'data_per']]

confirm_df = dict(zip(wb1['Programing'], wb1['data_per']))

#生成词云
def generate_pic(frequency,name,colormap):
    wd = wordcloud.WordCloud(font_path="c:/Windows/Fonts/STXINGKA.TTF",
                          width=1920, height=1080,
                          background_color="white",
                          colormap=colormap)
    wd.generate_from_frequencies(frequency)
    wd.to_file('%s.png'%name)
    print("已生成词云")


generate_pic(confirm_df,'编译语言热度词云图图','Blues')
