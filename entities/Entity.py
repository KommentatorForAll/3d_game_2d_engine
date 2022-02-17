from abc import ABC

from arcade import Sprite

from level import Level


class Entity(Sprite, ABC):
    def __init__(self, speed: int, hit_box_sprite: Sprite, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed: int = speed
        self.hit_box_sprite: Sprite = hit_box_sprite

    def move(self):
        raise NotImplemented()

    def __move(self):
        pos = self.hit_box_sprite.position
        self.hit_box_sprite.position = pos[0] + self.change_x, pos[1]
        if Level.current_level is not None and Level.current_level.collides(self.hit_box_sprite):
            self.hit_box_sprite.position = pos
        pos = self.hit_box_sprite.position
        self.hit_box_sprite.position = pos[0], pos[1] + self.change_y
        if Level.current_level is not None and Level.current_level.collides(self.hit_box_sprite):
            self.hit_box_sprite.position = pos

        self.angle += self.change_angle

        self.position = self.hit_box_sprite.position

    def update(self):
        super().update()
        self.move()
        self.__move()
        self.stop()
        self.hit_box_sprite.position = self.position
