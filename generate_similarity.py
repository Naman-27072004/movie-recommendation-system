import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading movies_dict.pkl...")
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
df = pd.DataFrame(movies_dict)

print("Calculating count vectors...")
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['tags']).toarray()

print("Calculating cosine similarity...")
similarity = cosine_similarity(vectors)

print("Saving similarity.pkl...")
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("Completed successfully!")
