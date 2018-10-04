import pandas as pd
import matplotlib.pyplot as plt
import json
import urllib

data = []

with open('data/responses.json', 'rb') as f:
    for l in f.readlines():
        x = l.decode('unicode_escape').encode('latin').decode('utf8')
        data.append(json.loads(x))


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

class Tag:
    def __init__(self, cr, f):
        self.cr = cr
        self.f = f
    def __enter__(self):
        print("<{}>".format(self.cr), file=self.f)
    def __exit__(self, type, value, traceback):
        print("</{}>".format(self.cr), file=self.f)
# Resultados agrupados por turma

for turma, frame  in df.groupby('turma'):
    with open("outputs/turma_{}.html".format(turma), 'w') as f:
        print("<html><head><meta charset=\"UTF-8\"></head><body>", file=f)
        print("<h1> Turma", turma ,"</h1>", file=f)
        for i, column in enumerate(frame.columns):
            if not column in {'turma', 'time'}:
                print("<h2>", column ,"</h2>", file=f)
                group = frame.groupby([column]).size().reset_index(name='counts')
                fig = plt.figure()
                plt.pie(group['counts'],labels=group[column])
                imgname = "turma_{}_imagem_{}.png".format(turma, i)
                fig.savefig("outputs/"+imgname)

                with Tag("table", f):
                    with Tag("tr", f):
                        for gc in group[column]:
                            with Tag("td", f):
                                print(gc, file=f)
                    with Tag("tr", f):
                        for gc in group['counts']:
                            with Tag("td", f):
                                print(gc, file=f)

                print("<img src={} />".format(imgname), file=f)
        print("</body></html>", file=f)

with open("outputs/total.html", 'w') as f:
    print("<html><head><meta charset=\"UTF-8\"></head><body>", file=f)

    for i, column in enumerate(frame.columns):
        if not column in {'time'}:
            if column == "turma":
                print("<h2> Resultado agregado para todas as turmas </h2>", file=f)
            else:
                print("<h2>", column ,"</h2>", file=f)


            group = frame.groupby([column]).size().reset_index(name='counts')

            fig = plt.figure()
            plt.pie(group['counts'],labels=group[column])
            imgname = "total_imagem_{}.png".format(i)
            fig.savefig("outputs/"+imgname)

            with Tag("table", f):
                with Tag("tr", f):
                    for gc in group[column]:
                        with Tag("td", f):
                            print(gc, file=f)
                with Tag("tr", f):
                    for gc in group['counts']:
                        with Tag("td", f):
                            print(gc, file=f)
            print("<img src={} />".format(imgname), file=f)

    print("</body></html>", file=f)
