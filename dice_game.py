# 12. 아래의 주사위 게임을 짜시오.
# 주사위 게임
# >>첫번째의 참가자의 이름을 입력하세요.
# 영희
# >>두번째의 참가자의 이름을 입력하세요.
# 철수
# 영희 주사위 숫자는 : 6
# 철수 주사위 숫자는 : 5
# 영희가 이겼습니다.

import random

class DiceGame:
    # def __init__(self):
    #     pass

    def input_players(self):
        try:
            self.player1 = input("첫번째 참가자의 이름을 입력하세요. ")
            self.player2 = input("두번째 참가자의 이름을 입력하세요. ")
            
            self.players = ([self.player1, 0], [self.player2, 0])
        except ValueError:
            print("잘못 입력했습니다. 다시 입력하세요.")
    
    def dice_result(self):
        for i in range(2):
            self.players[i][1] = random.randint(1,6)
        print(self.players)

        if self.players[0][1] > self.players[1][1]:
            print(self.players[0][0]+"가 이겼습니다.")
        elif self.players[1][1] > self.players[0][1]:
            print(self.ㅊplayers[1][0]+"가 이겼습니다.")
        else:
            print("비겼습니다.")


    def run(self):
        self.input_players()
        self.dice_result()
    
    
dice_game = DiceGame()
dice_game.run()
