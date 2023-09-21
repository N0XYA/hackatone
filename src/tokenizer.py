import re
import pandas as pd
import nltk
import emoji
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pymorphy2

nltk.download("punkt")
nltk.download("stopwords")


def preprocess_text(text):
    text = emoji.demojize(text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r':[a-z_]+:', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[!\"#$%&\'()*+,\-./:;<=>?@[\\]^_`{|}~»«]', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    
    tokens = nltk.word_tokenize(text, language='russian')
    tokens = [token.lower() for token in tokens]

    stop_words = set(stopwords.words('russian'))
    filtered_tokens = [token for token in tokens if token not in stop_words]

    morph = pymorphy2.MorphAnalyzer()
    lemmatized_tokens = [morph.parse(word)[0].normal_form for word in filtered_tokens]

    return ' '.join(lemmatized_tokens)


def tokenize_all(list_str):
    tokens = [preprocess_text(row) for row in list_str]
    return tokens

def get_preprocessed_df(row_count=5):
    print("preprocessing started")

    df = pd.read_csv('data.csv', encoding="utf-8")
    df = df.head(row_count)

    df['text'] = df['text'].astype(str)

    df['text'] = df['text'].apply(preprocess_text)
    df[['text']].to_csv("data_trunked.csv", index=False, encoding="utf-8")

    print("preprocessing ended")
    return df