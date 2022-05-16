import random
from datetime import datetime, timedelta

from event import Event


class EventGenerator:
    def __init__(self):
        self.titles = ["Learn python", "Drive a car", "Clean up"]
        self.locations = ["Pcim", "Męcikał", "Kozia Wólka"]
        self.users = ["Ala", "Lech", "Roch", "Damian", "Izmael"]
        self.events = []

    def generate(self, quantity=100):
        for _ in range(quantity):
            event = Event(
                title=random.choice(self.titles),
                location=random.choice(self.locations),
                start_time=f'{(datetime.now() + timedelta(minutes=random.randint(50, 500000))):%d-%m-%Y %H:%M}',
                duration=random.randint(16, 599),
                owner=random.choice(self.users),
                participants=random.choices(self.users, k=random.randint(0, len(self.users)))
            )
            self.events.append(event)
