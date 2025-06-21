import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
#colors 
black = (0,0,0)
green = (0,255,0)
screen.fill(black)

#rectangle class
class CustomRect:
    def __init__(self,color,dimension):
        self.rect_surface = screen
        self.rect_color = color
        self.rect_dimension = dimension
    def draw(self):
        pygame.draw.rect(self.rect_surface,self.rect_color,self.rect_dimension)

#create objects 
greenRect = CustomRect(green,(50,20,100,100))

greenRect.draw()
pygame.display.update()
