#!/usr/bin/env python
from brain_games.logic import play_game
from brain_games.games import brain_calc


def main():
    Uniq_game_message = brain_calc.Uniq_game_message
    play_game(Uniq_game_message, brain_calc.question_for_user)


if __name__ == '__main__':
    main()
