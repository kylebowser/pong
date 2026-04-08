import arcade

# Rectangle info
RECT_WIDTH = 50
RECT_HEIGHT = 50
RECT_COLOR = arcade.color.DARK_BROWN

BACKGROUND_COLOR = arcade.color.ALMOND


class Ball:
    """ This class represents our rectangle """

    def __init__(self, wh, ww):

        # Set up attribute variables
        self.wh = wh
        self.ww = ww
        # Where we are
        self.center_x = 0
        self.center_y = 0

        # Where we are going
        self.change_x = 0
        self.change_y = 0

        # self.width = RECT_WIDTH
        # self.height = RECT_HEIGHT

        # self.set_hit_box_points([
        #     (-self.width/2, -self.height/2),
        #     ( self.width/2, -self.height/2),
        #     ( self.width/2,  self.height/2),
        #     (-self.width/2,  self.height/2)
        # ])

    def update(self):
        # Move the rectangle
        self.center_x += self.change_x
        self.center_y += self.change_y
        # Check if we need to bounce of right edge
        if self.center_x > self.ww - RECT_WIDTH / 2:
            self.change_x *= -1
        # Check if we need to bounce of top edge
        if self.center_y > self.wh - RECT_HEIGHT / 2:
            self.change_y *= -1
        # Check if we need to bounce of left edge
        if self.center_x < RECT_WIDTH / 2:
            self.change_x *= -1
        # Check if we need to bounce of bottom edge
        if self.center_y < RECT_HEIGHT / 2:
            self.change_y *= -1

    def draw(self):
        # Draw the rectangle
        arcade.draw_rect_filled(
            arcade.rect.XYWH(self.center_x, self.center_y, RECT_WIDTH, RECT_HEIGHT), RECT_COLOR)