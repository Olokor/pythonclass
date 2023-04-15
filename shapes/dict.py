def game():

    answers = []
    correct_answer = []
    score = 0
    question_number = 1
    print("you have three question for this test")
    for key in questions:
        print("-"*50)
        print(key)
        print("-"*50)

        for option in options[question_number -1]:#options[0]
            print(option)
        
        user_answer = input("enter (A,B,C)").upper()
        answers.append(user_answer)
        correct_answer.append(questions.get(key))
        score += checker(questions.get(key), user_answer)
        question_number += 1

        
    print(f"your answers were {answers}")
    print()
    print(f"correct answers: {correct_answer}")
    print(f"{(score/len(questions))*100}%")




def checker(right_answer, user_answer):

    if right_answer == user_answer:
        return 1
    else:
        return 0







questions = {"1. what is a noun": "C",
           "2. what is a verb": "B",
           "3. how do you bake a cookie": "B",
           "4. how do you get to the supermarket": "C",
           "5. what's the function of a pencil": "A",
           "6. what is a computer":"A"
}

options = [["A. A noun is an action word", "B. A noun deals with python", "C. A noun is a name of anything"], 
           ["A. A verb is a word used instead of noun", "B. A verb is an action word", "C.A verb shows relationship between words "], 
           ["A. we use kettles to make cookie", "B. we use a baking pan and flour to make cookie", "C. we use frying pan to make cookie"],
           ["A. you fly to the supermarket", "B. you walk to the supermarket", "C. you drive to the supermarket"],
           ["A. for writing", "B. for typing", "C. for working"],
           ["A. a computer is a smart dummy", "B. A computer is a super machine", "C. A computer is just dumb"]]



game()
# print(options[0])

# print(type(options))

