from quadline import Observer


class Observable:

    observers: [Observer]

    def attach(self, o: Observer):
        self.observers.add(o)

    def detach(self, o: Observer):
        self.observers.remove(o)

    def notify_observers(self):
        for i in self.observers:
            i.update(self)

    def get_observers(self):
        return self.observers
