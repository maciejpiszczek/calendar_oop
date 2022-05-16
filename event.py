from datetime import timedelta
from datetime import datetime


class Event:
    def __init__(self, title, location, start_time, duration, owner, participants):
        self.title = title
        self.location = location
        self.start_time = start_time
        self.duration = duration
        self.owner = owner
        self.participants = participants

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, val):
        if not isinstance(val, str):
            raise TypeError(f'Invalid value: {val}')

        try:
            parsed_date = datetime.strptime(val, '%d-%m-%Y %H:%M')
        except ValueError:
            raise ValueError(f'Invalid date format, use DD-MM-YYYY HH:MM, {val}')

        if parsed_date < datetime.now() + timedelta(minutes=15):
            raise ValueError(f'Not enough time to organize a meeting: {parsed_date - datetime.now()}')

        self._start_time = val

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(str(value)):
            self._title = value
        else:
            self._title = "No title"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Invalid duration value ({value}), use integer or float!')

        if not (10 < value < 600):
            raise ValueError(f'Too short or too long: {value} minutes')

        self._duration = timedelta(minutes=value)


e = Event(42, '', '16-05-2022 14:00', 20, '', '')
print(e.start_time)
