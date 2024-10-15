from transformers import BartForConditionalGeneration, BartTokenizer

class Summarizer:
    def __init__(self):
        self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
        self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

    def summarize(self, text):
        inputs = self.tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
        summary_ids = self.model.generate(inputs['input_ids'], num_beams=4, max_length=200, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

summarizer = Summarizer()
