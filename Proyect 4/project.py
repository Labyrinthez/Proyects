from data import question_data
from question import Question
from question_brain import QuizBrain

question_bank = []
for i in question_data:
    new_question = Question(i["question"], i["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()
    print(f"Score: {quiz.score}/ {quiz.question_number}")