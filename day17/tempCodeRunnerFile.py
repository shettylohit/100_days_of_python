from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)

quiz = Question(question_bank)
quiz.next_question()