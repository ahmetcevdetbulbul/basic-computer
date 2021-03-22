import random
import time


class Computer():
    def __init__(self,pc_power = "Close",pc_voice = 0,games = ["aoe3"],Ram = "8 Gb",random_game = ["aoe3"]):

        self.pc_power = pc_power
        self.pc_voice = pc_voice
        self.games = games
        self.Ram = Ram
        self.random_games = random_game

    def open_pc(self):
        print("Getting Ready...")
        self.pc_power ="Open"

    def close_pc(self):
        print("Computer is closing")
        self.pc_power = "Close"

    def voice(self):

        while True:

            character = input("to increase: '>'-to decrease: '<'-to exit: 'q'")

            if character == "<":
                if self.pc_voice != 0:
                    self.pc_voice -= 1
                    print("%",self.pc_voice)

            elif character == ">":
                if self.pc_voice != 100:
                    self.pc_voice += 1
                    print("%", self.pc_voice)

            elif character =="q":
                break

            else:
                print("invalid!!")
                break
    def add_games(self,game):
        print(game,"added")
        time.sleep(1)
        self.games.append(game)

    def random_game_select(self):
        randomx = random.randint(0,len(self.games)-1)

        self.random_games = self.games[randomx]
        print("Last played:",self.random_games)


    def __str__(self):
        return "Computer: {}\nVoice: %{}\nGames: {}\nRam: {}\nLast played: {}".format(self.pc_power,self.pc_voice,self.games,self.Ram,self.random_games)

    def __len__(self):
        return len(self.games)



computer1 = Computer()

print("""
***************************
Welcome to Computer

	Transactions:
	
1. Open Computer

2. Close computer

3. About Computer

4. Number of Games

5. Add Game

6. Last played

7. Voice settings

To exit 'q'
***************************
""")

while True:
    option = input("choose option:")
    if option == "q":

        break

    elif option == "1":
        if computer1.pc_power != "Open":

            computer1.open_pc()
        else:
            print("Computer still open")

    elif option == "2":
        if computer1.pc_power != "Close":
            computer1.close_pc()

        else:
            print("Eror")

    elif option == "3":
        print(computer1)

    elif option == "5":
        gamesx = input("Enter the games you want to add, separating them with ',':")
        willadd = gamesx.split(",")

        for i in willadd:
            computer1.add_games(i)

    elif option == "4":
        print("Number of Games",len(computer1))

    elif option == "6":
        computer1.random_game_select()

    elif option == "7":
        computer1.voice()

    else:
        print("EROR!")


