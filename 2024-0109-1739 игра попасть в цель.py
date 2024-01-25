# ============================================
import pygame
import random as rnd


# ============================================
class Pos:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


# ------------------------------------
class Figure:
    def __init__(self, pos) -> None:
        self.setPos(pos)

    def setPos(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def isIn(self, x, y) -> bool:
        return False


class Square(Figure):
    def __init__(self, pos, w, h) -> None:
        super().__init__(pos)
        self.w = w
        self.h = h

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def isIn(self, x, y) -> bool:
        _pos = super().getPos()
        if (_pos.x < x) and ((_pos.x + self.w) > x) and (_pos.y < y) and ((_pos.y + self.h) > y):
            return True
        return False


# ----------------------------------
class HitMark:
    def __init__(self, cost) -> None:
        self.setCost(cost)
        self.setState(HitMark.State_Normal)

    def setCost(self, cost):
        self.cost = cost

    def getCost(self):
        return self.cost


class SquareHitMark(Square, HitMark):
    def __init__(self, pos, w, h, cost) -> None:
        super().__init__(pos, w, h)
        HitMark.setCost(self, cost)


# ---------------------------------
# класс внутриигрового сообщения
class GameEvent:
    # пустое событие
    Event_None = 0
    # событие таймера
    Event_Tick = 1
    # событие "выстрела" по цели
    Event_Hit = 2

    def __init__(self, type, data) -> None:
        self.type = type
        self.data = data

    def getType(self):
        return self.type

    def getData(self):
        return self.data


class GameLogic:
    def __init__(self, w, h) -> None:
        self.gameboard_width = w
        self.gameboard_height = h
        self.marks = []
        self.hitMarks = []
        self.score = 0

    def processEvent(self, event):
        if event.type == GameEvent.Event_Tick:
            markRandPos = Pos(rnd.randint(20, self.gameboard_width - 20)
                              , rnd.randint(20, self.gameboard_height - 20))

            markSize = rnd.randint(10, 20)
            markCost = 30 - markSize
            markColor = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
            mark = SquareHitMark(markRandPos, markSize, markSize, markCost)
            mark.setColor(markColor)
            self.addHitMark(mark)

        if event.type == GameEvent.Event_Hit:
            self.hit(event.data)

    def addHitMark(self, mark):
        self.marks.append(mark)

    def hit(self, pos):
        for markIndex in range(len(self.marks)):
            mark = self.marks[markIndex]
            if mark.isIn(pos.x, pos.y):
                self.score += mark.getCost()
                self.marks.pop(markIndex)
                self.hitMarks.append(mark)
                break

    def getBoard(self):
        return self.marks

    def getScore(self):
        return self.score


# -----------------------------------------
class PyGameGui:
    def __init__(self, w, h, logic) -> None:
        self.main_w = w
        self.main_h = h
        self.screen = pygame.display.set_mode([self.main_w, self.main_h])
        self.logic = logic
        self.font = pygame.font.SysFont('Consolas', 30)

    def run(self):
        running = True
        pygame.time.set_timer(pygame.USEREVENT + GameEvent.Event_Tick, 1000)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.processEvent(event)

            self.draw()

    def processEvent(self, event):
        if (event.type >= pygame.USEREVENT) and (event.type < pygame.NUMEVENTS):
            myevent = GameEvent(event.type - pygame.USEREVENT, None)
            self.logic.processEvent(myevent)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pypos = event.pos
            myevent = GameEvent(GameEvent.Event_Hit, Pos(pypos[0], pypos[1]))
            self.logic.processEvent(myevent)

    def draw(self):
        # Fill the background with white
        self.screen.fill((255, 255, 255))

        marks = self.logic.getBoard()
        for mark in marks:
            pygame.draw.rect(self.screen, mark.getColor(),
                             pygame.Rect(mark.getPos().x, mark.getPos().y, mark.getWidth(), mark.getHeight()))

        score = self.logic.getScore()
        self.screen.blit(self.font.render(f'score:{score}', True, (0, 0, 0)), (32, 48))

        # Flip the display
        pygame.display.flip()


# --------------------------------------------
if __name__ == "__main__":
    pygame.init()
    width = 800
    height = 600
    gui = PyGameGui(width, height, GameLogic(width, height))
    gui.run()
    pygame.quit()