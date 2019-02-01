import pandas as pd # 导入pandas库用来处理csv文件
import matplotlib.pyplot as plt # 导入matplotlib.pyplot并用plt简称

unrate = pd.read_csv('/users/zehe/Desktop/archive.csv') # 读csv文件
# 通过pd.to_datetime函数将unrate.csv文件中'DATE'属性数据的strin数据类型转换为time类型
print(unrate.head(32)) # 打印查看前12行数据

first_twelve = unrate[0:32] # 取前12行数据

plt.scatter(first_twelve['avgrank'], first_twelve['avgsalary']/1000000)

plt.xlabel('AvgRank') # 给x轴数据加上名称
plt.ylabel('AvgSalary/Billion') # 给y轴数据加上名称

plt.show() # 将刚画的图显示出来
