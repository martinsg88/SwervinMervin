import pygame, os
import settings as s
import world_object as wo

class Sprite(wo.WorldObject):
    """Represents a single sprite in a level."""

    def __init__(self, offset, name):
        self.offset     = offset
        self.sprite     = s.SPRITES[name]
        self.quantifier = 3
        self.hit        = False

    def is_hooker(self):
        """Returns True if this sprite is a live hooker."""
        return self.sprite.has_key("hooker")

    def path(self):
        sprite_name = self.sprite["path"]

        if self.is_hooker() and self.hit:
            sprite_name = sprite_name.replace(".", "_dead.")

        return pygame.image.load(os.path.join("lib", sprite_name))
