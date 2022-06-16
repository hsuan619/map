
import folium # 匯入 folium 套件
import pandas as pd

df = pd.read_csv('2222.csv', encoding = 'big5')


def parse_zhch(s):
        return str(str(s).encode('ascii' , 'xmlcharrefreplace'))[2:-1]
loc = []
fliteru = (df["url"])
fliters = (df["店家"])
fliterf = (df["food"])
fmap = folium.Map(location=[23.6960, 120.5341], zoom_start=15)

(folium.Marker(location=[23.6960, 120.5341],popup='YUNTECH',icon=folium.Icon(color = 'green',icon_color = 'white', icon='home', prefix='glyphicon'))).add_to(fmap)

for x, y , s , url, f in zip(df["x"],df["y"], fliters, fliteru, fliterf):
    (folium.Marker(location=[x,y], popup=parse_zhch('<b>'+ s + '</b><a href=' + url + ' target="_blank">' + f + '</a>'), width=750, height=500)).add_to(fmap)


fmap.save('fin.html')
