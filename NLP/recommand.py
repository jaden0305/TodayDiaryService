import pandas as pd
import numpy as np
import random

data = pd.read_csv('C:/Users/multicampus/Desktop/response.csv', encoding='CP949')

print(data.head())

print(data.happy)

choice = random.choice(data.sad)
print(choice, type(choice))