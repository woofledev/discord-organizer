import json
messages = json.load(open("msgs.json", "r", encoding="utf-8"))
messages = [i for sub in messages for i in sub]  # merge all lists into one
print(f"messages: {len(messages)}")


from config import categorizer
bert = __import__(f"impl.{categorizer['model']}", globals(), locals(), ['nlp']).nlp() # this is ugly but it works
processed, labels = [], set()

for msg in messages:
  content = msg.get("content")
  sentiment = bert(content)[0]
  bestOne = max(sentiment, key=lambda x: x['score'])

  current = {
    "name": msg['author']['username'],
    "msg": content,
    "label": bestOne['label'], "score": bestOne['score']
  }
  processed.append(current)
  labels.add(bestOne['label'])
  if categorizer['stdout']: print(f"from {msg['author']['username']}: {content}, {bestOne}")
#print(processed)



# visualize on mpl
import matplotlib.pyplot as plt
from collections import Counter

allLabels = {label: Counter([msg['name'] for msg in processed if msg['label'] == label]) for label in labels}

def render(title, counts):
  plt.figure(figsize=(12, 8))
  plt.pie(counts.values(), labels=counts.keys(), autopct="%1.1f%%", startangle=140, pctdistance=0.35)
  plt.title(title)
  plt.axis("equal")
  plt.savefig(f"{title}.png")
  # plt.show()
  plt.close()
  return plt

for label, counter in allLabels.items():
  render(f"most {label} users", counter)
