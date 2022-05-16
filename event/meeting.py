from event import Event


class Meeting(Event):
    def __init__(self, title, location, start_time, duration, owner, participants, reason):
        super().__init__(title, location, start_time, duration, owner, participants)
        self.reason = reason
