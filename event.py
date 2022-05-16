from datetime import timedelta, datetime


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

        self._start_time = parsed_date

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

    def __str__(self):
        delta_time = self.start_time - datetime.now()
        hours, rest = delta_time.seconds // 3600, delta_time.seconds % 3600
        minutes, seconds = rest // 60, rest % 60
        days = f'{delta_time.days} days, ' if delta_time.days > 0 else ''
        minutes = f'0{minutes}'[-2:]
        seconds = f'0{seconds}'[-2:]
        return f'{self.title}, time to event: {days}{hours}:{minutes}:{seconds}'

    def __repr__(self):
        return f"{type(self).__name__}('{self.title}', '{self.location}', {self.start_time:%d-%m-%Y %H:%M}, " \
               f"{self.duration.total_seconds() / 60}, '{self.owner}', {self.participants})"


e = Event('Piwo', 'Wwa', '16-05-2022 16:00', 20, 'Ala', ['Ela', 'Ola'])
print(repr(e))
