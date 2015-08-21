""" Chatbot - Post to slack as another user
    Author: Edward Tirado Jr."""

#!/usr/bin/python
from __future__ import print_function
import os
import urllib
import json

url = os.environ['SLACK_HOOK']

characterJSON = open('characters.json').read()
output_json = json.loads(characterJSON)
totalCharacters = len(output_json["characters"])

for index, character in enumerate(output_json["characters"]):
    print(str(index + 1) + ') ' + character["username"])

    if index == totalCharacters - 1:
        print(str(index + 2) + ') Other')


character = raw_input("Choose a character => ")
channel = raw_input("Enter channel => ")


#Enter character if 'Other' is chosen
if int(character) == totalCharacters + 1:
    username = raw_input("Enter username => ")
    icon_url = raw_input("Enter image url => ")

else:
    username = output_json["characters"][int(character) - 1]['username']
    icon_url = output_json["characters"][int(character) - 1]['icon_url']


message = raw_input("Enter message => ")
params = {"username":username,
          "icon_url":icon_url,
          "text": message,
          "channel":channel,
          "link_names":1
         }

data = json.dumps(params)
req = urllib.urlopen(url, data)
print(req.read()) #Display send status
