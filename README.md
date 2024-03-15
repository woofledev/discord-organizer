# discord-organizer
a thing that takes discord messages through sentimental analysis 


## what?
this basically takes messages from a discord channel, takes each user and message and runs it<br>
through a sentimental analysis model. After, it generates results of how many traits each user has<br>
in the form of a pie chart (for now).

## usage
clone this repo, and then configure stuff in `config.py`<br>
to fetch messages, you can use the `fetchmsgs.py` script. assuming everything is configured, run:
```sh
python3 fetchmsgs.py
```
you can obtain messages in any other way you want too, as long as it aligns to the structure expected.<br>
**NOTE:** i am *not* responsible if this script gets your account termed. you should use it correctly.


<br><br>
to then categorize everything, just run:
```sh
python3 categorize.py
```
assuming everything is configured, again.

that's it! at the end of this, PNG chart results should generate into the same folder.