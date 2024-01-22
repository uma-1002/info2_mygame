import pyxel

class App:
    def __init__(self):
        pyxel.init(200,200)
        pyxel.load("assets/mygame.pyxres")
        self.ball = Ball()
        self.keeper = Keeper()
        self.team1score = 0
        self.team2score = 0
        self.team1_flag = False
        self.team2_flag = False
        
        pyxel.run(self.update, self.draw)
 

    def update(self):
        self.ball.move()
        self.keeper.move()



        if self.ball.y <= 80:
            self.ball.dir = None
            if self.keeper.catch(self.ball):
                self.team2score +=1
                self.ball.score_flag = False
                if self.team2score >= 5:
                    self.team2_flag = True
            if self.ball.score_flag:
                self.team1score +=1
                if self.team1score >= 5:
                    self.team1_flag = True
            self.ball.restart()
            self.keeper.restart()
        if self.keeper.y <= 50:
            self.keeper.dir = None


    def draw(self):
        pyxel.cls(7)
        if self.team1_flag:
            pyxel.text(70, 100, "kicker Wins!!", 0)
        elif self.team2_flag:
            pyxel.text(70, 100, "keeper wins!!", 0)
        else:
            pyxel.rect(0, 100 ,200, 100, 11)
            pyxel.rect(0, 0, 200, 100, 6)
            pyxel.rect(26, 50, 4, 70, 7)
            pyxel.rect(26, 46, 148, 4, 7)
            pyxel.rect(170, 50, 4, 70, 7)
            pyxel.rect(98, 193, 4, 4, 7)
            pyxel.rect(0, 120, 200, 2, 7)
            pyxel.line(20, 120, 5, 150, 7)
            pyxel.rect(5, 150, 190, 2, 7)
            pyxel.line(180, 120, 195, 150, 7)
            pyxel.blt(self.ball.x - 8, self.ball.y, 0, 0, 0, 16, 16, 0)
            pyxel.blt(self.keeper.x - 16 , self.keeper.y + 33 ,1, 0, 0, 32, 32, 0)
            pyxel.text(0, 0, "Kicker: " + str(self.team1score), 7)
            pyxel.text(40, 0, "Keeper: " + str(self.team2score), 7)

class Ball:
    def __init__(self):
        self.restart()

    def restart(self):
        self.x = 100
        self.y = 180
        self.dir = None
        self.score_flag = True
        self.keeper_flag = False

    def move(self):
        if pyxel.btnr(pyxel.KEY_D) or pyxel.btnr(pyxel.KEY_A) or pyxel.btnr(pyxel.KEY_S):
            self.keeper_flag = True
        if self.keeper_flag:
            if self.dir == pyxel.KEY_RIGHT:
                self.x += 5
                self.y -= 10
            elif self.dir == pyxel.KEY_LEFT:
                self.x -= 5
                self.y -= 10
            elif self.dir == pyxel.KEY_UP:
                self.y -= 10

        
        if pyxel.btnr(pyxel.KEY_RIGHT):
            self.dir = pyxel.KEY_RIGHT
        elif pyxel.btnr(pyxel.KEY_LEFT):
            self.dir = pyxel.KEY_LEFT
        elif pyxel.btnr(pyxel.KEY_UP):
            self.dir = pyxel.KEY_UP
    
    
class Keeper:
    def __init__(self) :
        self.restart()

    def restart(self) :
        self.x = 100
        self.y = 55
        self.dir = None

    def move(self):
        if self.dir == pyxel.KEY_D:
            self.x += 11
            self.y -= 1
        elif self.dir == pyxel.KEY_A:
            self.x -= 11
            self.y -= 1
        elif self.dir == pyxel.KEY_S:
            self.y -= 1

        
        if pyxel.btnr(pyxel.KEY_D):
            self.dir = pyxel.KEY_D
        elif pyxel.btnr(pyxel.KEY_A):
            self.dir = pyxel.KEY_A
        elif pyxel.btnr(pyxel.KEY_S):
            self.dir = pyxel.KEY_S

    def catch(self, ball):
        return ball.y <= 80 and self.x - 16 <= ball.x <= self.x + 16 and ball.score_flag

App()
