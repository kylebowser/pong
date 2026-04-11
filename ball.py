import arcade

RECT_WIDTH = 50
RECT_HEIGHT = 50
RECT_COLOR = arcade.color.DARK_BROWN

BACKGROUND_COLOR = arcade.color.ALMOND


class Ball:

    #Sets up the Ball
    def __init__(self, wh, ww):

        self.wh = wh
        self.ww = ww
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    # Updates the ball movements and handles to wall hit logic
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x > self.ww - RECT_WIDTH / 2:
            self.change_x *= -1
        if self.center_y > self.wh - RECT_HEIGHT / 2:
            self.change_y *= -1
        if self.center_x < RECT_WIDTH / 2:
            self.change_x *= -1
        if self.center_y < RECT_HEIGHT / 2:
            self.change_y *= -1
    
    # The draw function of the ball class
    def draw(self):
        arcade.draw_rect_filled(
            arcade.rect.XYWH(self.center_x, self.center_y, RECT_WIDTH, RECT_HEIGHT), RECT_COLOR)