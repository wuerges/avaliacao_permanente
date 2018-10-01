import pandas as pd
import matplotlib.pyplot as plt
import json
import urllib

data = []

with open('data/responses.json', 'r') as f:
    for l in f.readlines():
        data.append(json.loads(l))


df = pd.DataFrame()
df['merge'] = 1

for d in data:
    #dl = list(zip(*d))
    #print(dict(d))
    x = dict((k, [v]) for k,v in d)
    df1 = pd.DataFrame(x)
    df1['merge'] = 1
    #print(df1)

    df = df.merge(df1, how='outer')

df = df.drop('merge', axis=1)

# Resultados agrupados por turma

for turma, frame  in df.groupby('turma'):
    print("------", turma, "-----")
    for column in frame.columns if column != 'turma':
        group = frame.groupby([column]).size().reset_index(name='counts')
        plt.pie(group['counts'],labels=group[column])
        plt.show()

for turma, frame  in df.groupby('turma'):
    print("------", turma, "-----")
    for column in frame.columns:
        group = frame.groupby([column]).size().reset_index(name='counts')
        plt.pie(group['counts'],labels=group[column])
        plt.show()
