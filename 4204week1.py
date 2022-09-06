import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
sns.set(color_codes=True)
weather = pd.read_csv('weather.csv')



plt.figure(figsize=(10,5))
plt.title('HIST PLOT')
sns.distplot(weather['humidity'], kde=False, rug=True);
plt.show()


sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
plt.show()
sns.stripplot(data=weather, x="weather_type", y="temperature", hue="weather_type")


plt.figure(figsize=(10,5))
plt.title('BOX PLOT')
sns.boxplot(data=weather, x="humidity", y="temperature", hue="weather_type")
plt.show()

plt.figure(figsize=(10,5))
plt.title('COUNT PLOT')
sns.countplot(weather['weather_type'])
plt.show()

sns.pointplot(weather['humidity'][0:10], weather['temperature'][0:10], hue=weather['weather_type'])
plt.figure(figsize=(10,5))
plt.title('REG PLOT')
sns.regplot(x="humidity", y="temperature", data=weather)
plt.show()
