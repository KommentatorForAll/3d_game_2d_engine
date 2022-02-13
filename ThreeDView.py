import arcade
from arcade import View

from entities.Player import Player
from level import Level


class ThreeDView(View):

    def __init__(self):
        super().__init__()
        self.level = Level.create_level()
        self.player = Player()
        self.player.position = 500, 100

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.player.draw_hit_box((0, 0, 255), 3)
        self.level.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        self.player.on_key_press(symbol, modifiers)

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.player.on_key_release(_symbol, _modifiers)

    def update(self, delta_time: float):
        self.player.update()
