import random


class WordleGame:

    # List of words to be randomly chosen by the program
    def __init__(self):
        self.words = [
            "apple", "brave", "chair", "dream", "eagle",
            "flame", "grape", "house", "index", "jelly",
            "knife", "lemon", "magic", "night", "ocean",
            "piano", "queen", "river", "smile", "tiger",
            "uncle", "vivid", "whale", "xenon", "youth",
            "zebra", "bread", "cloud", "frost", "giant"
        ]

        self.points = 0
        self.games_played = 0
        self.games_won = 0

    def print_header(self):
        print("\n" + "=" * 50)
        print("WORDLE")
        print("=" * 50)

        print("\nHow to play:")
        print("- Guess the hidden 5-letter word")
        print("- You have 5 attempts per round")
        print("- Feedback after each guess:")
        print("  🟩 correct letter, correct position")
        print("  🟨 correct letter, wrong position")
        print("  ⬜ letter not in the word")
        print("\nTry to guess the word before attempts run out.")
        print("=" * 50)

    def generate_feedback(self, guess, target):
        feedback = ""

        for i in range(5):
            if guess[i] == target[i]:
                feedback += "🟩"
            elif guess[i] in target:
                feedback += "🟨"
            else:
                feedback += "⬜"

        return feedback

    def play_round(self):

        target_word = random.choice(self.words)
        tries = 0
        guess_history = []

        self.games_played += 1

        while tries < 5:

            self.print_header()

            print("\nPrevious guesses:\n")

            for g, f in guess_history:      #g: guess   f: feedback
                print(f"{g.upper()}  {f}")

            print("\nAttempts remaining:", 5 - tries)

            guess = input("\nEnter a 5-letter word: ").lower()

            if len(guess) != 5:
                print("\nInvalid input. Must be 5 letters.")
                input("Press Enter to continue...")
                continue

            feedback = self.generate_feedback(guess, target_word)

            guess_history.append((guess, feedback))

            if guess == target_word:
                self.points += 10
                self.games_won += 1

                print("\nCorrect word!")
                print(f"You used {tries + 1} attempts.")
                print("Points earned: 10")

                input("\nPress Enter to continue...")
                return

            tries += 1

        print("\nGame Over")
        print("The word was:", target_word)

        input("\nPress Enter to continue...")

    def show_stats(self):

        print("\n" + "=" * 50)
        print("STATISTICS")
        print("=" * 50)

        print("Games Played:", self.games_played)
        print("Games Won:", self.games_won)
        print("Points:", self.points)

        if self.games_played > 0:
            win_rate = (self.games_won / self.games_played) * 100
            print(f"Win Rate: {win_rate:.1f}%") #.1f for 1 digit after decimal point

        print("=" * 50)

        input("\nPress Enter to continue...")

    def start_game(self):

        while True:

            self.play_round()
            self.show_stats()

            choice = input("\nPlay another round? (y/n): ").lower()

            if choice != "y":
                print("\nThanks for playing Wordle.")
                break


game = WordleGame()
game.start_game()