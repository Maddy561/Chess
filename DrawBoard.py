import arcade


class DrawBoard(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHEAT)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 1:
                    arcade.draw_lrtb_rectangle_filled(100*i,100*(i+1),100*(j+1),100*j, arcade.color.DARK_BROWN)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


