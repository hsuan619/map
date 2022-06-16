import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('333.csv', encoding = 'big5')
#print(df)
bar = []
df = df['fu'] #篩選
#計算數量
f = df[df== "f"].count()
u = df[df== "u"].count()
b = df[df== "b"].count()
n = df[df== "n"].count()

#放入list
bar.append(f)
bar.append(u)
bar.append(b)
bar.append(n)
#print(bar)
labels = ['foodpanda','ubereats','both','none']

x = np.arange(len(labels)) #arange(4) = index[0~3]
print(x)
plt.bar(x, bar,color=['deeppink', 'green', 'blue', 'black'])
plt.xticks(x, labels)#plt.xticks(數量,標籤)

plt.xlabel("外送平台")
plt.ylabel("數量")
plt.title("雲科附近外送平台數量")
plt.show()
#plt.savefig('數量.jpg', dpi=300)