import pandas as pd 
import matplotlib.pyplot as plt 
pokemon_dataframe = pd.read_csv('/home/tintin/study/Data-science/Feature-engineering/Pokemon.csv', encoding='utf-8',sep =',')
#print(pokemon_dataframe.head())
#print('Len: ', len(pokemon_dataframe))
#pokemon_dataframe.info()
#print(pokemon_dataframe['Name'].head(5))
pokemon_dataframe[['HP', 'Attack','Defense']].describe()