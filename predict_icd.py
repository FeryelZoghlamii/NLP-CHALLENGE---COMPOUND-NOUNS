# ==============================================================================
# NLP CHALLENGE : COMPOUND NOUNS
# proposed by   : MIA (Medical Information Analytics)
# Author        : Feryel Zoghlami
# Date          : 01.11.2021
# ==============================================================================


## Imports
import sys
from nltk.tokenize 	import word_tokenize
from nltk.stem 		import PorterStemmer
from nltk.corpus 	import stopwords
from Levenshtein 	import jaro_winkler
from flask 			import Flask, render_template, redirect,url_for, request

## Dataset
compound_nouns  = ['Arterienriss', 'Harnblaseninfektion', 'Klaviculafraktur', 'Ovarialzyste', 'Schädelprellung', 'Schenkelhalsfraktur', 'Zungengrundkarzinom']
ICD_codes       = ['I77.2', 'N30.9', 'S42.00', 'N83.2', 'S00.95', 'S72.00', 'C01']
stop_words      = set(stopwords.words('german'))

# Predict the icd code depending on the user input
def predict_icd(description):
    global compound_nouns, ICD_codes, stop_words

    # The input is one of the compound nouns in the given dataset
    if description in compound_nouns:
        return ICD_codes.index(description)
    
    # The input in a split-up variant of one of the compound noun in the given dataset
    else:
        # Tokenization of the split-up description 
        split_up_token = word_tokenize(description)

        # Remove stop words, in our case "der" and "des" 
        split_up_filtered= [tok for tok in split_up_token if not tok.lower() in stop_words]

        # stemming split-up description words by keeping only root form (base) for each word
        ps = PorterStemmer()
        split_up_lower = [ps.stem(tok).lower() for tok in split_up_filtered]

        # Formulate one word out of the split-up description words
        split_up_final = split_up_lower[1]+split_up_lower[0]

        # calculate matching scores between the input and the compound nouns in the given dataset
        scores = [jaro_winkler(split_up_final, possible.lower()) for possible in compound_nouns]
        
        # return the compound noun with the higher matching score
        return ICD_codes[scores.index(max(scores))]




if __name__ == "__main__":
	ICD_codes = predict_icd(sys.argv[1])
	print(ICD_codes)






