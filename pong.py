"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import ball
import paddles

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"

class StartScreen(arcade.View):
    def on_show_view(self):
    
        self.window.background_color = arcade.csscolor.DARK_SLATE_BLUE

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        # self.window.default_camera.use()
    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_text("Pong", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press 1 for 1 ball", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Press 2 for 2 balls", self.window.width / 2, self.window.height / 2-100,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        
    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.KEY_1:
            balls = 1
            game_view = GameView()
            game_view.setup(balls)
            self.window.show_view(game_view)
        elif key == arcade.key.KEY_2:
            balls = 2
            game_view = GameView()
            game_view.setup(balls)
            self.window.show_view(game_view)


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.AMAZON

        # If you have sprite lists, you should create them here,
        # and set them to None

        self.scoreL = 0
        self.scoreR = 0
        self.direction = 0
        self.scoreL_text = None
        self.scoreR_text = None
        self.balls = []

        self.paddleR = paddles.Paddle()
        self.paddleL = paddles.Paddle()

    def createBall(self, y):
        z = 0
        if y % 2:
            z = -1
        else:
            z = 1

        newBall = ball.Ball(WINDOW_HEIGHT, WINDOW_WIDTH)
        newBall.center_x = self.width // 2
        newBall.center_y = self.height // 2
        newBall.change_x = 5*z
        newBall.change_y = 7*z
        
        return newBall

    def setup(self, ballCount):
        self.scoreL = 0
        self.scoreR = 0
        self.scoreL_text = arcade.Text(f"Score: {self.scoreL}", x = 20, y = WINDOW_HEIGHT-15)
        self.scoreR_text = arcade.Text(f"Score: {self.scoreR}", x = WINDOW_WIDTH - 100, y = WINDOW_HEIGHT-15)

        self.paddleL.center_x = 50
        self.paddleL.center_y = WINDOW_HEIGHT / 2

        self.paddleR.center_x = WINDOW_WIDTH - 50
        self.paddleR.center_y = WINDOW_HEIGHT / 2

        y = 0
        for x in range(ballCount):
            self.balls.append(self.createBall(y))
            y += 1


    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        self.scoreL_text.draw()
        self.scoreR_text.draw()
        self.paddleL.draw()
        self.paddleR.draw()
        for ball in self.balls:
            ball.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        ballScore = None
        
        for ball in self.balls:
            if ball.center_x < 25:
                self.scoreR += 1
                self.scoreR_text.text = f"Score: {self.scoreR}"
                ballScore = ball
                self.direction+=1
                continue
                

            if ball.center_x > (WINDOW_WIDTH-25):
                self.scoreL += 1
                self.scoreL_text.text = f"Score: {self.scoreL}"
                ballScore = ball
                self.direction+=1
                continue
            
            if ((ball.center_x - 25) < self.paddleL.center_x + 5) and (ball.center_y <= (self.paddleL.center_y + 50)) and (ball.center_y >= (self.paddleL.center_y - 50)):
                ball.change_x *= -1
                ball.change_x *= 1.1
                ball.change_y *= 1.1
            if ((ball.center_x + 25) > self.paddleR.center_x - 5) and (ball.center_y <= (self.paddleR.center_y + 50)) and (ball.center_y >= (self.paddleR.center_y - 50)):
                ball.change_x *= -1
                ball.change_x *= 1.1
                ball.change_y *= 1.1
            ball.update()

        self.paddleR.update()
        self.paddleL.update()

        if ballScore:
            self.balls.remove(ballScore)

            self.balls.append(self.createBall(self.direction))

        # if ((self.ball.center_x - 25) < self.paddleL.center_x + 5) & (self.ball.center_y <= (self.paddleL.center_y + 50)) & (self.ball.center_y >= (self.paddleL.center_y - 50)):
        #     self.ball.change_x *= -1
        # if ((self.ball.center_x + 25) > self.paddleR.center_x - 5) & (self.ball.center_y <= (self.paddleR.center_y + 50)) & (self.ball.center_y >= (self.paddleR.center_y - 50)):
        #     self.ball.change_x *= -1

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.UP:
            self.paddleR.change_y = 10
        elif key == arcade.key.DOWN:
            self.paddleR.change_y = -10

        if key == arcade.key.W:
            self.paddleL.change_y = 10
        elif key == arcade.key.S:
            self.paddleL.change_y = -10

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP:
            self.paddleR.change_y = 0
        elif key == arcade.key.DOWN:
            self.paddleR.change_y = 0

        if key == arcade.key.W:
            self.paddleL.change_y = 0
        elif key == arcade.key.S:
            self.paddleL.change_y = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = StartScreen()

    #game.setup()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()



if __name__ == "__main__":
    main()