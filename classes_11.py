class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'( '+self.meaning+' )'
flash = []
print("Welcome to the flashcard application!")
while (True):
    word = input("Enter a word: ")
    meaning = input("Enter the meaning: ")
    flash.append(flashcard(word, meaning))
    another_flashcard = int(input("Would you like to do another flashcard(0 to continue, 1 to stop): "))
    if another_flashcard == 1:
        break
    elif another_flashcard == 2:
        continue
print("\nYour Flashcards:")
for i in flash:
    print(">", i)
    
        