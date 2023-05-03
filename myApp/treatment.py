import spacy
import re
nlp = spacy.load('en_core_web_sm')

class Display :
    def display_verbs(self,text) :
        values = []
        doc = nlp(text)
        values = [token.lemma_ for token in doc if token.pos_ == 'VERB' ]
        return values
    def display_noun(self,text):
        values = []
        doc = nlp(text)
        values = [token.lemma_ for token in doc if token.pos_ == 'NOUN' ]
        return values
    def display_adj(self,text):
        values = []
        doc = nlp(text)
        values = [token.lemma_ for token in doc if token.pos_ == 'ADJ' ]
        return values
    

    def get_mail(self,text):
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        values = re.findall(pattern, text, flags=re.MULTILINE)
        return values

    def get_number(self,text):
        pattern = r"\+\d{3}[-\s]?\d{8}"
        values = re.findall(pattern, text)
        return values




