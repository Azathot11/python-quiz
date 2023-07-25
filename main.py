from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

quiz_start = True

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    generated_question = Question(question_text, question_answer)
    question_bank.append(generated_question)

quiz = QuizBrain(question_bank)

print()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")