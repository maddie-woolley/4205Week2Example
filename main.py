import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
sns.set(color_codes=True)

weather = pd.read_csv('weather.csv')
weather.head()
weather.describe()
weather.isnull()
weather.isna()

plt.figure(figsize=(10, 5))
plt.title('BAR PLOT')
sns.barplot(data=weather, x="humidity", y="temperature")
plt.show()

plt.figure(figsize=(10, 5))
plt.title('HIST PLOT')
sns.distplot(weather['humidity'])
plt.show()

plt.figure(figsize=(10, 5))
plt.title('HIST PLOT')
sns.distplot(weather['humidity'], kde=False, rug=True);
plt.show()

sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
plt.show()

sns.stripplot(data=weather, x="weather_type", y="temperature")
plt.figure(figsize=(10, 5))
plt.title('BOX PLOT')
sns.boxplot(data=weather, x="humidity", y="temperature", hue="weather_type")
plt.show()

plt.figure(figsize=(10, 5))
plt.title('COUNT PLOT')
sns.countplot(x=weather['weather_type'])
plt.show()

sns.pointplot(data=weather, x="humidity", y="temperature", hue="weather_type")
plt.figure(figsize=(10,5))
plt.title('REG PLOT')
sns.regplot(x="humidity", y="temperature", data=weather)
plt.show()


#taken from a class code, and edited to be current
