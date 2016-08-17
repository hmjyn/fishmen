class fishman:
    def __init__(self):
        self.name=fishman
        self.live=100
        self.livestatus=1
        self.fishnb=0
        self.fishchick=0
        self.fishislandnb=0
    def fishhamter(self):
        if random==1:
            self.fishnb+=1

    def fishtochick(self):
        self.fishnb-=1
        self.fishchick+=1

    def foodtolive(self):
        self.fishnb-=1
        self.live+=50
