import pygame as pg
class Grid:    
    def __init__(self,screen,n_square) -> None:
        self.n_square = n_square
        self.screen_ = screen
        self.line_len_ = screen.get_width()
        self.square_size_ = self.line_len_/n_square
    def drawGrid(self):
        for i in range(1,self.n_square+1):
            pg.draw.line(self.screen_,"green",(i*self.square_size_,0),(i*self.square_size_,self.line_len_))
            pg.draw.line(self.screen_,"green",(0,i*self.square_size_),(self.line_len_,i*self.square_size_))

    def drawBackground(self,screen,color : str):
        screen.fill(color)
    
    def get_square_size(self):
        return self.square_size_

    

    


