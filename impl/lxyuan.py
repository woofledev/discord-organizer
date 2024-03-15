from transformers import pipeline

def nlp():
  return pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
    return_all_scores=True
  )