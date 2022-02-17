import typing
from typing import List

import arcade.key as key
from arcade import Sprite

from entities.Entity import Entity
from entities.RayCaster import RayCaster


class Player(Entity):

    def __init__(self, *args, **kwargs):
        super().__init__(2, Sprite("player_hitbox.png"), "player.png", *args, **kwargs)
        self.pressed_keys: List[int] = []
        self.ray_caster = RayCaster()

    def on_update(self, delta_time: float = 1 / 60):
        self.ray_caster.cast(self)

    def move(self):
        # for button in self.pressed_keys:
        #     match button:
        #         case key.W:
        #             self.forward(self.speed)
        #         case key.S:
        #             self.forward(-self.speed)
        #         case key.A:
        #             self.strafe(self.speed/2)
        #         case key.D:
        #             self.strafe(-self.speed/2)
        #         case key.LEFT:
        #             self.change_angle += self.speed*2
        #         case key.RIGHT:
        #             self.change_angle -= self.speed*2
        for button in self.pressed_keys:
            if button == key.W:
                self.forward(self.speed)
            elif button == key.S:
                self.forward(-self.speed)
            elif button == key.A:
                self.strafe(self.speed / 2)
            elif button == key.D:
                self.strafe(-self.speed / 2)
            elif button == key.LEFT:
                self.change_angle += self.speed * 2
            elif button == key.RIGHT:
                self.change_angle -= self.speed * 2

    def on_key_press(self, symbol: int, modifiers: int):
        self.pressed_keys.append(symbol)

    def on_key_release(self, symbol: int, _modifiers: int):
        self.pressed_keys.remove(symbol)
