# chatbot
A script to send a message as someone else in Slack


Setup
-------------
For this to work you'll need a webhook for your chat group.  You can get that here:
https://my.slack.com/services/new/incoming-webhook/

Then you need to tell your script to use that hook. You have a couple of options for that.

1) Add an environment variable named 'SLACK_HOOK' to your OS that contains your web hook. No code change necessary.

2) Change the line in chatbot.py that says: 
url = os.environ['SLACK_HOOK'] 

to 

url = 'http://yourwebhook'


That should be enough to get you up and running with the default characters.  Just follow the directions to send a message.


Adding/changing characters
--------------------------
The script pulls a list of characters from characters.json.  The list contains a set of pairs than contain the username and image for the message sender.  Add or remove them as needed.
