import arcade
import DrawBoard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

def main():
    game = DrawBoard(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()