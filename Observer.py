from quadline import Observable


class Observer:

    def update(self, o: Observable):
        raise NotImplementedError
