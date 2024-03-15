# SamLowe/roberta-base-go_emotions allows for more emotions and stuff
from transformers import pipeline

def nlp():
  model = pipeline("text-classification",
    model="SamLowe/roberta-base-go_emotions",
    return_all_scores=True
  )
  
  wrapper = lambda text: model([text])
  return wrapper