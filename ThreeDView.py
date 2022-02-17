import arcade
from arcade import View, PerfGraph

import level.Level
from entities.Player import Player
from level import Level


class ThreeDView(View):

    def __init__(self):
        super().__init__()
        arcade.enable_timings(300)
        self.player = Player()
        if Level.current_level is None:
            Level.current_level = Level.create_level()
        self.player.position = 500, 0
        self.perf_graph = PerfGraph(100, 50)
        self.perf_graph.position = 50, 25

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.player.hit_box_sprite.draw_hit_box((0, 0, 255), 3)
        self.player.on_update()
        Level.current_level.draw()
        self.perf_graph.draw()

    def on_update(self, delta_time: float):
        self.perf_graph.update_graph(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        self.player.on_key_press(symbol, modifiers)

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.player.on_key_release(_symbol, _modifiers)

    def update(self, delta_time: float):
        self.player.update()
