import random
import time

# three possible moves and their rules

moves = ['rock', 'paper', 'scissors']


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)

# remembers what move the opponent played last round,
# and plays that move this round
# always starts with rock as its favorite one ;)


class ReflectPlayer(Player):

    def __init__(self):
        self.pre_my_move = "rock"

    def move(self):
        return self.pre_my_move

    def learn(self, my_move, their_move):
        self.pre_my_move = their_move

# remembers what move it played last round,
# and cycles through the different moves
# always starts with paper as its favorite one ;)


class CyclePlayer(Player):

    def __init__(self):
        self.pre_my_move = "paper"

    def move(self):
        move_choise = moves.index(self.pre_my_move)
        if move_choise < len(moves):
            return moves[move_choise + 1]
        else:
            return moves[0]

    def learn(self, my_move, their_move):
        self.pre_my_move = my_move

# move chosen by human player


class Human(Player):
    def move(self):
        while True:
            my_move = input('Choose (r)ock, (p)aper or (s)cissors!\n')
            if my_move == 'r':
                return moves[0]
            elif my_move == 'p':
                return moves[1]
            elif my_move == 's':
                return moves[2]
            else:
                print("Sorry! I don't understand.\n")
                time.sleep(2)
                Human.move


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        # set every countabal score and round to zero
        # to keep track of the score

        self.human = 0
        self.opponent = 0
        self.tie = 0

        # and the rounds played

        self.rounds_to_play = 0
        self.exit = False

    # Game start welcome text to introduce the rules
    # than the user gets asked for the level
    # the hight of the level depends on the 'strategy'
    # of the opponent
    # opponent always playing 'rock' as the easiest level 1
    # and opponent playing randomly as the highest level 4

    def chose_level(self):
        print("\nWelcome to rock, paper or scissors!\n")
        time.sleep(1)
        print("Remember:")
        time.sleep(1)
        print("rock beats scissors,")
        time.sleep(1)
        print("scissors beat paper")
        time.sleep(1)
        print("and paper beats rock\n")
        time.sleep(1)

        # to keep it simple and avoid typing mistakes the input
        # asked for is a single number

        while True:
            level = (input(
                "Choose a level between 1 and 4.\n"
                "Or press x to quit the game.\n"))
            if level == "1":
                print("\nYou've chosen the easy track.\n")
                self.p2 = Player()
                time.sleep(1)
                break
            elif level == "2":
                print("\nSecond level! Go for it!\n")
                self.p2 = CyclePlayer()
                time.sleep(1)
                break
            elif level == "3":
                print("\nThird Level! Good luck!\n")
                self.p2 = ReflectPlayer()
                time.sleep(1)
                break
            elif level == "4":
                print("\nYou've chosen the highest level! "
                      "May the force be with you.\n")
                self.p2 = RandomPlayer()
                time.sleep(1)
                break
            elif level == "x":
                print("\nYou quit the game. See you again next time!\n")
                self.exit = True
                time.sleep(1)
                break
            else:
                print("\nSorry. Something went wrong. Try again.\n")

    # for more interactivity the player gets asked for the number of
    # rounds to play
    # to make it diverting its possible to choose to options:
    # a single battle or three rounds

    def game_type(self):
        if self.exit is True:
            print("Bye!")
            self.winner()
        else:

            while True:
                rounds = input(
                     "\nDo you want to fight a \'single battle\' (1) \n"
                     "or \'best out of three\' (2)?\n")
                if rounds == "1":
                    self.rounds_to_play = 1
                    print("\nGet ready for a single battle!\n")
                    time.sleep(1)
                    break
                elif rounds == "2":
                    print("\nGet ready for best out of three!\n")
                    self.rounds_to_play = 3
                    time.sleep(1)
                    break
                else:
                    print("\nSorry. Something went wrong. Try again.\n")
                time.sleep(1)

    # to announce a winner at the end of the game the score
    # gets counted
    # a a little re-registration the player get told who won
    # the round after every single round

    def count_score(self, my_move, their_move):

        # human wins
        if beats(my_move, their_move):
            self.human += 1
            print("yeah {0} beats {1}.\n".format(my_move, their_move))
            time.sleep(0.5)
        # opponent wins
        elif beats(their_move, my_move):
            self.opponent += 1
            print("Hmmmpf {0} beats {1}.\n".format(their_move, my_move))
            time.sleep(0.5)
        # tie
        else:
            self.tie += 1
            print("It's a tie!\n")
            time.sleep(0.5)

    # every round played the player sees which move he took
    # and which move the opponent made
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("You chose {0}. \nThe computer took {1}.".format(move1, move2))
        time.sleep(1)
        self.count_score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        time.sleep(1)

    # to play multiple rounds in a game the number of battles when you
    # play best out of three gets counted up
    def battle(self):
        for x in range(self.rounds_to_play):
            self.play_round()

    # If the game is done or the player exits the game
    # the player gets told who wins or told good bye.
    # after that the program exits

    def winner(self):
        if self.exit is True:
            print("\n")
        else:
            if self.human > self.opponent:
                print("You win with a score of " + str(self.human) + ":"
                      "" + str(self.opponent) + "!\n")
            elif self.human < self.opponent:
                print("The computer wins with a score of "
                      "" + str(self.opponent) + ":" + str(self.human) + "!\n")
            else:
                print("The game ends in a draw!\n")

    # following the logical structure of the
    # game the player gets guided
    # through the game

    def play_game(self):
        self.chose_level()
        self.game_type()
        self.battle()
        self.winner()


if __name__ == '__main__':
    game = Game(Human(), Player())
    game.play_game()
