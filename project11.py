import re, random
from colorama import Fore, init
init(autoreset=True)
animal_class = {
    "reptiles": ["snakes", "crocodiles", "lizards", "frogs"],
    "mammals": ["koalas, hedgehogs, badgers, pandas"],
    "birds": ["hummingbirds", "robins", "parrots", "swan"],
    "sea creatures": ["dolphin", "seahorse", "shark", "turtle"]
}
places = { 
    "rainforests": ["Amazon", "Congo", "Indu-Burma"],
    "cities": ["Tokyo", "Paris", "Dubai"],
    "canyons": ["Grand", "Copper", "Waimea"]
}
jokes = [
    "How did the picture end up in prison? | It was framed.",
    "What did the cop say to his belly button? | You are under a vest.",
    "Why did the frog use the bus to get to work? | Because his car got toad.",
    "Why can't you give Elsa a balloon? | She will let it go.",
    "How did the barber cheat in the race? | He used a shortcut."
]
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
    print(Fore.CYAN + "ChatBot: Forests, canyons or cities?")
    choice = input(Fore.YELLOW + "You: ")
    choice = normalize_input(choice)
    if choice in places:
        idea = random.choice(places[choice])
        print(Fore.RED + f"ChatBot: How about {idea}?")
        print(Fore.GREEN + f"ChatBot: Do you like it? (yes or no)")
        answer = input(Fore.CYAN + "You: ").lower()
        if answer == "yes":
            print(Fore.GREEN + f"ChatBot: Awesome! Enjoy {idea}!")
        elif answer == "no":
            print(Fore.YELLOW + f"ChatBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "ChatBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "ChatBot: Sorry, I do not have that type of "
    "destination.")
        recommend()
def tell_joke():
    print(Fore.YELLOW + f"ChatBot: {random.choice(jokes)}")
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "ChatBot: Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")
if __name__ == "__main__":
    chat()



               






