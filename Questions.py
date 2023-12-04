import random


class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

    def questionText(self):
        return self.question_text


class QuestionList:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.questions:
            return self.questions.pop(0)
        else:
            return None

    def size(self):
        return len(self.questions)

    def shuffle(self):
        random.shuffle(self.questions)

    def getCurrentQuestion(self, qnum):
        return self.questions[qnum]
