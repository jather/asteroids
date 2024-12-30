from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS
