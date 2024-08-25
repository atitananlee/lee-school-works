import matplotlib.pyplot as plt
import pandas as pd
wtdata = pd.read_csv('wtdata2.csv')
cols = ['Location', 'Temperature_C']
datasong = pd.read_csv('wtdata2.csv', usecols=cols)
trlocate = wtdata['Location'].astype(str)  
trtemp = wtdata['Temperature_C']
print(trlocate)
print(trtemp)