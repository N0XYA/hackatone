import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
import torch

categories = {
    'Блоги': ['личный', 'блоггер', 'дневник', 'отзывы'],
    'Новости и СМИ': ['новости', 'медиа', 'журналистика', 'пресса'],
    'Развлечения и юмор': ['юмор', 'развлечения', 'шутки', 'комедия'],
    'Технологии': ['техника', 'инновации', 'it', 'сайты'],
    'Экономика': ['финансы', 'экономический', 'рынок', 'инвестиции'],
    'Бизнес и стартапы': ['предпринимательство', 'стартап', 'бизнес', 'стратегия'],
    'Криптовалюты': ['биткоин', 'эфириум', 'криптовалютный', 'blockchain'],
    'Путешествия': ['туризм', 'путешественники', 'отпуск', 'города'],
    'Маркетинг, PR, реклама': ['маркетинг', 'pr', 'реклама', 'бренд'],
    'Психология': ['психологический', 'эмоции', 'психотерапия', 'исследования'],
    'Дизайн': ['графический', 'веб', 'искусство', 'дизайн', 'интерьер'],
    'Политика': ['политика', 'америка', 'украина', 'россия', 'путин', 'байден'],
    'Искусство': ['живопись', 'скульптура', 'искусство', 'художники'],
    'Право': ['юридические', 'законы', 'судебные', 'решения'],
    'Образование и познавательное': ['образовательные', 'университеты', 'наука', 'исследования'],
    'Спорт': ['футбол', 'баскетбол', 'теннис', 'спортивные'],
    'Мода и красота': ['модные', 'красота', 'дизайн', 'модельеры'],
    'Здоровье и медицина': ['здоровый', 'медицинские', 'болезни', 'медицинское'],
    'Картинки и фото': ['изображения', 'фотографии', 'графика', 'фотогалереи'],
    'Софт и приложения': ['программное', 'мобильные', 'разработка', 'техническая'],
    'Видео и фильмы': ['видеоматериалы', 'кино', 'сериалы', 'фильмы'],
    'Музыка': ['музыкальные', 'артисты', 'концерты', 'альбомы'],
    'Игры': ['видеоигры', 'игровые', 'индустрия', 'гейминг'],
    'Еда и кулинария': ['рецепты', 'кулинарные', 'еда', 'рестораны'],
    'Цитаты': ['цитаты', 'мудрые', 'вдохновение', 'жизни'],
    'Рукоделие': ['хобби', 'творчество', 'рукодельные', 'искусство'],
    'Финансы': ['личные', 'инвестиции', 'бюджетирование', 'советы'],
    'Шоубиз': ['знаменитости', 'шоу', 'голливуд', 'кино']
}


def compute_word_embedding(word):
    input_ids = tokenizer.encode(word, return_tensors='pt', max_length=512, truncation=True)
    with torch.no_grad():
        output = model(input_ids)
    return output.last_hidden_state.mean(dim=1).squeeze().numpy()


category_keyword_embeddings = {}
for categ, keywords in categories.items():
    keyword_embeddings = np.array([compute_word_embedding(keyword) for keyword in keywords])
    category_keyword_embeddings[categ] = keyword_embeddings.mean(axis=0)
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
model = AutoModel.from_pretrained("bert-base-multilingual-cased")


def classify_text(input_text):
    input_words = input_text.split()
    category_scores = {category: 0 for category in categories}

    for word in input_words:
        word_embedding = compute_word_embedding(word)
        for category, keyword_embedding in category_keyword_embeddings.items():
            similarity = cosine_similarity(word_embedding.reshape(1, -1), keyword_embedding.reshape(1, -1))[0][0]
            category_scores[category] += similarity

    predicted_category = max(category_scores, key=category_scores.get)
    return predicted_category


def classify_all(list_str):
    predicted_categories = [classify_text(row) for row in list_str]
    return predicted_categories
