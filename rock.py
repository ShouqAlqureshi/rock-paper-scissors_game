
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock', 'paper', 'scissors']


class Player():
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        while True:
            move = input("Rock, paper, scissors?\t").lower()
            if move in moves:
                return move
            print(f"The move {move} is invalid. Try again!")


class Game():
    p1_points = 0
    p2_points = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round_counter = 0
        # I dicided to add is_a_win and learn to game class
        # since it belongs to the game rules not players

    def is_a_win(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def gudge(self, p1_move, p2_move):
        if p1_move == p2_move:
            print("** TIE **")
        elif self.is_a_win(p1_move, p2_move):
            print("** PLAYER ONE WINS **")
            self.p1_points += 1
        else:
            print("** PLAYER TWO WINS **")
            self.p2_points += 1

    def play_round(self):
        self.move1 = self.p1.move()
        self.move2 = self.p2.move()
        print(f"\nYou played:  {self.move1} \nOpponent played: {self.move2}\n")
        self.gudge(self.move1, self.move2)
        print(f"Round {self.round_counter} --"
              f"\n#=====================#")
        print(f"##  Current scores   ##"
              f"\n#=====================#"
              f"\n#=  Player One: {self.p1_points}    =#"
              f"\n#=====================#\n"
              f"#=  Player Two: {self.p2_points}    =#"
              f"\n#=====================#\n")
        self.p1.learn(self.move1, self.move2)
        self.p2.learn(self.move2, self.move1)

    def play_game(self):
        print("Rock Paper Scissors, Go!")
        while True:
            print(f"Round {self.round_counter} --")
            self.play_round()
            if self.round_counter >= 3:
                self.game_over()
                break
            self.round_counter += 1

    def game_over(self):
        print(f"\n#=====================#\n"
              f"##  General scores   ##"
              f"\n#=====================#")
        print(f"#=  Player 1: {self.p1_points}      =#")
        print(f"#=  Player 2: {self.p2_points}      =#"
              f"\n#=====================#\n")
        if self.p1_points > self.p2_points:
            print("** PLAYER ONE IS THE WINNER! **\n Game over!")
            exit()
        elif self.p2_points > self.p1_points:
            print("** PLAYER TWO IS THE WINNER! **\n Game over! ")
            exit()
        else:
            print("** IT'S A TIE! **\n Game over! ")
            exit()


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.b = "out"

    def move(self):
        if self.b == "in":
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.b = "in"


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.a = "out"

    def move(self):
        if self.my_move == "rock":
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


    def learn(self, my_move, their_move):
       self.my_move = my_move


class AllRockPlayer(Player):
    pass


if __name__ == '__main__':
    players = [
        AllRockPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
