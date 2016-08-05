import requests
import json

a = open("titles.txt")
k = a.read()
words = k.split('\n')
words = words[:-1]
for items in words:
   a = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&titles=%s"% items)
   response = json.loads(a.text)
   d = response['query']['pages'].keys()
   if d[0] == '-1':
     print "The item %s do not exist in the wiki"%items
   
  