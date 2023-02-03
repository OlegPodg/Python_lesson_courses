class AnonymousServey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):  # выводит опрос
        print(self.question)

    def store_response(self, new_response):  # сохраняет один ответ на опрос
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")
