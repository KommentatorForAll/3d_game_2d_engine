import arcade
from arcade import Window

from ThreeDView import ThreeDView


def main():
    window = Window(500, 500)
    three_d_view = ThreeDView()
    window.show_view(three_d_view)
    arcade.run()


if __name__ == '__main__':
    main()
