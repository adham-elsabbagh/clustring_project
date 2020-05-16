import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer


# list_of_lists = []
#
# with open('data') as f:
#     for line in f:
#         inner_list = [line.strip() for line in line.split('\t')]
#         list_of_lists.append(inner_list)
#
# df = pd.DataFrame(list_of_lists)
# df['headline_text']=df[0]
# df=df.iloc[:,-1]
#
# print(df.head())
# print(df.info())
df=pd.read_csv('data2.csv')
# df=df.iloc[:,-1]
# df.drop('id')
print(df.head())
print(df.columns)
print(df.info())