from random import randint

class fishman:
    def __init__(self):
        self.name="fishman"
        self.live=100
        self.livestatus=1
        self.fishnb=0
        self.fishchick=0
        self.fishislandnb=0
    def fishhamter(self):
        #rrrdd=1
        if randint(1,5) == 3:
            self.fishnb+=1
        #print rrrdd
        print self.fishnb
    def fishtochick(self):
        self.fishnb-=1
        self.fishchick+=1

    def foodtolive(self):
        self.fishnb-=1
        self.live+=50
    def printall(self):
        print self.name
        print self.live
        print self.livestatus
        print self.fishnb
        print self.fishchick
        print self.fishislandnb

if __


  #      print "name="+self.name
  #      print "live="+self.live
  #      print "livestatus="+self.livestatus
  #      print "fishnb="+self.fishnb
  #      print "fishchick="+self.fishchick
  #      print "fishislandnb="+self.fishislandnb

  
