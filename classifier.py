from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd
import tokenizer
import keyword_lists

category_keywords = {
    "Финансы": keyword_lists.Finances(),
    "Технологии": keyword_lists.Technology(),
    "Политика": keyword_lists.Politics(),
    "Шоубиз": keyword_lists.ShowBussines(),
    "Fashion": keyword_lists.Fashion(),
    "Крипта": keyword_lists.Crypto(),
    "Путешествия/релокация": keyword_lists.Travel(),
    "Образовательный контент": keyword_lists.Education(),
    "Развлечения": keyword_lists.Entertaiment()
}

training_data = []
training_labels= []

for category, keywords in category_keywords.items():
    for keyword in keywords:
        training_data.append(keyword)
        training_labels.append(category)

model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(training_data, training_labels)


# если вероятность категории ниже 0.12, выбирается категория "Общее"
confidence_threshold = 0.12

def classify_text(text):
    probabilities = model.predict_proba([text])[0]
    max_probability = max(probabilities)
    print(probabilities)

    if max_probability < confidence_threshold:
        return "Общее"
    else:
        category = model.predict([text])[0]
        return category

df = tokenizer.get_preprocessed_df(100)
df['category'] = df['preprocessed_text'].apply(classify_text)

output_file = 'output.xlsx'

df[['text', 'preprocessed_text', 'category']].to_excel(output_file, sheet_name="данные", index=False)


