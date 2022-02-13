from arcade import SpriteList, Sprite

from level.LevelElement import LevelElement


class Level:

    def __init__(self):
        self.elements = SpriteList()

    def draw(self):
        self.elements.draw()

    def collides(self, other: Sprite):
        return other.collides_with_list(self.elements)

    def append(self, element: LevelElement):
        self.elements.append(element)


def create_level():
    level = Level()
    element = LevelElement("map_v1.png", hit_box_algorithm="Detailed")
    element.position = 500, 500
    level.append(element)
    return level
