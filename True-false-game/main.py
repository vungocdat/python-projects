# True False game
# answer true or false based on the question given. For correct answer - +1 point, for wrong +0 point

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# creating Question objects and save them to the list called question_bank
question_bank = []
for i in question_data:
    question = Question(i["text"], i["answer"])
    question_bank.append(question)

# starting game created by QuizBrain class
game = QuizBrain(question_bank)
while game.still_has_questions():
    game.next_question()

# after finishing the game show the result
print("You have completed the quiz!")
print(f"Your score is {game.get_score()}/{game.get_question_number()}")
