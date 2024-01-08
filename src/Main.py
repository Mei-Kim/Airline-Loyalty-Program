import psycopg2
import matplotlib as mp
import seaborn as sb
import pandas as pd
import numpy as np

# read csv into pandas DataFrame
df1 = pd.read_csv('/Users/meikimura/Desktop/project/Airline-Loyalty-Program/data/Customer_Flight_Activity.csv')
df2 = pd.read_csv('/Users/meikimura/Desktop/project/Airline-Loyalty-Program/data/Customer_Loyalty_History.csv')

# Merge DataFrames based on common column
merge_df = pd.merge(df1, df2, on='Loyalty_Number')