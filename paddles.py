import arcade

RECT_WIDTH = 10
RECT_HEIGHT = 100
RECT_COLOR = arcade.color.BLUE

class Paddle:

    # Initilize the paddle params
    def __init__(self):

        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    # Updates the paddle 
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

    # Draws the paddle on the screen
    def draw(self):
        arcade.draw_rect_filled(
            arcade.rect.XYWH(self.center_x, self.center_y, RECT_WIDTH, RECT_HEIGHT), RECT_COLOR)