import re 

def clean_text(text):
    #remove html tags 
    text = re.sub(r'<[^>]+>', '', text)
    #remove urls 
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    #remove special characters 
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    #replace multiple spaces with single space 
    text = re.sub(r'\s+', ' ', text).strip()
    #trim leading and trailing whitespace 
    text = text.strip()
    return text 