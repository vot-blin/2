import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv(r'C:\Users\User\Downloads\Telegram Desktop\test.csv')
print(dataset.info())
print(dataset.isnull().sum())
print(dataset.describe())
print(dataset.select_dtypes(include=['object']).nunique())