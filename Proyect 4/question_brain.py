class QuizBrain:
    def __init__(self, quiz):
        self.score = 0
        self.question_number = 0
        self.question_list = quiz

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].question} True/False: ")
        self.question_number += 1
        self.check_question(user_answer, current_question.answer)

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def check_question(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct answer uwu")
            self.score += 1
        else:
            print("Incorrect answer")
