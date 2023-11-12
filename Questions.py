import random

class Question:
    def __init__(self, question_text, *options, correct_option=None):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option
    def checkAnswer(self, user_answer):
        return user_answer.lower == self.correct_option.lower
    def questionTest(self):
        return self.question_text



class QuestionList:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def shuffle_questions(self):
        random.shuffle(self.questions)

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