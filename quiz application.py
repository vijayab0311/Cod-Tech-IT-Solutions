import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("500x400")  # Set the initial size of the window
        self.questions = {
            "Q1": {"question": "What is the capital of Japan?",
                   "options": ["Beijing", "Tokyo", "Seoul", "Bangkok"],
                   "correct_answer": "Tokyo"},
            "Q2": {"question": "Who wrote 'Romeo and Juliet'?",
                   "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"],
                   "correct_answer": "William Shakespeare"},
            "Q3": {"question": "Which planet is known as the Red Planet?",
                   "options": ["Mars", "Venus", "Jupiter", "Mercury"],
                   "correct_answer": "Mars"},
            "Q4": {"question": "Who is credited with inventing the World Wide Web?",
                   "options": ["Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Mark Zuckerberg"],
                   "correct_answer": "Tim Berners-Lee"}
        }
        self.score = 0
        self.current_question = 1
        self.total_questions = len(self.questions)

        self.question_label = tk.Label(self.root, text="", font=("Calibri", 14), fg="indigo")  # Change text color to indigo
        self.question_label.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", command=lambda idx=i: self.check_answer(idx), font=("Calibri", 12), bg="lightgreen")  # Change button background color to lightgreen
            button.pack(fill=tk.X)
            self.option_buttons.append(button)
        
        self.next_question()

    def next_question(self):
        if self.current_question <= self.total_questions:
            q_data = self.questions[f"Q{self.current_question}"]
            self.question_label.config(text=q_data["question"])
            for i, option in enumerate(q_data["options"]):
                self.option_buttons[i].config(text=option)
            self.current_question += 1
        else:
            messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {self.total_questions}!")
            self.root.destroy()

    def check_answer(self, idx):
        selected_option = self.questions[f"Q{self.current_question - 1}"]["options"][idx]
        correct_answer = self.questions[f"Q{self.current_question - 1}"]["correct_answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Correct answer is: {correct_answer}")
        self.next_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
