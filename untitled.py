class Tree():
    def __init__(self, question):
        self.root = question

    def add_child(self, ):
        pass

    def start_int(self):
        ans = self.root.ask_question()

class Question():
    MAX = 5
    MIN = 2
    def __init__(self, question, ans):
        assert Question.MIN <= len(ans) <= Question.MAX
        self.question = question
        self.ans = ans

    def ask_question(self):
        print(self.question)
        for i in range(len(self.ans)):
            print(str(i) + ": " + self.ans[i])
        while True:
            ans = int(input('--> '))
            if ans >= 0 and ans < len(self.ans):
                break
        return ans

q = Question("Select your gender: ", ["male", "female"])
tree = Tree(q)
tree.start_int()

tree = {
    'male': {
        'party': "smoking",
        'job': {},
        'church': {}
    },
    'female': {}
}