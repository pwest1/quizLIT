import random
from Questions import Question, QuestionList
import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuizLIT")
        self.root.configure(bg="royalblue3")
        self.root.geometry("500x400")
        self.root.resizable(width=False, height=False)

        self.question_list = QuestionList()
        self.wrong_answers = ["Chicago", "New York", "Toronto", "Mexico City", "Orlando", "Santa Ana", "Long Beach"]
        self.current_question = 0
        self.score = 0
        self.quiz_started = False

        self.quiz_label = tk.Label(root, text="QuizLIT", font=("Futura", 50, 'bold'), bg="royalblue3")
        self.quiz_label.pack(pady=25)

        self.add_question_button = tk.Button(root, text="Add Question", command=self.add_question_button_clicked,
                                             font=("Futura", 14, 'bold'), height="2", width="10", bg='white',
                                             fg='black', highlightthickness=0, border=0)
        self.add_question_button.pack(pady=10)

        self.start_quiz_button = tk.Button(root, text="Start Quiz", command=self.start_quiz,
                                           font=("Futura", 14, 'bold'), height="2", width="10", bg='white', fg='black',
                                           highlightthickness=0, border=0)
        self.start_quiz_button.pack(pady=10)

        self.score_label = tk.Label(root, text="", font=("Futura", 18, 'bold'), bg='royalblue3', fg='white')
        self.score_label.pack(pady=25)

    def open_add_question_window(self):
        self.add_question_window = tk.Toplevel(self.root)
        self.add_question_window.title("Add Term")
        self.add_question_window.configure(bg="royalblue3")
        self.add_question_window.geometry("250x300")
        self.add_question_window.resizable(width=False, height=False)

        question_label = tk.Label(self.add_question_window, text="Enter Question:", font=("Futura", 14, 'bold'),
                                  bg='royalblue3', fg='white')
        question_label.pack(pady=10)

        self.custom_question_entry = tk.Entry(self.add_question_window, font=("Futura", 12),
                                              highlightbackground='white')
        self.custom_question_entry.pack(pady=10)

        answer_label = tk.Label(self.add_question_window, text="Enter Answer:", font=("Futura", 14, 'bold'),
                                bg='royalblue3', fg='white')
        answer_label.pack(pady=10)

        self.custom_answer_entry1 = tk.Entry(self.add_question_window, font=("Futura", 12),
                                             highlightbackground='white')
        self.custom_answer_entry1.pack(pady=10)

        submit_button = tk.Button(self.add_question_window, text='Submit', command=self.add_custom_question,
                                  font=("Futura", 14, 'bold'), height="2", width="10", bg='white', fg='black',
                                  highlightthickness=0, border=0)
        submit_button.pack(pady=10)

    def open_quiz_window(self):
        self.quiz_question_window = tk.Toplevel(self.root)
        self.quiz_question_window.title("Quiz")
        self.quiz_question_window.configure(bg="royalblue3")
        self.quiz_question_window.geometry("600x300")
        self.quiz_question_window.resizable(width=False, height=False)

        # question label
        self.quiz_label = tk.Label(self.quiz_question_window, text="", font=("Futura", 14, 'bold'), bg="royalblue3",
                                   fg="white")
        self.quiz_label.pack(side=tk.TOP, pady=10)

        # Create Radiobuttons
        options_frame = tk.Frame(self.quiz_question_window)
        options_frame.pack(pady=20)
        options_frame.configure(bg="royalblue3")
        self.selected_option = tk.StringVar()

        # Create RadioButtons with an initial value (empty string)
        self.rb1 = tk.Radiobutton(options_frame, value="", variable=self.selected_option, font=('Futura', 12),
                                  bg="royalblue3", fg='white')
        # self.rb1.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=5)

        self.rb2 = tk.Radiobutton(options_frame, value="", variable=self.selected_option, font=('Futura', 12),
                                  bg="royalblue3", fg='white')
        # self.rb2.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=5)

        self.rb3 = tk.Radiobutton(options_frame, value="", variable=self.selected_option, font=('Futura', 12),
                                  bg="royalblue3", fg='white')
        # self.rb3.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=5)

        self.rb4 = tk.Radiobutton(options_frame, value="", variable=self.selected_option, font=('Futura', 12),
                                  bg="royalblue3", fg='white')
        # self.rb4.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=5)
        self.quiz_question_window.rowconfigure(0, weight=1)
        self.quiz_question_window.columnconfigure(0, weight=1)
        self.quiz_question_window.columnconfigure(1, weight=1)

        # grid layout
        for i, rb in enumerate([self.rb1, self.rb2, self.rb3, self.rb4]):
            row_num = i // 2 + 1
            col_num = i % 2
            rb.grid(row=row_num, column=col_num, sticky=tk.W, padx=20, pady=5)
        submit_button = tk.Button(
            self.quiz_question_window,
            text='Submit',
            command=self.check_answer,
            font=("Futura", 14, 'bold'),
            height="2",
            width="10",
            bg='white',
            fg='black',
            highlightthickness=0,
            border=0
        )
        submit_button.pack(side=tk.BOTTOM, pady=15)

    def add_question_button_clicked(self):
        self.open_add_question_window()

    def view_question_button_clicked(self):
        self.show_question()

    def add_custom_question(self):
        # Add logic to create a Question instance with the entered details
        question_text = self.custom_question_entry.get()
        correct_answer = self.custom_answer_entry1.get()
        self.wrong_answers.append(correct_answer)

        # add the question to the question list

        self.question_list.add_question(Question(question_text, correct_answer))

        # Optionally, you can display a message or perform additional actions
        messagebox.showinfo("Question Added", "Question has been added.")
        self.add_question_window.destroy()

    def show_question(self):
        if self.quiz_started and self.current_question < self.question_list.size():
            question = self.question_list.questions[self.current_question]
            self.quiz_label.config(text=question.question_text)

            question_choices = [question.answer]
            for i in range(3):
                random_number = random.randint(0, len(self.wrong_answers) - 1)

                while self.wrong_answers[random_number] == question.answer or \
                        self.wrong_answers[random_number] in question_choices:
                    random_number = random.randint(0, len(self.wrong_answers) - 1)

                question_choices.append(self.wrong_answers[random_number])

            random_num = random.randint(1, 100)
            for i, rb in enumerate([self.rb1, self.rb2, self.rb3, self.rb4]):
                rb.config(
                    text=question_choices[(random_num + i) % 4],
                    variable=self.selected_option,
                    value=question_choices[(random_num + i) % 4]
                )
        else:

            self.show_score()
            self.quiz_question_window.destroy()

    def check_answer(self):
        user_answer = self.selected_option.get()
        if self.question_list.questions[self.current_question].answer == user_answer:
            self.score += 1
        self.current_question += 1
        self.show_question()

    def show_score(self):

        self.score_label.config(text=f"Quiz completed. Your score: {self.score}/{self.question_list.size()}")
        messagebox.showinfo("Quiz Completed", f"Quiz completed. Your score: {self.score}/{self.question_list.size()}")
        self.score = 0
        self.current_question = 0

    def start_quiz(self):
        if not self.question_list.size():
            messagebox.showwarning("Quiz Warning",
                                   "No questions have been added. Please add questions before starting the quiz.")
        else:
            self.quiz_started = True
            self.question_list.shuffle()
            self.open_quiz_window()
            self.show_question()
