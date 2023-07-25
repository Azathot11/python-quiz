class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_question_text = current_question.text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question_text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() != "true" and user_answer.lower() != "false":
            print("Please enter 'True' or 'False'.")
            self.question_number -= 1
        elif user_answer.lower() == answer:
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


