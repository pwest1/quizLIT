import random
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Creator")
        self.root.configure(bg="red")

        self.questions = []
        self.current_question = 0
        self.score = 0
        self.quiz_started = False

        self.question_label = tk.Label(root, text="", font=("Arial", 12), bg="red")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(root, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        self.add_question_button = tk.Button(root, text="Add Question", command=self.add_question, font=("Arial", 12))
        self.add_question_button.pack()

        self.start_quiz_button = tk.Button(root, text="Start Quiz", command=self.start_quiz, font=("Arial", 12)
                                          )
        self.start_quiz_button.pack()

        self.score_label = tk.Label(root, text="", font=("Arial", 12), bg="red")
        self.score_label.pack(pady=10)

        self.load_questions()
        self.show_question()

    def load_questions(self):
        # Initialize an empty list for questions
        self.questions = []

    def show_question(self):
        if self.quiz_started and self.current_question < len(self.questions):
            question, _ = self.questions[self.current_question]
            self.question_label.config(text=question)
            self.answer_entry.delete(0, tk.END)
        elif self.quiz_started:
            self.show_score()

    def check_answer(self):
        if self.quiz_started and self.current_question < len(self.questions):
            _, answer = self.questions[self.current_question]
            user_answer = self.answer_entry.get()
            if user_answer.lower() == answer.lower():
                self.score += 1
            self.current_question += 1
            self.show_question()

    def show_score(self):
        self.question_label.config(text="")
        self.answer_entry.config(state=tk.DISABLED)
        self.start_quiz_button.config(state=tk.DISABLED)
        self.add_question_button.config(state=tk.DISABLED)
        self.score_label.config(text=f"Quiz completed. Your score: {self.score}/{len(self.questions)}")
        messagebox.showinfo("Quiz Completed", f"Quiz completed. Your score: {self.score}/{len(self.questions)}")

    def add_question(self):
        custom_question = self.question_label.cget("text")
        custom_answer = self.answer_entry.get()
        if custom_question and custom_answer:
            self.questions.append((custom_question, custom_answer))
            messagebox.showinfo("Question Added", "Question has been added.")
            self.question_label.config(text="")
            self.answer_entry.delete(0, tk.END)

    def start_quiz(self):
        if not self.questions:
            messagebox.showwarning("Quiz Warning", "No questions have been added. Please add questions before starting the quiz.")
        else:
            self.quiz_started = True
            random.shuffle(self.questions)
            self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
