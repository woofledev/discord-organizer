from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def nlp():
  tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
  model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
  return pipeline("sentiment-analysis", 
      model=model, tokenizer=tokenizer,
      return_all_scores=True
  )