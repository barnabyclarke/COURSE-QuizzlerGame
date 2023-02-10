from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # Bring in QuizBrain as a variable of type (:)...
        # ...QuizBrain to give us access to its functions and data.
        self.quiz = quiz_brain
        # SET UP WHOLE POP UP #
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Sets white square background with its formatted text to not exceed its width
        self.canvas = Canvas(height=250, width=300, highlightthickness=0, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"),
                                                   fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)
        # Score Label
        self.score = Label(text="", bg=THEME_COLOR, fg="white", font=("Arial", 15, "normal"))
        self.score.grid(column=1, row=0)
        # Import button images
        tick = PhotoImage(file="images/true.png")
        cross = PhotoImage(file="images/false.png")
        # Set up buttons
        self.true_button = Button(image=tick, highlightthickness=0, command=self.true_press)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=cross, highlightthickness=0, command=self.false_press)
        self.false_button.grid(column=1, row=2)
        # Run method defined below
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # Return canvas to white
        if self.quiz.still_has_questions():  # Check if there are any questions remaining in list
            q_text = self.quiz.next_question()  # Sets up the question using QuizBrain function
            self.canvas.itemconfig(self.canvas_text, text=q_text)  # Sets question text in canvas every time it is run
            self.score.config(text=f"Score: {self.quiz.score}")  # Keeps score updated
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("true"))  # Uses check_answer from QuizBrain to give back boolean

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("false"))  # Uses check_answer from QuizBrain to give back boolean

    def give_feedback(self, answer: bool):
        if answer:  # If check True
            self.canvas.config(bg="green")  # Set canvas green for 1 second
        else:  # If check False
            self.canvas.config(bg="red")  # Set canvas red for 1 second
        self.window.after(1000, self.get_next_question)  # NO () AT END OR COLOUR DOESN'T CHANGE!!
