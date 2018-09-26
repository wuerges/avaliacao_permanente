
class Field:
    def __init__(self, q, i, t, txt):
        self.i = i
        self.t = t
        self.q = q
        self.txt = txt

    def value(self):
        return "v{}".format(self.i)


class Question:
    def __init__(self, i, t):
        self.i = i
        self.txt = t
        self.fields = []

    def name(self):
        return "q{}".format(self.i)


def load_questions(filename):
    questions = []
    question = None

    with open("simples.mf", 'r') as f:
        for i, l in  enumerate(f.readlines()):
            w = l.split()
            t = " ".join(w[1:])
            if w[0] == "P.":
                question = Question(i, t)
                questions.append(question)
            else:
                question.fields.append(Field(question, i, w[0], t))
    return questions
