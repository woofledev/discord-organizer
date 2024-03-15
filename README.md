# discord-organizer
a thing that takes discord messages through sentimental analysis 


## what?
this basically takes messages from a discord channel, takes each user and message and runs it<br>
through a sentimental analysis model. After, it generates results of how many traits each user has<br>
in the form of a pie chart (for now).

## usage
```sh
git clone https://github.com/woofledev/discord-organizer && cd discord-organizer
pip3 install -r requirements.txt

# now, open config.py and configure everything to your liking.
# then, let's fetch messages:
python3 fetchmsgs.py

# after we've done that, we can simply run this to create our charts from the data:
python3 categorize.py
```

you can obtain messages in any other way you want to, as long as it aligns to the structure expected in `msgs.json`.<br>
**NOTE:** i am *not* responsible if the fetch script gets your account termed. you should use it correctly.