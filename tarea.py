import pandas as pd


def jaccard_similarity(set1, set2):
    # Computa la similitud de Jaccard entre dos sets
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)


dataframe = pd.read_csv('tweets_2022_abril_junio.csv')
dataframe = dataframe.dropna(subset=['text'])

tweets = {}

# Recorrer el DataFrame y agregar los IDs y retweet_count al diccionario
for index, row in dataframe.iterrows():
    id_tweet = row['id']
    text = row['text'].split(":")[1:]
    text = ":".join(text)
    tweets[id_tweet] = text


tweets_shingles = {}
k = 3

# iteramos sobre todas las odas
for (name, text) in tweets.items():

    tweets_shingles[name] = set()

    for i in range(len(text) - k-1):
        shingle = text[i:i+k]
        tweets_shingles[name].add(shingle)

print(tweets_shingles)
