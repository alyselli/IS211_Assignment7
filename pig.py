
import random

random.seed(0)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points


class Die:
    def roll(self):
        return random.randint(1, 6)


class PigGame:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.die = Die()
        self.current_player = 0

    def play_turn(self):
        player = self.players[self.current_player]
        turn_total = 0

        print("\n" + player.name + "'s turn!")

        while True:
            print("\nTotal score:", player.score)
            print("Turn score:", turn_total)

            choice = input("Roll (r) or Hold (h)? ").lower().strip()

            if choice == "r":
                roll = self.die.roll()
                print("You rolled:", roll)

                if roll == 1:
                    print("You rolled a 1! No points this turn.")
                    turn_total = 0
                    break

                turn_total += roll
                print("Current turn score:", turn_total)

            elif choice == "h":
                player.add_points(turn_total)
                print(player.name, "now has", player.score, "points!")
                break

            else:
                print("Invalid choice. Enter r or h.")

        return player.score >= 100

    def play(self):
        print("Welcome to Pig!")
        print("First player to reach 100 points wins!")

        while True:
            game_over = self.play_turn()

            if game_over:
                winner = self.players[self.current_player]
                print("\nGame Over!")
                print(winner.name, "wins with", winner.score, "points!")
                break

            self.current_player = (self.current_player + 1) % 2


if __name__ == "__main__":
    game = PigGame()
    game.play()

