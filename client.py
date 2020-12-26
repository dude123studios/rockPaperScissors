import pygame
from network import Network

import pickle
width = 700
height = 700

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("client")

client_num = 0

class Button:
    def __init__(self,x,y,text,color):
        self.text = text
        self.x=x
        self.y=y
        self.text=text
        self.color
        self.width = 150
        self.height = 100
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
        font = pygame.font.SysFont("comicsans",40)
        text = font.render(self.text,1,(255,255,255))
        win.blit(text, (self.x+round(self.width/2)-round(text.get_width()/2),
                        self.y+round(self.height/2)-round(text.get_height() /2)))
    def click(self,pos):
        x1=pos[0]
        y1=pos[1]
        if self.x <=x1 <= self.x+self.width and self.y <=y1<=self.y+self.height:
            return True
        else:
            return False

def redraw_window(win,game,p):
    win.fill((128, 128, 128))

    if not (game.connected()):
        font = pygame.font.SysFont("comicsans",80)
        text = font.render("Waiting for player...",1,(255,0,0),True)
        win.blit(text, (width/2-text.get_width()/2,height/2-text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Your Move", 1, (255, 0, 0))
        win.blit(text, (80,200))

        text = font.render("Opponents", 1, (255, 0, 0))
        win.blit(text, (380, 200))

btns = [Button('Rock',50,500,(0,0,0)),Button('Paper',250,500,(255,0,0)),Button('Scissors',450,500,(0,255,0))]
def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    p = int(n.get_p())
    print('You are player',p)
    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print('Couldnt get game')
            break
        if game.both_gone():
            redraw_window()
            pygame.time.delay(200)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break
            font = pygame.font.SysFont('comicsans',100)
            if (game.winner() == 1 and p == 1) or (game.winner()==-1 and p == 0):
                text = font.render("You Won!",1,(255,0,0))
            elif game.winner() == 0:
                text = font.render("Tie Game",1,(255,0,0))
            else:
                text = font.render("You Lost...",1,(255,0,0))
            win.blit(text, (width/2-text.get_width()/2,height/2-text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if p ==0:
                            if not game.p1gone:
                                n.send(btn.text)
                        else:
                            if not game.p2gone:
                                n.send(btn.text)
        redraw_window(win,game,p)
main()