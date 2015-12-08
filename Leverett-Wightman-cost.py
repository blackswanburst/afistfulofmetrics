#! /usr/bin/env python
# coding=UTF-8
# Filename: Leverett-Wightman-cost.py
# Template python-shodan code from:
# eireann.leverett@cantab.net
# www.concinnity-risks.com

import time, sys
from shodan import Shodan

SHODAN_API_KEY = ""

if SHODAN_API_KEY == "":
	print "Please add an API key to use this code."
	sys.exit()

# Create a connection to the Shodan API
api = Shodan(SHODAN_API_KEY)

FACETS = [
('org', 10),
('asn', 10),
# We only care about the top 5 countries, this is how we let Shodan know to return 5 instead of the
# default 10 for a facet. If you want to see more than 10, you could do ('country', 1000) for example
# to see the top 1,000 countries for a search query.
('country', 10),
]

FACET_TITLES = {
'org': 'Top 10 Organizations',
'asn': 'Top 10 Autonomous Systems',
'country': 'Top 10 Countries',
}

#Queries Shodan for a search term and then stores results in a list of dictionaries
def query_Shodan(term):
	try:
		#Search Shodan
		results = api.count(term, facets=FACETS)
	except Exception, e:
		#No results found, print no 'matches'
		print 'No %s\r' %e
	#Returns a list of dictionary objects. Each dictionary is a result
	return results

# Input validation
if len(sys.argv) == 1:
	print 'Usage:%s<search query>' %sys.argv[0]
	sys.exit(1)

query = ' '.join(sys.argv[1:])

result = query_Shodan(query)

shodancost = 19.00
ipcost = shodancost/4294967296

print 'Shodan Summary Information'
print 'Query:%s' % query
print 'Total Results: %s\n' % result['total']
if result['total'] == 0:
	IPv4lwcost = float('Inf')
else:
	IPv4lwcost = (shodancost/result['total'])
print 'All-IPv4 L-W cost:  $%f\n' % IPv4lwcost
# Print the summary info from the facets
for facet in result['facets']:
	print FACET_TITLES[facet]
	for term in result['facets'][facet]:
		print term['value']+'\n'
		query = facet+':\"%s\"' % term['value']
		vips = api.count(query)
		print '%f' % ((ipcost*vips['total'])/term['count'])
		print ''
