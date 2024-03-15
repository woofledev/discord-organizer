# configure stuff for each thing here. do NOT share this with anyone.
message_fetcher = {
  "token": "", # your discord ACCOUNT token
  "channelId": "", # the channel id you want to fetch messages from
  "batch": 25, # the batch of messages you want to get (25 works most of the time)
}



# here are the currently implemented models, from the impl folder. you can implement your own too!
# cardiffnlp - is generally pretty good for formal stuff. (cardiffnlp/twitter-roberta-base-sentiment-latest)
# lxyuan - i find this one to be more accurate, pretty good. (lxyuan/distilbert-base-multilingual-cased-sentiments-student)
# samlowe - this one has a LOT of emotions (24-26) and allows for more categorization 
#           and stuff. i like this one. (SamLowe/roberta-base-go_emotions)

categorizer = {
  "model": "lxyuan",  # which model implementation to use
  "stdout": True, # if you want to print out debugging stuff
}