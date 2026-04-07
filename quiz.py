class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(f"\n{self.question}\n")
        for i, choice in enumerate(self.choices, start=1):
            print(f" {i}. {choice}")
    
    def check(self, user_answer):
        return self.answer == user_answer