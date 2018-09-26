class Oferta:
    def __init__(self, t, d):
        self.turma = t
        self.disciplina = d
        self.codigo = t.split()[0]

    def __repr__(self):
        return "O{}".format(self.codigo)


def load_ofertas(filename):
    ofertas = []
    turma     = None
    disciplina = None

    with open(filename, 'r') as f:
        for i, l in  enumerate(f.readlines()):
            w = l.split()
            t = " ".join(w[1:])
            if w[0] == "T.":
                if turma:
                    ofertas.append(Oferta(turma, disciplina))
                turma = t
            if w[0] == "D.":
                disciplina= t
            else:
                pass
        if turma:
            ofertas.append(Oferta(turma, disciplina))
    return dict( (o.codigo, o) for o in ofertas )


if __name__ == '__main__':
    print(load_ofertas("ofertas.mf"))
