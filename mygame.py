import pyxel

class App:
    def __init__(self):
        pyxel.init(200,200)
        self.ball = Ball()
        
        pyxel.run(self.update, self.draw)

    def update(self):
        self.ball.move()

    def draw(self):
        pyxel.cls(3)
        pyxel.rect(10, 25, 180, 90, 7)
        pyxel.circ(self.ball.x, self.ball.y, 10, 6)

class Ball:
    def __init__(self):
        self.x = 100
        self.y = 180
        self.dir = None

    def move(self):
        if self.dir == pyxel.KEY_RIGHT:
            self.x += 2.5
            self.y -= 5
        elif self.dir == pyxel.KEY_LEFT:
            self.x -= 2.5
            self.y -= 5
        elif self.dir == pyxel.KEY_UP:
            self.y -= 5
        
        if self.y == 70:
            self.dir = None



        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.dir = pyxel.KEY_RIGHT
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.dir = pyxel.KEY_LEFT
        elif pyxel.btnp(pyxel.KEY_UP):
            self.dir = pyxel.KEY_UP

    
    



App()