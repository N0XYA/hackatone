import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

df = pd.read_excel("training_data.xlsx")
list_of_titles = df["text"].to_list()
# print(list_of_titles[50])
# print(list_of_titles[60])

result = []
line = "Российское правительство"
line2 = "Москва дорожит братскими отношениями с Ереваном, которые носят стратегический и союзнический характер, заявил премьер-министр РФ Михаил Мишустин."
for i in range(len(list_of_titles)):
    a = fuzz.token_set_ratio(line, list_of_titles[i])
    b = fuzz.token_set_ratio(line2, list_of_titles[i])
    if a > 50:
        # result.append(line)
        result.append(list_of_titles[i])

    if b > 50:
        # result.append(list_of_titles[i])
        pass
for raw in result:
    print(raw)
    print("================================================================================================")
print(len(result))