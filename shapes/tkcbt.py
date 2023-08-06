import tkinter as tk

# Define the quiz questions and their options
questions = {
    "What is the capital of France?": ["A. Paris", "B. Berlin", "C. London"],
    "What is the largest mammal in the world?": ["A. Elephant", "B. Whale", "C. Gorilla"],
    "What is the currency of Japan?": ["A. Dollar", "B. Yen", "C. Euro"]
}

# Define the correct answers for each question
answers = {
    "What is the capital of France?": "A",
    "What is the largest mammal in the world?": "B",
    "What is the currency of Japan?": "B"
}

# Define variables to keep track of user's score and current question
score = 0
current_question = 0

# Define a function to check the user's answer and update the score
def check_answer(answer):
    global score, current_question
    if answer == answers[list(questions.keys())[current_question]]:
        score += 1
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        display_score()

# Define a function to display the current question and its options
def display_question():
    question_label.config(text=list(questions.keys())[current_question])
    option_a.config(text=questions[list(questions.keys())[current_question]][0])
    option_b.config(text=questions[list(questions.keys())[current_question]][1])
    option_c.config(text=questions[list(questions.keys())[current_question]][2])

# Define a function to display the user's final score
def display_score():
    question_label.config(text=f"Your final score is {score}/{len(questions)}")
    option_a.config(text="")
    option_b.config(text="")
    option_c.config(text="")
    next_button.config(text="Quit", command=root.destroy)

# Create the GUI window
root = tk.Tk()
root.title("Quiz App")
root.geometry("450x350")

# Create the question label and option buttons
question_label = tk.Label(root, text="")
question_label.pack()

option_a = tk.Radiobutton(root, text="", command=lambda: check_answer("A"))
option_a.pack()

option_b = tk.Radiobutton(root, text="", command=lambda: check_answer("B"))
option_b.pack()

option_c = tk.Radiobutton(root, text="", command=lambda: check_answer("C"))
option_c.pack()

# Create the "Next" button to move to the next question
next_button = tk.Button(root, text="Next", command=display_question)
next_button.pack()

# Display the first question
display_question()

root.mainloop()
