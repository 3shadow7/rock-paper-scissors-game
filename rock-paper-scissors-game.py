import random 
import time
import os
import re

class game(object):
    def __init__(self) :
        self.purple_color="\033[0;35m"
        self.cyan_color="\033[0;36m"
        self.green_color="\033[0;32m"
        self.red_color="\033[0;31m"

        self.yourname = str(input("        [#] before we play , what is your name ! : ").upper())
        
        self.chose = ["rock","paper","scissors"] 
        self.rock = r"rock" # use it to find a same word to count it
        self.paper = r"paper" # use it to find a same word to count it
        self.scissors = r"scissors" # use it to find a same word to count it

        time = [0.1,0.2,0.3] 
        self.randomTIME = time[random.randint(0,2)] # to take a random time (0.1 - 0.2 - 0.3)

        ### to show a hero info one time in story mode (AND) do not show it in battle mode ###
        self.joker_info = False 
        self.zoro_info = False
        self.thanos_info = False
        self.shadow_info = False

        ### i use this inside each (def hero) to switch between story mode (AND) fighting mode ###
        self.joker_1v1 = False
        self.zoro_1v1 = False
        self.thanos_1v1 = False
        self.shadow_1v1 = False

        ### i use this to count points of player and heros ( IN FIGHT MODE ) ###
        self.player_point = 0
        self.joker_point = 0
        self.zoro_point = 0
        self.thanos_point = 0
        self.shadow_point = 0
        self.point_to_win = 3 # how many points do you need to win ( IN FIGHT MODE ) 

        self.start() # i put it here to work first auto 

    ### down below is : defs i creat as tool to use it later inside defs of heros ###

    # def to show logo of the game on screen
    def logo(self):
        print(f"{self.purple_color}-----------------------------------------------------")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.cyan_color}                {self.purple_color}|{self.cyan_color}     ..     .. {self.purple_color}| {self.cyan_color}  ..    ^    ..  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.cyan_color} .^..^..^..^.   {self.purple_color}|{self.cyan_color}     \ \   / / {self.purple_color}|{self.cyan_color}   \ \  | |  / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.cyan_color} : :  :  :  :\  {self.purple_color}|{self.cyan_color}      \ \ / /  {self.purple_color}|{self.cyan_color} .. \ \ | | / /   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.cyan_color} : :  :  :  : / {self.purple_color}|{self.cyan_color} .^..^.\ ' /.  {self.purple_color}|{self.cyan_color} \ \ \ \| |/ / .. {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.cyan_color} : :  :  : / /  {self.purple_color}|{self.cyan_color} : :  :      \ {self.purple_color}|{self.cyan_color}  \ \|      | / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.cyan_color}  ' '' '''..'   {self.purple_color}|{self.cyan_color} : :  :    / / {self.purple_color}|{self.cyan_color}   \        |/ /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.cyan_color}                {self.purple_color}|{self.cyan_color}  ' '' '''..'  {self.purple_color}|{self.cyan_color}    \_________/   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}-----------------------------------------------------")

    # defs to show logo when u take rock
    def rock_to_rock(self):

        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}                {self.purple_color}|{self.red_color}                {self.purple_color}")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} .^..^..^..^.   {self.purple_color}|{self.red_color} .^..^..^..^.   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :  :  :\  {self.purple_color}|{self.red_color} : :  :  :  :\  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :  :  : / {self.purple_color}|{self.red_color} : :  :  :  : / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :  : / /  {self.purple_color}|{self.red_color} : :  :  : / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}  ' '' '''..'   {self.purple_color}|{self.red_color}  ' '' '''..'   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}                {self.purple_color}|{self.red_color}                {self.purple_color}|")
        time.sleep(0.1)

    def rock_to_paper(self):
        
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}                {self.purple_color}|{self.red_color}   ..    ^    ..  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} .^..^..^..^.   {self.purple_color}|{self.red_color}   \ \  | |  / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :  :  :\  {self.purple_color}|{self.red_color} .. \ \ | | / /   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :  :  : / {self.purple_color}|{self.red_color} \ \ \ \| |/ / .. {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :  : / /  {self.purple_color}|{self.red_color}  \ \|      | / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}  ' '' '''..'   {self.purple_color}|{self.red_color}   \        |/ /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}                {self.purple_color}|{self.red_color}    \_________/   {self.purple_color}|")
        time.sleep(0.1)

    def rock_to_scissors(self):
        
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}                {self.purple_color}|{self.red_color}     ..     .. {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} .^..^..^..^.   {self.purple_color}|{self.red_color}     \ \   / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :  :  :\  {self.purple_color}|{self.red_color}      \ \ / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :  :  : / {self.purple_color}|{self.red_color} .^..^.\ ' /.  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :  : / /  {self.purple_color}|{self.red_color} : :  :      \ {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}  ' '' '''..'   {self.purple_color}|{self.red_color} : :  :    / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}                {self.purple_color}|{self.red_color}  ' '' '''..'  {self.purple_color}|")
        time.sleep(0.1)


    # defs to show logo when u take paper
    def paper_to_rock(self):
        
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}   ..    ^    ..  {self.purple_color}|{self.red_color}                {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}   \ \  | |  / /  {self.purple_color}|{self.red_color} .^..^..^..^.   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} .. \ \ | | / /   {self.purple_color}|{self.red_color} : :  :  :  :\  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} \ \ \ \| |/ / .. {self.purple_color}|{self.red_color} : :  :  :  : / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}  \ \|      | / / {self.purple_color}|{self.red_color} : :  :  : / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}   \        |/ /  {self.purple_color}|{self.red_color}  ' '' '''..'   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}    \_________/   {self.purple_color}|{self.red_color}                {self.purple_color}|")
        time.sleep(0.1)

    def paper_to_paper(self):
        
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}   ..    ^    ..  {self.purple_color}|{self.red_color}   ..    ^    ..  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}   \ \  | |  / /  {self.purple_color}|{self.red_color}   \ \  | |  / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} .. \ \ | | / /   {self.purple_color}|{self.red_color} .. \ \ | | / /   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} \ \ \ \| |/ / .. {self.purple_color}|{self.red_color} \ \ \ \| |/ / .. {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}  \ \|      | / / {self.purple_color}|{self.red_color}  \ \|      | / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}   \        |/ /  {self.purple_color}|{self.red_color}   \        |/ /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}    \_________/   {self.purple_color}|{self.red_color}    \_________/   {self.purple_color}|")
        time.sleep(0.1)

    def paper_to_scissors(self):
        
        time.sleep(0.1)
        print(f"{self.purple_color}| {self.green_color}  ..    ^    ..  {self.purple_color}|{self.red_color}     ..     .. {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}   \ \  | |  / /  {self.purple_color}|{self.red_color}     \ \   / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} .. \ \ | | / /   {self.purple_color}|{self.red_color}      \ \ / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} \ \ \ \| |/ / .. {self.purple_color}|{self.red_color} .^..^.\ ' /.  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}  \ \|      | / / {self.purple_color}|{self.red_color} : :  :      \ {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}   \        |/ /  {self.purple_color}|{self.red_color} : :  :    / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}    \_________/   {self.purple_color}|{self.red_color}  ' '' '''..'  {self.purple_color}|")
        time.sleep(0.1)


    # defs to show logo when u take scissors
    def scissors_to_rock(self):
        
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}     ..     .. {self.purple_color}|{self.red_color}                {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}     \ \   / / {self.purple_color}|{self.red_color} .^..^..^..^.   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}      \ \ / /  {self.purple_color}|{self.red_color} : :  :  :  :\  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} .^..^.\ ' /.  {self.purple_color}|{self.red_color} : :  :  :  : / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :      \ {self.purple_color}|{self.red_color} : :  :  : / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :    / / {self.purple_color}|{self.red_color}  ' '' '''..'   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}  ' '' '''..'  {self.purple_color}|{self.red_color}                {self.purple_color}|")
        time.sleep(0.1)

    def scissors_to_paper(self):
        
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}     ..     .. {self.purple_color}|{self.red_color}   ..    ^    ..  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}     \ \   / / {self.purple_color}|{self.red_color}   \ \  | |  / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}      \ \ / /  {self.purple_color}|{self.red_color} .. \ \ | | / /   {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} .^..^.\ ' /.  {self.purple_color}|{self.red_color} \ \ \ \| |/ / .. {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :      \ {self.purple_color}|{self.red_color}  \ \|      | / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :    / / {self.purple_color}|{self.red_color}   \        |/ /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}  ' '' '''..'  {self.purple_color}|{self.red_color}    \_________/   {self.purple_color}|")
        time.sleep(0.1)

    def scissors_to_scissors(self):
        
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}     ..     .. {self.purple_color}|{self.red_color}     ..     .. {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}     \ \   / / {self.purple_color}|{self.red_color}     \ \   / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}      \ \ / /  {self.purple_color}|{self.red_color}      \ \ / /  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} .^..^.\ ' /.  {self.purple_color}|{self.red_color} .^..^.\ ' /.  {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :      \ {self.purple_color}|{self.red_color} : :  :      \ {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color} : :  :    / / {self.purple_color}|{self.red_color} : :  :    / / {self.purple_color}|")
        time.sleep(0.1)
        print(f"{self.purple_color}|{self.green_color}  ' '' '''..'  {self.purple_color}|{self.red_color}  ' '' '''..'  {self.purple_color}|")
        time.sleep(0.1)

    ### def to show you home page ###

    def start(self): 
        self.refreash() 
        os.system("clear")
        print(f'\n\n{self.purple_color}    welcome {self.green_color}{self.yourname} {self.purple_color}to ( ROCK,PAPER,SCISSORS ) GAME  \n\n')
        time.sleep(3)
        self.logo()
        time.sleep(2)
        print(f"{self.purple_color}        [{self.cyan_color}+{self.purple_color}] chose what you need to play :")
        print(f"{self.purple_color}        [{self.cyan_color}1{self.purple_color}] story game")
        print(f"{self.purple_color}        [{self.cyan_color}2{self.purple_color}] fight (one VS one) hero")
        print(f"{self.purple_color}        [{self.cyan_color}3{self.purple_color}] info\n")
        game_ask_u = str(input(f"        [{self.cyan_color}#{self.purple_color}] hmmm , i will take number :{self.green_color} "))
        if game_ask_u == "1" :
            self.story()
        if game_ask_u == "2" :
            self.all_heros()
        if game_ask_u == "3" :
            self.info()
        if (game_ask_u != "1") and (game_ask_u != "2") and (game_ask_u != "3") :
            os.system("clear")
            input(f"\n {self.red_color}       wrong input .. \n\n\n\n      {self.purple_color}  ")
            self.start()

    # when you take namber 1 from home page
    def story (self):
        self.refreash()
        os.system("clear")
        print(f"\n\n {self.purple_color}       [{self.green_color}1{self.purple_color}] the first hero is : \n")
        self.JOKER()

    ### all heros in this GAME down below ### 

    # def for joker hero 
    def JOKER(self):

        if self.joker_info == False :
            self.joker_info = True
            joker_hero = input(f'{self.purple_color}        [{self.cyan_color} JOKER {self.purple_color}] , all players say he is esay hero\n        but do not listen to them , joker has an unpredictable movement .. \n\n        {self.purple_color}[{self.cyan_color}#{self.purple_color}] press any kay ')

        if (self.joker_point == 3) or (self.player_point == 3) :
            os.system("clear")
            print(f"\n\n{self.red_color}        (( {self.cyan_color}game over{self.red_color} )) {self.purple_color}\n\n")
            if (self.joker_point == 3) :
                print("        the winer is JOKER")
                time.sleep(1)
                input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                self.start()
            if (self.player_point == 3) :
                print(f"        the winer is {self.yourname}")
                time.sleep(1)
                input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                self.start()





        time.sleep(1)
        os.system('clear')
        print(f'\n\n\n {self.red_color}               (({self.cyan_color} battle will start in{self.red_color} ))')
        time.sleep(2)
        print(f'{self.cyan_color}                             3')
        time.sleep(self.randomTIME)
        print(f'{self.cyan_color}                             2')
        time.sleep(self.randomTIME)
        print(f'{self.cyan_color}                             1')
        time.sleep(self.randomTIME)
        print(f'{self.red_color}                         fight !!\n\n\n')
        time.sleep(1)
        your_input = input(f'{self.purple_color}        [{self.cyan_color}+{self.purple_color}] what do you chose :\n {self.purple_color}       [{self.cyan_color}1{self.purple_color}] ROCK\n        [{self.cyan_color}2{self.purple_color}] PAPER\n        [{self.cyan_color}3{self.purple_color}] SCISSORS\n\n        [{self.cyan_color}#{self.purple_color}] i will shose {self.cyan_color}--> {self.green_color}')
        os.system("clear")

        if (your_input == "1") or (your_input == "ROCK") or (your_input =="rock") :
            
            joker_chose = random.randint(0,1000)
            if joker_chose <= 300 :
                self.joker = self.chose[0]

            if (joker_chose >= 300) and (joker_chose <= 400) :
                self.joker = self.chose[1]

            if joker_chose >= 400 :
                self.joker = self.chose[2]

            
            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[0]+f'{self.purple_color} and {self.red_color}JOKER{self.purple_color} take '+self.joker+"\n"
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_rock) <= 1 :
                try:
                    if (how_mach_rock[0] == "rock") and (how_mach_scissors[0] == "scissors") :
                        self.rock_to_scissors()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")
                        if self.joker_1v1 == False :
                            time.sleep(2)
                            input(f"\n\n{self.purple_color}        time to hit next hero\n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            os.system("clear")
                            print(f"\n\n {self.purple_color}       [{self.green_color}2{self.purple_color}] the second hero is : \n")
                            self.refreash()
                            self.ZORO()

                        if self.joker_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  JOKER : {self.joker_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.JOKER()

                except:
                    pass
                try:
                    if (how_mach_rock[0] == "rock") and (how_mach_paper[0] == "paper") :
                        self.rock_to_paper()
                        if self.joker_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops , u loss ..\n\n\n{self.purple_color}        if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.JOKER()
                        
                        if self.joker_1v1 == True :
                            self.joker_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  JOKER : {self.joker_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.JOKER() 
                except:
                    pass
            else:
                if self.joker_1v1 == False :
                    self.rock_to_rock()
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.JOKER()

                if self.joker_1v1 == True :
                    self.rock_to_rock()
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  JOKER : {self.joker_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.JOKER()



        if (your_input == "2") or (your_input == "PAPER") or (your_input =="paper") :
            
            joker_chose = random.randint(0,1000)
            if joker_chose <= 300 :
                self.joker = self.chose[1]

            if (joker_chose >= 300) and (joker_chose <= 400) :
                self.joker = self.chose[2]

            if joker_chose >= 400 :
                self.joker = self.chose[0]

            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[1]+f'{self.purple_color} and {self.red_color}JOKER{self.purple_color} take '+self.joker+"\n"
            
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_paper) <= 1 :
                try:
                    if (how_mach_paper[0] == "paper") and (how_mach_rock[0] == "rock") :
                        self.paper_to_rock()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")
                        if self.joker_1v1 == False :
                            time.sleep(2)
                            input(f"\n\n{self.purple_color}        time to hit next hero\n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            os.system("clear")
                            print(f"\n\n {self.purple_color}       [{self.green_color}2{self.purple_color}] the second hero is : \n")
                            self.refreash()
                            self.ZORO()

                        if self.joker_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  JOKER : {self.joker_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.JOKER()
                except:
                    pass

                try:
                    if (how_mach_paper[0] == "paper") and (how_mach_scissors[0] == "scissors") :
                        self.paper_to_scissors()
                        if self.joker_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n{self.purple_color}        if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.JOKER()
                        
                        if self.joker_1v1 == True :
                            self.joker_point +=  1
                            print(f"\n\n{self.green_color}        Ops . u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  JOKER : {self.joker_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.JOKER()              
                except:
                    pass
            else:
                self.paper_to_paper()
                if self.joker_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.JOKER()

                if self.joker_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  JOKER : {self.joker_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.JOKER()

        if (your_input == "3") or (your_input == "SCISSORS") or (your_input =="scissors") :
            
            joker_chose = random.randint(0,1000)
            if joker_chose <= 300 :
                self.joker = self.chose[2]

            if (joker_chose >= 300) and (joker_chose <= 400) :
                self.joker = self.chose[0]

            if joker_chose >= 400 :
                self.joker = self.chose[1]

            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[2]+f'{self.purple_color} and {self.red_color}JOKER{self.purple_color} take '+self.joker+"\n"
            
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_scissors) <= 1 :
                try:
                    if (how_mach_scissors[0] == "scissors") and (how_mach_rock[0] == "rock") :
                        self.scissors_to_rock()
                        if self.joker_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n{self.purple_color}        if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.JOKER()
                        
                        if self.joker_1v1 == True :
                            self.joker_point +=  1
                            print(f"\n\n{self.green_color}        Ops . u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  JOKER : {self.joker_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.JOKER()                      
                except:
                    pass
                
                try:
                    if (how_mach_scissors[0] == "scissors") and (how_mach_paper[0] == "paper") :
                        self.scissors_to_paper()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")                        
                        if self.joker_1v1 == False :
                            time.sleep(2)
                            input(f"\n\n{self.purple_color}        time to hit next hero\n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            os.system("clear")
                            print(f"\n\n {self.purple_color}       [{self.green_color}2{self.purple_color}] the second hero is : \n")
                            self.refreash()
                            self.ZORO()

                        if self.joker_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  JOKER : {self.joker_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.JOKER()
                except:
                    pass
            else:
                self.scissors_to_scissors()
                if self.joker_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.JOKER()

                if self.joker_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  JOKER : {self.joker_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.JOKER() 

        if ((your_input != "1") or (your_input != "ROCK") or (your_input !="rock")) and ((your_input != "2") or (your_input != "PAPER") or (your_input !="paper")) and ((your_input != "3") or (your_input != "SCISSORS") or (your_input !="scissors")) : 
            input(f"\n {self.red_color}       wrong input .. \n\n\n\n      {self.purple_color}  ")
            self.JOKER()


    # def for zoro hero
    def ZORO(self):
        
        if self.zoro_info == False :
            self.zoro_info = True
            zoro_hero = input(f'{self.purple_color}        [{self.cyan_color} ZORO {self.purple_color}] , everyone says he is lazy hero\n        but in fact , zoro has akeen eye for your nervousness .. \n\n        {self.purple_color}[{self.cyan_color}#{self.purple_color}] press any kay ')

        if (self.zoro_point == 3) or (self.player_point == 3) :
            os.system("clear")
            print(f"\n\n{self.red_color}        (( {self.cyan_color}game over{self.red_color} )) {self.purple_color}\n\n")
            if (self.zoro_point == 3) :
                print("        the winer is ZORO")
                time.sleep(1)
                input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                self.start()
            if (self.player_point == 3) :
                print(f"        the winer is {self.yourname}")
                time.sleep(1)
                input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                self.start()





        time.sleep(1)
        os.system('clear')
        print(f'\n\n\n {self.red_color}               (({self.cyan_color} battle will start in{self.red_color} ))')
        time.sleep(2)
        print(f'{self.cyan_color}                             3')
        time.sleep(self.randomTIME)
        print(f'{self.cyan_color}                             2')
        time.sleep(self.randomTIME)
        print(f'{self.cyan_color}                             1')
        time.sleep(self.randomTIME)
        print(f'{self.red_color}                         fight !!\n\n\n')
        time.sleep(1)
        your_input = input(f'{self.purple_color}        [{self.cyan_color}+{self.purple_color}] what do you chose :\n {self.purple_color}       [{self.cyan_color}1{self.purple_color}] ROCK\n        [{self.cyan_color}2{self.purple_color}] PAPER\n        [{self.cyan_color}3{self.purple_color}] SCISSORS\n\n        [{self.cyan_color}#{self.purple_color}] i will shose {self.cyan_color}--> {self.green_color}')
        os.system("clear")

        if (your_input == "1") or (your_input == "ROCK") or (your_input =="rock") :
            
            zoro_chose = random.randint(0,1000)
            if zoro_chose <= 300 :
                self.zoro = self.chose[0]

            if (zoro_chose >= 300) and (zoro_chose <= 600) :
                self.zoro = self.chose[1]

            if zoro_chose >= 600 :
                self.zoro = self.chose[2]

            
            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[0]+f'{self.purple_color} and {self.red_color}ZORO{self.purple_color} take '+self.zoro+"\n"
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_rock) <= 1 :
                try:
                    if (how_mach_rock[0] == "rock") and (how_mach_scissors[0] == "scissors") :
                        self.rock_to_scissors()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")   
                        if self.zoro_1v1 == False :                     
                            time.sleep(2)
                            input(f"\n\n{self.purple_color}        time to hit next hero\n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            os.system("clear")
                            print(f"\n\n {self.purple_color}       [{self.green_color}3{self.purple_color}] the third hero is : \n")
                            self.thanos_info = False
                            self.THANOS()

                        if self.zoro_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  ZORO : {self.zoro_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.ZORO()

                except:
                    pass
                try:
                    if (how_mach_rock[0] == "rock") and (how_mach_paper[0] == "paper") :
                        self.rock_to_paper()
                        if self.zoro_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n {self.purple_color}       if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.ZORO()
                        
                        if self.zoro_1v1 == True :
                            self.zoro_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  ZORO : {self.zoro_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.ZORO()   

                except:
                    pass
            else:
                self.rock_to_rock()
                if self.zoro_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.ZORO()

                if self.zoro_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  ZORO : {self.zoro_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.ZORO()


                



        if (your_input == "2") or (your_input == "PAPER") or (your_input =="paper") :
            
            zoro_chose = random.randint(0,1000)
            if zoro_chose <= 300 :
                self.zoro = self.chose[1]

            if (zoro_chose >= 300) and (zoro_chose <= 600) :
                self.zoro = self.chose[2]

            if zoro_chose >= 600 :
                self.zoro = self.chose[0]

            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[1]+f'{self.purple_color} and {self.red_color}ZORO{self.purple_color} take '+self.zoro+"\n"
            
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_paper) <= 1 :
                try:
                    if (how_mach_paper[0] == "paper") and (how_mach_rock[0] == "rock") :
                        self.paper_to_rock()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")                                          
                        if self.zoro_1v1 == False :                     
                            time.sleep(2)
                            input(f"\n\n{self.purple_color}        time to hit next hero\n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            os.system("clear")
                            print(f"\n\n {self.purple_color}       [{self.green_color}3{self.purple_color}] the third hero is : \n")
                            self.thanos_info = False
                            self.THANOS()

                        if self.zoro_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  ZORO : {self.zoro_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.ZORO()

                        
                except:
                    pass

                try:
                    if (how_mach_paper[0] == "paper") and (how_mach_scissors[0] == "scissors") :
                        self.paper_to_scissors()
                        if self.zoro_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n {self.purple_color}       if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.ZORO()
                        
                        if self.zoro_1v1 == True :
                            self.zoro_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  ZORO : {self.zoro_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.ZORO()   

                except:
                    pass
            else:
                self.paper_to_paper()
                if self.zoro_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.ZORO()

                if self.zoro_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  ZORO : {self.zoro_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.ZORO()


        if (your_input == "3") or (your_input == "SCISSORS") or (your_input =="scissors") :
            
            zoro_chose = random.randint(0,1000)
            if zoro_chose <= 300 :
                self.zoro = self.chose[2]

            if (zoro_chose >= 300) and (zoro_chose <= 600) :
                self.zoro = self.chose[0]

            if zoro_chose >= 600 :
                self.zoro = self.chose[1]

            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[2]+f'{self.purple_color} and {self.red_color}ZORO{self.purple_color} take '+self.zoro+"\n"
            
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_scissors) <= 1 :
                try:
                    if (how_mach_scissors[0] == "scissors") and (how_mach_rock[0] == "rock") :
                        self.scissors_to_rock()
                        if self.zoro_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n {self.purple_color}       if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.ZORO()
                        
                        if self.zoro_1v1 == True :
                            self.zoro_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  ZORO : {self.zoro_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.ZORO()   

                except:
                    pass
                
                try:
                    if (how_mach_scissors[0] == "scissors") and (how_mach_paper[0] == "paper") :
                        self.scissors_to_paper()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")                                          
                        if self.zoro_1v1 == False :                     
                            time.sleep(2)
                            input(f"\n\n{self.purple_color}        time to hit next hero\n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            os.system("clear")
                            print(f"\n\n {self.purple_color}       [{self.green_color}3{self.purple_color}] the third hero is : \n")
                            self.thanos_info = False
                            self.THANOS()

                        if self.zoro_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  ZORO : {self.zoro_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.ZORO()

                except:
                    pass
            else:
                self.scissors_to_scissors()
                if self.zoro_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.ZORO()

                if self.zoro_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  ZORO : {self.zoro_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.ZORO()


        if ((your_input != "1") or (your_input != "ROCK") or (your_input !="rock")) and ((your_input != "2") or (your_input != "PAPER") or (your_input !="paper")) and ((your_input != "3") or (your_input != "SCISSORS") or (your_input !="scissors")) : 
            input(f"\n {self.red_color}       wrong input .. \n\n\n\n      {self.purple_color}  ")
            self.ZORO()


    # def for thanos hero
    def THANOS(self):
        
        if self.thanos_info == False :
            self.thanos_info = True
            thanos_hero = input(f'{self.purple_color}        [{self.cyan_color} THANOS {self.purple_color}] everyone is afraid of his fight ,\n        thanos has a glove with the powers of the entire universe .. \n\n        {self.purple_color}[{self.cyan_color}#{self.purple_color}] press any kay ')

        if (self.thanos_point == 3) or (self.player_point == 3) :
            os.system("clear")
            print(f"\n\n{self.red_color}        (( {self.cyan_color}game over{self.red_color} )) {self.purple_color}\n\n")
            if (self.thanos_point == 3) :
                print("        the winer is THANOS")
                time.sleep(1)
                input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                self.start()
            if (self.player_point == 3) :
                print(f"        the winer is {self.yourname}")
                time.sleep(1)
                input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                self.start()





        time.sleep(1)
        os.system('clear')
        print(f'\n\n\n {self.red_color}               (({self.cyan_color} battle will start in{self.red_color} ))')
        time.sleep(2)
        print(f'{self.cyan_color}                             3')
        time.sleep(self.randomTIME)
        print(f'{self.cyan_color}                             2')
        time.sleep(self.randomTIME)
        print(f'{self.cyan_color}                             1')
        time.sleep(self.randomTIME)
        print(f'{self.red_color}                         fight !!\n\n\n')
        time.sleep(1)
        your_input = input(f'{self.purple_color}        [{self.cyan_color}+{self.purple_color}] what do you chose :\n {self.purple_color}       [{self.cyan_color}1{self.purple_color}] ROCK\n        [{self.cyan_color}2{self.purple_color}] PAPER\n        [{self.cyan_color}3{self.purple_color}] SCISSORS\n\n        [{self.cyan_color}#{self.purple_color}] i will shose {self.cyan_color}--> {self.green_color}')
        os.system("clear")

        if (your_input == "1") or (your_input == "ROCK") or (your_input =="rock") :
            
            thanos_chose = random.randint(0,1000)
            if thanos_chose <= 300 :
                self.thanos = self.chose[0]

            if (thanos_chose >= 300) and (thanos_chose <= 800) :
                self.thanos = self.chose[1]

            if thanos_chose >= 800 :
                self.thanos = self.chose[2]

            
            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[0]+f'{self.purple_color} and {self.red_color}THANOS{self.purple_color} take '+self.thanos+"\n"
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_rock) <= 1 :
                try:
                    if (how_mach_rock[0] == "rock") and (how_mach_scissors[0] == "scissors") :
                        self.rock_to_scissors()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")   
                        if self.thanos_1v1 == False :                                       
                            time.sleep(2)
                            input(f"\n\n{self.purple_color}        time to hit next hero\n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            os.system("clear")
                            print(f"\n\n {self.purple_color}       [{self.green_color}4{self.purple_color}] the fourth hero is : \n")
                            self.shadow_info = False
                            self.SHADOW()

                        if self.thanos_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  THANOS : {self.thanos_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.THANOS()

                except:
                    pass
                try:
                    if (how_mach_rock[0] == "rock") and (how_mach_paper[0] == "paper") :
                        self.rock_to_paper()
                        if self.thanos_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n{self.purple_color}        if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.THANOS()

                        if self.thanos_1v1 == True :
                            self.thanos_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  THANOS : {self.thanos_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.THANOS()   
                        
                except:
                    pass
            else:
                self.rock_to_rock()
                if self.thanos_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.THANOS()

                if self.thanos_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  THANOS : {self.thanos_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.THANOS()



        if (your_input == "2") or (your_input == "PAPER") or (your_input =="paper") :
            
            thanos_chose = random.randint(0,1000)
            if thanos_chose <= 300 :
                self.thanos = self.chose[1]

            if (thanos_chose >= 300) and (thanos_chose <= 800) :
                self.thanos = self.chose[2]

            if thanos_chose >= 800 :
                self.thanos = self.chose[0]

            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[1]+f'{self.purple_color} and {self.red_color}THANOS{self.purple_color} take '+self.thanos+"\n"
            
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_paper) <= 1 :
                try:
                    if (how_mach_paper[0] == "paper") and (how_mach_rock[0] == "rock") :
                        self.paper_to_rock()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")                                                              
                        if self.thanos_1v1 == False :                                       
                            time.sleep(2)
                            input(f"\n\n{self.purple_color}        time to hit next hero\n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            os.system("clear")
                            print(f"\n\n {self.purple_color}       [{self.green_color}4{self.purple_color}] the fourth hero is : \n")
                            self.shadow_info = False
                            self.SHADOW()

                        if self.thanos_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  THANOS : {self.thanos_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.THANOS()

                except:
                    pass

                try:
                    if (how_mach_paper[0] == "paper") and (how_mach_scissors[0] == "scissors") :
                        self.paper_to_scissors()
                        if self.thanos_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n{self.purple_color}        if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.THANOS()

                        if self.thanos_1v1 == True :
                            self.thanos_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  THANOS : {self.thanos_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.THANOS()   
            
                except:
                    pass
            else:
                self.paper_to_paper()
                if self.thanos_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.THANOS()

                if self.thanos_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  THANOS : {self.thanos_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.THANOS()



        if (your_input == "3") or (your_input == "SCISSORS") or (your_input =="scissors") :
            
            thanos_chose = random.randint(0,1000)
            if thanos_chose <= 300 :
                self.thanos = self.chose[2]

            if (thanos_chose >= 300) and (thanos_chose <= 800) :
                self.thanos = self.chose[0]

            if thanos_chose >= 800 :
                self.thanos = self.chose[1]

            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[2]+f'{self.purple_color} and {self.red_color}THANOS{self.purple_color} take '+self.thanos+"\n"
            
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_scissors) <= 1 :
                try:
                    if (how_mach_scissors[0] == "scissors") and (how_mach_rock[0] == "rock") :
                        self.scissors_to_rock()
                        if self.thanos_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n{self.purple_color}        if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.THANOS()

                        if self.thanos_1v1 == True :
                            self.thanos_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  THANOS : {self.thanos_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.THANOS()   
                
                except:
                    pass
                
                try:
                    if (how_mach_scissors[0] == "scissors") and (how_mach_paper[0] == "paper") :
                        self.scissors_to_paper()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")                                                              
                        if self.thanos_1v1 == False :                                       
                            time.sleep(2)
                            input(f"\n\n{self.purple_color}        time to hit next hero\n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            os.system("clear")
                            print(f"\n\n {self.purple_color}       [{self.green_color}4{self.purple_color}] the fourth hero is : \n")
                            self.shadow_info = False
                            self.SHADOW()

                        if self.thanos_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  THANOS : {self.thanos_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.THANOS()

                except:
                    pass
            else:
                self.scissors_to_scissors()
                if self.thanos_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.THANOS()

                if self.thanos_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  THANOS : {self.thanos_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.THANOS()



        if ((your_input != "1") or (your_input != "ROCK") or (your_input !="rock")) and ((your_input != "2") or (your_input != "PAPER") or (your_input !="paper")) and ((your_input != "3") or (your_input != "SCISSORS") or (your_input !="scissors")) : 
            input(f"\n {self.red_color}       wrong input .. \n\n\n\n      {self.purple_color}  ")
            self.THANOS()


    # def for shadow hero
    def SHADOW(self):
        
        if self.shadow_info == False :
            self.shadow_info = True
            shadow_hero = input(f'{self.purple_color}        [{self.cyan_color} SHADOW {self.purple_color}] known as the creator of this game ,\n        shadow os very difficult , and your win rate is about 3% , be careful .. \n\n        {self.purple_color}[{self.cyan_color}#{self.purple_color}] press any kay ')

        if (self.shadow_point == 3) or (self.player_point == 3) :
            os.system("clear")
            print(f"\n\n{self.red_color}        (( {self.cyan_color}game over{self.red_color} )) {self.purple_color}\n\n")
            if (self.shadow_point == 3) :
                print("        the winer is SHADOW")
                time.sleep(1)
                input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                self.start()
            if (self.player_point == 3) :
                print(f"        the winer is {self.yourname}")
                time.sleep(1)
                input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                self.start()





        time.sleep(1)
        os.system('clear')
        print(f'\n\n\n {self.red_color}               (({self.cyan_color} battle will start in{self.red_color} ))')
        time.sleep(2)
        print(f'{self.cyan_color}                             3')
        time.sleep(self.randomTIME)
        print(f'{self.cyan_color}                             2')
        time.sleep(self.randomTIME)
        print(f'{self.cyan_color}                             1')
        time.sleep(self.randomTIME)
        print(f'{self.red_color}                         fight !!\n\n\n')
        time.sleep(1)
        your_input = input(f'{self.purple_color}        [{self.cyan_color}+{self.purple_color}] what do you chose :\n {self.purple_color}       [{self.cyan_color}1{self.purple_color}] ROCK\n        [{self.cyan_color}2{self.purple_color}] PAPER\n        [{self.cyan_color}3{self.purple_color}] SCISSORS\n\n        [{self.cyan_color}#{self.purple_color}] i will shose {self.cyan_color}--> {self.green_color}')
        os.system("clear")

        if (your_input == "1") or (your_input == "ROCK") or (your_input =="rock") :
            
            shadow_chose = random.randint(0,1000)
            if shadow_chose <= 450 :
                self.shadow = self.chose[0]

            if (shadow_chose >= 450) and (shadow_chose <= 970) :
                self.shadow = self.chose[1]

            if shadow_chose >= 970 :
                self.shadow = self.chose[2]

            
            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[0]+f'{self.purple_color} and {self.red_color}SHADOW{self.purple_color} take '+self.shadow+"\n"
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_rock) <= 1 :
                try:
                    if (how_mach_rock[0] == "rock") and (how_mach_scissors[0] == "scissors") :
                        self.rock_to_scissors()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")   
                        if self.shadow_1v1 == False :                                        
                            time.sleep(1)
                            self.win_massage()

                        if self.shadow_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  SHADOW : {self.shadow_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.SHADOW()

                except:
                    pass
                try:
                    if (how_mach_rock[0] == "rock") and (how_mach_paper[0] == "paper") :
                        self.rock_to_paper()
                        if self.shadow_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n{self.purple_color}        if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.SHADOW()

                        if self.shadow_1v1 == True :
                            self.shadow_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  SHADOW : {self.shadow_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.SHADOW()   
                        
                except:
                    pass
            else:
                self.rock_to_rock()
                if self.shadow_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.SHADOW()

                if self.shadow_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  SHADOW : {self.shadow_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.SHADOW()



        if (your_input == "2") or (your_input == "PAPER") or (your_input =="paper") :
            
            thanos_chose = random.randint(0,1000)
            if thanos_chose <= 450 :
                self.thanos = self.chose[1]

            if (thanos_chose >= 450) and (thanos_chose <= 970) :
                self.thanos = self.chose[2]

            if thanos_chose >= 970 :
                self.thanos = self.chose[0]

            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[1]+f'{self.purple_color} and {self.red_color}SHADOW{self.purple_color} take '+self.thanos+"\n"
            
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_paper) <= 1 :
                try:
                    if (how_mach_paper[0] == "paper") and (how_mach_rock[0] == "rock") :
                        self.paper_to_rock()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")                                                              
                        if self.shadow_1v1 == False :                                        
                            time.sleep(1)
                            self.win_massage()

                        if self.shadow_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  SHADOW : {self.shadow_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.SHADOW()

                except:
                    pass

                try:
                    if (how_mach_paper[0] == "paper") and (how_mach_scissors[0] == "scissors") :
                        self.paper_to_scissors()
                        if self.shadow_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n{self.purple_color}        if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.SHADOW()

                        if self.shadow_1v1 == True :
                            self.shadow_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  SHADOW : {self.shadow_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.SHADOW()   

                except:
                    pass
            else:
                self.paper_to_paper()
                if self.shadow_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.SHADOW()

                if self.shadow_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  SHADOW : {self.shadow_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.SHADOW()


        if (your_input == "3") or (your_input == "SCISSORS") or (your_input =="scissors") :
            
            thanos_chose = random.randint(0,1000)
            if thanos_chose <= 450 :
                self.thanos = self.chose[2]

            if (thanos_chose >= 450) and (thanos_chose <= 970) :
                self.thanos = self.chose[0]

            if thanos_chose >= 970 :
                self.thanos = self.chose[1]

            score = f'\n\n  {self.green_color}  {self.yourname} {self.purple_color}take '+self.chose[2]+f'{self.purple_color} and {self.red_color}SHADOW{self.purple_color} take '+self.thanos+"\n"
            
            print(score)
            SCORE = rf"{score}"
            how_mach_rock = re.findall(self.rock,SCORE)
            how_mach_paper = re.findall(self.paper,SCORE)
            how_mach_scissors = re.findall(self.scissors,SCORE)

        #    print(how_mach_rock)
        #    print(how_mach_paper)
        #    print(how_mach_scissors)

            if len(how_mach_scissors) <= 1 :
                try:
                    if (how_mach_scissors[0] == "scissors") and (how_mach_rock[0] == "rock") :
                        self.scissors_to_rock()
                        if self.shadow_1v1 == False :
                            ask = str(input(f"\n\n {self.red_color}       Ops . u loss ..\n\n\n{self.purple_color}        if u need to play to him again  \n        [{self.cyan_color}#{self.purple_color}] press any kay \n\n        if u need to get out to home page\n        [{self.cyan_color}1{self.purple_color}] press 1 \n\n        [{self.cyan_color}->{self.purple_color}] : {self.green_color}"))
                            if ask == "1" :
                                self.start()
                            else:
                                self.SHADOW()

                        if self.shadow_1v1 == True :
                            self.shadow_point +=  1
                            print(f"\n\n{self.green_color}        Ops , u loss ..{self.purple_color}")
                            time.sleep(1)
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  SHADOW : {self.shadow_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.SHADOW()   

                except:
                    pass
                
                try:
                    if (how_mach_scissors[0] == "scissors") and (how_mach_paper[0] == "paper") :
                        self.scissors_to_paper()
                        print(f"\n\n{self.green_color}        yesssss , u win ..{self.purple_color}")                                                              
                        if self.shadow_1v1 == False :                                        
                            time.sleep(1)
                            self.win_massage()

                        if self.shadow_1v1 == True :
                            self.player_point +=  1
                            input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  SHADOW : {self.shadow_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                            self.SHADOW()

                except:
                    pass
            else:
                self.scissors_to_scissors()
                if self.shadow_1v1 == False :
                    input(f"\n\n{self.cyan_color}        it is equals , play again .. \n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
                    self.SHADOW()

                if self.shadow_1v1 == True :
                    print(f"\n\n{self.green_color}        it is equals , play again ..{self.purple_color}")
                    time.sleep(1)
                    input(f"\n\n{self.purple_color}        the score is :\n{self.green_color}        {self.yourname} : {self.player_point}  {self.purple_color}and{self.red_color}  SHADOW : {self.shadow_point}\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay \n\n")
                    self.SHADOW()

        if ((your_input != "1") or (your_input != "ROCK") or (your_input !="rock")) and ((your_input != "2") or (your_input != "PAPER") or (your_input !="paper")) and ((your_input != "3") or (your_input != "SCISSORS") or (your_input !="scissors")) : 
            input(f"\n {self.red_color}       wrong input .. \n\n\n\n      {self.purple_color}  ")
            self.SHADOW()


    # a message that came out to screen when u play story mode and win all matches 
    def win_massage(self):
        os.system("clear")
        print(f"{self.purple_color}        aaaaaah , well , just because you got here and read this message , it means that you beat the toughest hero in the game \n\n")
        time.sleep(4)
        print(f"{self.cyan_color}        congratulations{self.purple_color} , and the hero{self.green_color} shadow{self.purple_color} tells you : \n        {self.purple_color}you have supernatural powers in your hands so i lost the battle \n        maybe in the future you will be something{self.purple_color} GREAT {self.cyan_color}with these hands \n        only if you use them correctly")
        input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
        self.start()
        

    # when you take number 2 from home page 
    def all_heros (self):
        os.system("clear")
        self.refreash()
        self.logo()
        time.sleep(2)
        print(f"{self.purple_color}        [{self.cyan_color}+{self.purple_color}] chose who you want to fight : \n")
        print(f"{self.purple_color}        [{self.cyan_color}1{self.purple_color}] JOKER")
        print(f"{self.purple_color}        [{self.cyan_color}2{self.purple_color}] ZORO")
        print(f"{self.purple_color}        [{self.cyan_color}3{self.purple_color}] THANOS")
        print(f"{self.purple_color}        [{self.cyan_color}4{self.purple_color}] SHADOW\n")
        answer = str(input(f"        [{self.cyan_color}#{self.purple_color}] hmmm , i will take number :{self.green_color} "))
        if (answer == "1") or (answer == "JOKER") or (answer == "joker") :
            self.joker_info = True
            self.joker_1v1 = True
            self.JOKER()
        if (answer == "2") or (answer == "ZORO") or (answer == "zoro") :
            self.zoro_info = True
            self.zoro_1v1 = True
            self.ZORO()
        if (answer == "3") or (answer == "THANOS") or (answer == "thanos") :
            self.thanos_info = True
            self.thanos_1v1 = True
            self.THANOS()
        if (answer == "4") or (answer == "SHADOW") or (answer == "shadow") :
            self.shadow_info = True
            self.shadow_1v1 = True
            self.SHADOW()
        if ((answer != "1") or (answer != "JOKER") or (answer != "joker")) and ((answer != "2") or (answer != "ZORO") or (answer != "zoro")) and ((answer != "3") or (answer != "THANOS") or (answer != "thanos")) and ((answer != "4") or (answer != "SHADOW") or (answer != "shadow"))   :
            os.system("clear")
            input(f"\n {self.red_color}       wrong input .. \n\n\n\n      {self.purple_color}  ")
            self.all_heros()

    # to refreash points to zero 
    def refreash (self):
        
        self.joker_info = False
        self.zoro_info = False
        self.thanos_info = False
        self.shadow_info = False

        self.joker_1v1 = False
        self.zoro_1v1 = False
        self.thanos_1v1 = False
        self.shadow_1v1 = False

        self.player_point = 0
        self.joker_point = 0
        self.zoro_point = 0
        self.thanos_point = 0
        self.shadow_point = 0
        self.point_to_win = 3

    # when you take number 3 from home page 
    def info(self):
        os.system("clear")
        self.logo()
        info = f"\n  {self.green_color}INFORMATION :\n\n\t{self.purple_color}This game was made for fun , with a code i tried to explain well \n\ti hope you enjoy it .. \n\n\tand to contact the{self.cyan_color} developer{self.purple_color} on TELEGRAM : {self.cyan_color}https://t.me/the_crazy_shadow/{self.purple_color}\n"
        print(info)
        time.sleep(2)
        input(f"\n\n{self.purple_color}        [{self.cyan_color}#{self.purple_color}] press any kay  ")
        self.start()



if __name__ == "__main__" : 
    game() # to start this def code to work first auto [[   def __init__(self) :   ]]

