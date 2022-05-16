from pprint import pprint as pp
from data.utils import EventGenerator
from custom_calendar import Calendar
from event import Event

data = EventGenerator()
# data.generate_events(500)
# data.save('./data.json')
events_data = data.load('./data.json')
# pp(events_data)

events = [Event(**event) for event in events_data]

c = Calendar(events)
result = c.get_events_by_date('22-05-2022 00:00')
print(result, len(result))
# c.remove_event('20-05-2022 16:00')
#
# pp(result)
