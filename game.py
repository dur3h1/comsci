import tkinter as tk
import random
from tkinter import messagebox

# Questions categorized by chapter
questions_by_chapter = {
    "Chapter 1: Data Representation": {
        "What is the binary value of 1010?": "10",
        "What is a bit?": "A binary digit"
    },
    "Chapter 2: Communication and Internet Technologies": {
        "What does HTTP stand for?": "Hypertext Transfer Protocol",
        "What is the function of a router?": "Directs data traffic"
    },
    # Continue adding questions up to Chapter 13
}

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("IGCSE Computer Science Quiz")
        self.score = 0
        self.questions = []
        self.current_question = 0

        # Prepare questions from all chapters
        for chapter in questions_by_chapter:
            self.questions += list(questions_by_chapter[chapter].items())

        random.shuffle(self.questions)  # Shuffle for randomness
        
        self.total_questions = len(self.questions)
        
        # UI Elements
        self.label_question = tk.Label(root, text=self.questions[self.current_question][0], font=("Arial", 14))
        self.label_question.pack(pady=20)
        
        self.entry_answer = tk.Entry(root, width=50)
        self.entry_answer.pack(pady=10)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
        
        self.label_score = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14))
        self.label_score.pack(pady=10)

    def check_answer(self):
        user_answer = self.entry_answer.get().strip()
        correct_answer = self.questions[self.current_question][1]
        
        if user_answer.lower() == correct_answer.lower():
            self.score += 10
            messagebox.showinfo("Correct!", "Great job!")
        else:
            self.score -= 5
            messagebox.showerror("Wrong!", f"The correct answer was: {correct_answer}")
        
        self.current_question += 1
        self.entry_answer.delete(0, tk.END)
        
        if self.current_question < self.total_questions:
            self.label_question.config(text=self.questions[self.current_question][0])
        else:
            messagebox.showinfo("Quiz Over", f"Your final score is: {self.score}")
            self.root.quit()
        
        self.label_score.config(text=f"Score: {self.score}")

# Initialize the game
root = tk.Tk()
game = QuizGame(root)
root.mainloop()