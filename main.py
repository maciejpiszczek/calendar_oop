from pprint import pprint as pp
from data.utils import EventGenerator
from custom_calendar import Calendar

data = EventGenerator()
data.generate(500)

c = Calendar(data.events)

result = c.get_events_by_date('22-05-2022 00:00')
# c.remove_event('20-05-2022 16:00')

pp(result)
