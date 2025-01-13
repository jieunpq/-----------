# 8.가위 바위보 게임을 만드시오
# 예외처리 꼭 부탁드립니다.

import random

class RSPGame:
    def __init__(self):
        self.rsp = ['가위','바위','보']
        self.com_choice = ''
        self.player_choice = ''

    def player_rsp(self):
        while True:
            try:
                self.player_choice = input('가위 바위 보 중 하나를 입력하세요: ')
                if self.player_choice not in self.rsp:
                    raise ValueError("가위, 바위, 보 중 하나를 입력해야 합니다.")
                break
            except ValueError as e:
                print(e)

    def com_rsp(self):
        self.com_choice = random.choice(self.rsp)
        print("컴퓨터", self.com_choice)
        print("플레이어", self.player_choice)
    
    def decide_winner(self):
        winner = ""
        if self.player_choice == self.com_choice:
            print("무승부")
        else:
            if self.player_choice == '가위':
                if self.com_choice == '바위':
                    winner = "컴퓨터"
                else:
                    winner = "플레이어"

            if self.player_choice == '바위':
                if self.com_choice == '가위':
                    winner = "플레이어"
                else:
                    winner = "컴퓨터"

            if self.player_choice == '보':
                if self.com_choice == '바위':
                    winner = "플레이어"
                else:
                    winner = "컴퓨터"
                
            print(winner+"승리")            

    def run(self):

        while True:    
            self.player_rsp()
            self.com_rsp()
            self.decide_winner()
            
            continue_yn = input("계속하시겠습니까?(y/n) ")
            
            try:
                if continue_yn not in ['y', 'yes', 'n', 'no']:
                    raise ValueError("y 또는 n을 입력해야 합니다.")
                if continue_yn.lower() in ['n', 'no']:
                    break

            except ValueError:
                print("e")
        
        print("게임이 끝났습니다.")

game = RSPGame()
game.run()

# 가위 바위 보 게임
# 가위 바위 보를 하는 게임 입니다.

# 가위 바위 보 중 하나를 입력하세요: 가위
# 컴퓨터는 가위를 냈습니다.

# 플레이어는 가위를 냈습니다.
# 무승부

# 계속 하시겠습니까? no

# 게임이 끝났습니다.