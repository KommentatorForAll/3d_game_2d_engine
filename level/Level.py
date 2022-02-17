import random
from typing import Optional

from arcade import SpriteList, Sprite

from level.LevelElement import LevelElement


current_level: Optional["Level"] = None


class Level:

    def __init__(self):
        self.elements = SpriteList(use_spatial_hash=True)

    def draw(self):
        self.elements.draw()
        self.elements.draw_hit_boxes((0, 0, 255), 3)

    def collides(self, other: Sprite) -> bool:
        return len(other.collides_with_list(self.elements)) > 0

    def append(self, element: LevelElement):
        self.elements.append(element)


def create_level():
    level = Level()
    for i in range(20):
        element = LevelElement("ray_caster_hitbox.png")
        element.position = random.randrange(50, 400), random.randrange(50, 400)
        level.append(element)
    return level

#
# def collide(a: Sprite, b: Sprite) -> bool:
#     total_collision_radius_sum = a.collision_radius + b.collision_radius
#     dx = a.position[0] - b.position[0]
#     dy = a.position[1] - b.position[1]
#     distance2 = dx**2 + dy**2
#     if total_collision_radius_sum**2 < distance2:
#         return False
#     return collision.collide(
#         Concave_Poly(Vector(0, 0), [Vector(*x) for x in a.get_adjusted_hit_box()]),
#         Concave_Poly(Vector(0, 0), [Vector(*x) for x in b.get_adjusted_hit_box()])
#     )
