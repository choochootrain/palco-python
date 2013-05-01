import eventful
import urllib2
from bs4 import BeautifulSoup
import re

class Events:

  def __init__(self):
    self.api = eventful.API('fDJhdqLtn39Nbfcq')

  def search(self, query='', location='Berkeley'):
    evts = []
    events = self.api.call('/events/search', q=query, l=location)
    for event in events['events']['event']:
      evts.append((event['title'], event['venue_name']))
    return evts

  def scrape(self, loc, q):
    o = urllib2.build_opener()
    o.addheaders = [('user-agent', 'Mozilla/5.0')]

    url = "http://www.eventbrite.com/directory?sort=date&loc="+loc+"&q="+q+"&date=week"

    u = o.open(url).read()

    j= BeautifulSoup(u)
    if len(j) == 0:
      print "Sorry, couldn't find anything"
    else:
      l =[]
      for i in j:
        for x in re.findall("<dd(w*)>(.*)</dd>", str(i)):
          l.append(x[1])
      return l

  def nearby(self, query=''):
    events1 = self.search(query, 'San Francisco')
    events2 = self.search(query, 'Oakland')
    events3 = self.search(query, 'Berkeley')
    events4 = self.search(query, 'San Jose')
    events5 = self.search(query, 'Palo Alto')
    events6 = self.search(query, 'Fremont')
    events7 = self.scrape('San+francisco', 'music')

    return list(set(events1+events2+events3+events4+events5+events6+events7))
