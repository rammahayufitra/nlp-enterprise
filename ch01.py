import spacy

print("------------- part 1 ---------------------------")
nlp = spacy.load("en_core_web_sm")
print("nlp: ", nlp)

print("------------- part 1 Tokenizer -----------------")
sentence = nlp.tokenizer("We live in Paris.")
# Length of sentence
print("The number of tokens: ", len(sentence))
# Print individual words (i.e., tokens)
print("The tokens: ")
for words in sentence:
    print(words)

print("------------- part 1 Tokenizer is more-----------------")
import pandas as pd
import os
cwd = os.getcwd()
# Import Jeopardy Questions
data = pd.read_csv(cwd+'/data/jeopardy_questions.csv')
data = pd.DataFrame(data=data)
print(data)