class businessman:
    def __init__(self,hp,money,happi):
        self.hp = hp
        self.money = money
        self.happi = happi
        self.report()
    def work(self):
        self.hp -=10
        self.money +=20
        self.happi +=10
    def sleep(self):
        self.money -=10
        self.hp +=20
        self.happi +=10
    def play(self):
        self.hp -=10
        self.money -=10
        self.happi +=20
    def report(self):
        print(f'HP : {self.hp} , Money : {self.money} , Happiness :{self.happi}')
john=businessman(100,100,100)
john.work()
john.report()
john.play()
john.report()
john.sleep()
john.report()
print('Thanks for pressing run button cutie!')


