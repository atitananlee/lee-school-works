import matplotlib.pyplot as plt
import pandas as pd
wtdata = pd.read_csv('wtdata23.csv')
cols = ['Location', 'Temperature_C']
datasong = pd.read_csv('wtdata23.csv', usecols=cols)
trlocate = wtdata['Location'].astype(str).head(110)
trtemp = wtdata['Temperature_C'].astype(int).head(110)
plt.bar(trlocate, trtemp)
plt.xlabel('Location', size=20, color='black')
plt.ylabel('Temperature (°C)', size=20, color='black')
plt.title('Temperature by Location', size=24, color='black')
plt.xticks(rotation=75) 

plt.show()



