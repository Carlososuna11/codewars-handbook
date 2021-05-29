import string
from collections import Counter
def top_3_words(text):
    to_delete = set(string.punctuation) - {"'"} # remove comma and fullstop
    clean_tokens = ''.join(x.lower() if x not in to_delete else "," for x in text ).strip().replace(' ',',').replace('\n','')
    words = clean_tokens.split(',')
    words = list(filter(lambda x: x!="'"*len(x) and x!='',words))
    z = Counter(words).most_common(3)
    return [x[0] for x in z]