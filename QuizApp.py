import random
from Questions import Question, QuestionList
import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Creator")
        self.root.configure(bg="grey")
        self.root.geometry("800x600")


        self.question_list = QuestionList()
        self.current_question = 0
        self.score = 0
        self.quiz_started = False

        self.quiz_label = tk.Label(root, text="QuizLIT", font=("Arial", 12), bg="grey")
        self.quiz_label.pack(pady=10)



        self.add_question_button = tk.Button(root, text="Add Question", command=self.add_question_button_clicked,
                                             font=("Arial", 12))
        self.add_question_button.pack()

        self.start_quiz_button = tk.Button(root, text="Start Quiz", command=self.start_quiz, font=("Arial", 12)
                                           )
        self.start_quiz_button.pack()

        self.score_label = tk.Label(root, text="text section", font=("Arial", 12), bg="red")
        self.score_label.pack(pady=10)

       # self.load_questions()
        self.show_question()

    def open_add_question_window(self):
        self.add_question_window = tk.Toplevel(self.root)
        self.add_question_window.title("Add Question")
        self.add_question_window.configure(bg="orange")

        question_label = tk.Label(self.add_question_window, text="Enter Question:", font=("Arial", 12), bg="lightblue")
        question_label.pack(pady=10)

        self.custom_question_entry = tk.Entry(self.add_question_window, font=("Arial", 12))
        self.custom_question_entry.pack(pady=10)

        answer_label = tk.Label(self.add_question_window, text="Correct Answer:", font=("Tacoma", 12), bg="lightgreen")
        answer_label.pack(pady=10)

        self.custom_answer_entry1 = tk.Entry(self.add_question_window, font=("Arial", 12))
        self.custom_answer_entry1.pack(pady=10)

        answer_label = tk.Label(self.add_question_window, text="Option 2:", font=("Tacoma", 12), bg="lightgreen")
        answer_label.pack(pady=10)

        self.custom_answer_entry2 = tk.Entry(self.add_question_window, font=("Arial", 12))
        self.custom_answer_entry2.pack(pady=10)

        answer_label = tk.Label(self.add_question_window, text="Option 3:", font=("Tacoma", 12), bg="lightgreen")
        answer_label.pack(pady=10)

        self.custom_answer_entry3 = tk.Entry(self.add_question_window, font=("Arial", 12))
        self.custom_answer_entry3.pack(pady=10)

        answer_label = tk.Label(self.add_question_window, text="Option 4:", font=("Tacoma", 12), bg="lightgreen")
        answer_label.pack(pady=10)

        self.custom_answer_entry4 = tk.Entry(self.add_question_window, font=("Arial", 12))
        self.custom_answer_entry4.pack(pady=10)

        submit_button = tk.Button(self.add_question_window, text="Submit", command=self.add_custom_question,
                                  font=("Arial", 12))
        submit_button.pack()

    def open_quiz_window(self):
        self.quiz_question_window = tk.Toplevel(self.root)
        self.quiz_question_window.title("Quiz")
        self.quiz_question_window.configure(bg="navy")

        self.quiz_label = tk.Label(self.quiz_question_window, text="", font=("Arial", 12), bg="navy", fg="white")
        self.quiz_label.pack(pady=10)

    def add_question_button_clicked(self):
        self.open_add_question_window()

    def view_question_button_clicked(self):
        self.show_question()

    def add_custom_question(self):
        # Add logic to create a Question instance with the entered details
        question_text = self.custom_question_entry.get()
        correct_answer = self.custom_answer_entry1.get()
        option2 = self.custom_answer_entry2.get()
        option3 = self.custom_answer_entry3.get()
        option4 = self.custom_answer_entry4.get()
        #add the question to the question list

        self.question_list.add_question(Question(question_text,correct_answer, option2, option3, option4, correct_option=correct_answer))

        # Optionally, you can display a message or perform additional actions
        messagebox.showinfo("Question Added", "Question has been added.")
        self.add_question_window.destroy()

    def show_question(self):
        if self.quiz_started and self.current_question < self.question_list.size():
            question = self.question_list.questions[self.current_question]
            self.quiz_label.config(text=question.question_text)

            # Assuming you have an options attribute in your Question class
            options = question.options

            # Variable to store the selected option
            self.selected_option = tk.StringVar()

            # Create Radiobuttons for each option
            for option in options:
                tk.Radiobutton(
                    self.quiz_question_window,
                    text=option,
                    variable=self.selected_option,
                    value=option
                ).pack()

            # Display a submit button
            submit_button = tk.Button(
                self.quiz_question_window,
                text="Submit",
                command=self.check_answer
            )
            submit_button.pack()

        elif self.quiz_started:
            self.show_score()

    def check_answer(self):
        if self.quiz_started and self.current_question < self.question_list.size():
            user_answer = self.selected_option.get()
            if self.question_list.questions[self.current_question].checkAnswer(user_answer):
                self.score += 1
            self.current_question += 1
            self.show_question()

    def show_score(self):
        self.question_label.config(text=self.question_list[self.current_question].showQuestion())
        #self.answer_entry.config(state=tk.DISABLED)
        self.start_quiz_button.config(state=tk.DISABLED)
        self.add_question_button.config(state=tk.DISABLED)
        self.score_label.config(text=f"Quiz completed. Your score: {self.score}/{self.question_list.size()}")
        messagebox.showinfo("Quiz Completed", f"Quiz completed. Your score: {self.score}/{self.question_list.size()}")

    def add_question(self):
        custom_question = self.question_label.cget("text")
        custom_answer = self.answer_entry.get()
        if custom_question and custom_answer:
            self.questions.append((custom_question, custom_answer))
            messagebox.showinfo("Question Added", "Question has been added.")
            self.question_label.config(text="")
            self.answer_entry.delete(0, tk.END)

    def start_quiz(self):
        if not self.question_list.size():
            messagebox.showwarning("Quiz Warning",
                                   "No questions have been added. Please add questions before starting the quiz.")
        else:
            self.quiz_started = True
            self.question_list.shuffle()
            self.open_quiz_window()
            self.show_question()

