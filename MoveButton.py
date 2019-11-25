from quadline import Observer, Quadline


class MoveButton(Observer):
    quadline: Quadline

    def __init__(self, quadline: Quadline):
        self.quadline = quadline

    def update(self):
        self.quadline.make_move(None)

