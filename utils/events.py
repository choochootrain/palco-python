import eventful

class Events:

  def __init__(self):
    self.api = eventful.API('fDJhdqLtn39Nbfcq')

  def search(self, query='', location='Berkeley'):
    evts = []
    events = self.api.call('/events/search', q=query, l=location)
    for event in events['events']['event']:
      evts.append((event['title'], event['venue_name']))
    return evts

  def nearby(self, query=''):
    events1 = self.search(query, 'San Francisco')
    events2 = self.search(query, 'Oakland')
    events3 = self.search(query, 'Berkeley')
    events4 = self.search(query, 'San Jose')
    events5 = self.search(query, 'Palo Alto')
    events6 = self.search(query, 'Fremont')

    return list(set(events1+events2+events3+events4+events5+events6))
