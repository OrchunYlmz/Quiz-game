class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list= question_list
        self.score=0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # if len(self.question_list) < self.question_number+1:
        #     return False
        # else:
        #     return True

    def next_question(self):
        quest=self.question_list[self.question_number]
        self.question_number+=1
        ask=input(f"Q.{self.question_number}: {quest.text} (True/False): ")
        self.check_answer(ask, quest.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong.")
        print(f"The answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
