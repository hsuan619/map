import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #支援中文
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('333.csv', encoding = 'big5') #開啟
#print(df) 確認
bar = []
fliterb = (df["fu"] == "b") 
#print(df.loc[ff, ['fu']])
df = df['fu']

f = df[df== "f"].count()
u = df[df== "u"].count()

for i in fliterb:  #如果是both則n++,f++;
    if(i == True):
        f = f + 1
        u = u + 1

#print(bar)

labels = ['foodpanda','ubereats']  #建立標籤
bar.append(float(f))
bar.append(float(u)) #以小數點方式放入bar(list);


plt.axis('equal') #生成正方形圖
plt.pie(bar,labels = labels,                # 標籤
        autopct = "%1.1f%%",
        colors=['orange','green'],
        textprops = {"fontsize" : 14})
plt.title('Foodpanda&Ubereats比例', fontsize = 20)
plt.show()
#plt.savefig('比例.png', dpi=600)

