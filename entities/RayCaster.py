import typing

import arcade
from arcade import Sprite, Point

import settings
from entities.Entity import Entity
if typing.TYPE_CHECKING:
    from entities.Player import Player
from level import Level


class RayCaster(Entity):

    def __init__(self):
        super().__init__(8, Sprite("ray_caster_hitbox.png"))
        self.angle: float = 0
        self.position: Point = (0, 0)
        self.original_pos: Point = (0, 0)

    def cast(self, player: "Player"):
        self.original_pos = player.position
        self.position = player.position
        self.hit_box_sprite.position = self.position
        self.hit_box_sprite.angle = player.angle
        self.hit_box_sprite.angle -= settings.fov/2
        angle_incr = settings.fov/settings.resolution
        for i in range(settings.resolution):
            self.hit_box_sprite.position = self.original_pos
            self.cast_single()
            self.hit_box_sprite.angle += angle_incr

    def cast_single(self):
        steps = 0
        self.hit_box_sprite.forward(self.speed)
        while not Level.current_level.collides(self.hit_box_sprite) and steps < settings.render_distance:
            self.hit_box_sprite.update()
            steps += 1
        self.hit_box_sprite.stop()
        arcade.draw_line(*self.original_pos, *self.hit_box_sprite.position, (255, 255, 255), 3)

    def update(self):
        print("should not be called")

    def move(self):
        pass
