from abc import ABC

from arcade import Sprite


class Entity(Sprite, ABC):
    def __init__(self, speed: int, hit_box_sprite: Sprite, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed: int = speed
        self.hit_box_sprite: Sprite = hit_box_sprite

    def move(self):
        raise NotImplemented()

    def update(self):
        self.move()
        super().update()
        self.stop()
        self.hit_box_sprite.position = self.position
