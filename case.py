import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('countries of the world.csv')
print(df['GDP ($ per capita)'].max())
print(df['GDP ($ per capita)'].min())
df['GDP ($ per capita)'].fillna(-1, inplace=True)
df['Literacy (%)'].fillna(-1, inplace=True)
print('Нет данных', len(df[pd.isnull(df['Literacy (%)'])]))
print(df.groupby(by = 'Country')['Literacy (%)'].max())

print(df[df['GDP ($ per capita)'] == 55100])
print(df[df['GDP ($ per capita)'] == 500])
print(df[df['Literacy (%)'] == '100,0'])


    
    

print(df['Literacy (%)'].value_counts())
df['GDP ($ per capita)'].plot(kind = 'line')
df.info()
plt.show()




