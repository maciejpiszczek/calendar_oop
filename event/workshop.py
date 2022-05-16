from event import Event


class Workshop(Event):
    def __init__(self, title, location, start_time, duration, owner, participants, kind):
        super().__init__(title, location, start_time, duration, owner, participants)
        self.kind = kind
