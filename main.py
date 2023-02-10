from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)  # Sets it up as an object with q_text and q_answer...
    # ...values like a dictionary. Can access via '.text' for the question or '.answer' for the answer...
    # ...(Done in QuizBrain).
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
