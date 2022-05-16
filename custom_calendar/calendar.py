from datetime import datetime
from event import Event


class Calendar:
    def __init__(self, events):
        self.events = events

    def add_event(self, event):
        if not isinstance(event, Event):
            raise TypeError(f'Invalid type of event: {event}')

        self.events.append(event)

    def remove_event(self, start_date):
        parsed_date = self._parse_date(start_date)

        for event in self.events:
            if event.start_time == parsed_date:
                self.events.remove(event)

    @staticmethod
    def _parse_date(start_date):
        try:
            parsed_date = datetime.strptime(start_date, '%d-%m-%Y %H:%M')
        except ValueError:
            raise ValueError(f'Invalid date format, use DD-MM-YYYY HH:MM, {start_date}')
        return parsed_date

    def get_events_by_date(self, start_date):
        parsed_date = self._parse_date(start_date)
        return sorted([event for event in self.events if event.start_time > parsed_date], key=lambda x: x.start_time)

    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, val):
        if not isinstance(val, list):
            raise TypeError('Something went wrong!')
        self._events = val

    def __str__(self):
        return f'{type(self).__name__}: {self.events}'

    def __repr__(self):
        return f'{type(self).__name__}({self.events})'
