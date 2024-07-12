from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for index in question_data:
    question_text=index["text"]
    question_answer=index["answer"]
    new_question=Question(question_text, question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
    if quiz.question_number+1 > len(quiz.question_list):
        print("You've completed the quiz.")
        print(f"Your final score is: {quiz.score}/{quiz.question_number}") #it could also be /{len(question_bank)}