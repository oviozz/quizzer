
class Flashcards:
    track = 0
    def __init__(self, content, display, counter):
        self.questions = list(content.keys())
        self.answers = list(content.values())

        display.setText(self.questions[Flashcards.track])
        counter.setText(f'{Flashcards.track}/{len(self.questions) - 1}')


    def previous(self, count):
        Flashcards.track = Flashcards.track - 1
        if Flashcards.track <= 0:
            Flashcards.track = 0

        count.setText(f'{Flashcards.track}/{len(self.questions)-1}')
        return Flashcards.track


    def next(self, count):
        Flashcards.track = Flashcards.track + 1
        if Flashcards.track >= len(self.questions) - 1:
            Flashcards.track = len(self.questions) - 1

        count.setText(f'{Flashcards.track}/{len(self.questions) - 1}')
        return Flashcards.track

    def back_next(self, flashcard_text, action, counter):
        if action == 'back':
            self.previous(counter)
            flashcard_text.setText(self.questions[Flashcards.track])

        elif action == 'forward':
            self.next(counter)
            flashcard_text.setText(self.questions[Flashcards.track])

    def reveal_answer(self, flashcard_text):
        flashcard_text.setText(self.answers[Flashcards.track])

    def return_home(self, counter):
        Flashcards.track = 0
        counter.setText(f'{Flashcards.track}/{len(self.questions) - 1}')

