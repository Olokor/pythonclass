def cbt():

    user_answer = []
    correct_answer  = []
    score = 0
    question_number = 1
    print("you have 5 questions for this test!")
    for question in questions:
        print("-"*50)
        print(question)
        print("-"*50)

        for option in options[question_number -1]:
            print(option)
        user_input = input("enter (A, B, C)").upper()
        user_answer.append(user_input)
        correct_answer.append(questions.get(question))
        score += checker(user_input, questions.get(question))
        question_number += 1

    print(f"your answers were {user_answer}")
    print()
    print(f"correct answers: {correct_answer}")
    print(f"{(score/len(questions))*100}%")


def checker(user_input, right_answer):
    if user_input == right_answer:
        return 1
    else:
        return 0


questions = {
    "1. what is noun": "A",
    "2. who is doctor": "C",
    "3. what is computer": "C",
    "4. what is the name of the library in python that is used for drawing":"B",
    "5. what is the function of the random library in python": "A"
}

options = [
    ["A. a noun is a name of anything", 
    "B. a noun is an action word",
    "C. a noun is a word that shows relationship"],
    ["A. a doctor is food",
    "B. a doctor is person that does codding",
    "C. a doctor is a person that treats sick people"],
    ["A. a computer is a magical divice",
    "B. a computer is a medical device",
    "C. A computer is a smart dummy"],
    ["A. tkinter", "B. turtle", "C. random"],
    ["A. picks items at random from a list of different items", 
    "B. for doing math calaclations",
    "C. for doing websearch"]
]

cbt()