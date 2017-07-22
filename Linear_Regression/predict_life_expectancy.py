import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_csv('bmi_and_life_expectancy.csv')
x_values = dataframe[['BMI']]
y_values = dataframe[['Life_Expectancy']]

#train model on data
regression = LinearRegression()
regression.fit(x_values, y_values)
predict = regression.predict(21.07931)
print(predict)

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, regression.predict(x_values))
plt.show()

