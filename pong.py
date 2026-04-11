import arcade
import ball
import paddles

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Pong"

class StartScreen(arcade.View):

    #creates the intro screen
    def on_show_view(self):
    
        self.window.background_color = arcade.csscolor.DARK_SLATE_BLUE

    #draws the inital view of the intro screen
    def on_draw(self):
        self.clear()
        arcade.draw_text("Pong", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press 1 for 1 ball", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Press 2 for 2 balls", self.window.width / 2, self.window.height / 2-100,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        
    #handles the key presses of the intro screen and initializes the actual game
    def on_key_press(self, key, key_modifiers):

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

    #initalize the pong game params
    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.AMAZON

        self.scoreL = 0
        self.scoreR = 0
        self.direction = 0
        self.scoreL_text = None
        self.scoreR_text = None
        self.balls = []

        self.paddleR = paddles.Paddle()
        self.paddleL = paddles.Paddle()

    # A helper method to create balls to be added to the game
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

    # sets up the game state 
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

    # draws the inital game state
    def on_draw(self):
        self.clear()

        self.scoreL_text.draw()
        self.scoreR_text.draw()
        self.paddleL.draw()
        self.paddleR.draw()
        for ball in self.balls:
            ball.draw()

    # Updates the game based on events that happen on screen and the users input
    def on_update(self, delta_time):
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

    # Handles key presses from the user
    def on_key_press(self, key, key_modifiers):

        if key == arcade.key.UP:
            self.paddleR.change_y = 10
        elif key == arcade.key.DOWN:
            self.paddleR.change_y = -10

        if key == arcade.key.W:
            self.paddleL.change_y = 10
        elif key == arcade.key.S:
            self.paddleL.change_y = -10

# Makes sure that when the user stops pressing the keys that the movements stop
    def on_key_release(self, key, key_modifiers):

        if key == arcade.key.UP:
            self.paddleR.change_y = 0
        elif key == arcade.key.DOWN:
            self.paddleR.change_y = 0

        if key == arcade.key.W:
            self.paddleL.change_y = 0
        elif key == arcade.key.S:
            self.paddleL.change_y = 0

# Main functin
def main():
    
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    game = StartScreen()

    window.show_view(game)

    arcade.run()



if __name__ == "__main__":
    main()