class QuizBrain:

    # constructor - default value of question_number set to 0, question_list is a list of object Question
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    # check if there are still some questions in the list. returns boolean
    def still_has_questions(self):
        list_length = len(self.question_list)
        return self.question_number < list_length

    # method will pull out a question from question_list based on question_number
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"[Q.{self.question_number}]: {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question.answer)

    # check if the user's answer is correct or not. based on that it will give a point or not
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That is correct!")
        else:
            print("That is wrong!")
            print(f"The correct answer is: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}\n")

    # returns score
    def get_score(self):
        return self.score

    # returns question number
    def get_question_number(self):
        return self.question_number
