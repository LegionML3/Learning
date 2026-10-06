import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix
# Download latest version
df = pd.read_csv(r"C:\Users\user\Desktop\Common FIles\Datasets\email_spam.csv")
print(df.columns)

df['title'] = df['title'].fillna('')
df['text'] = df['text'].fillna('')
df['combined_text'] = df['title'] + " " + df['text']

df['label'] = df['type'].map({
    'not spam': 0,
    'spam': 1
})
X = df['text']
y = df['label']

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.3)

vectorizer = TfidfVectorizer()
vec_train_x = vectorizer.fit_transform(train_x)
vec_test_x = vectorizer.transform(test_x)

model = LogisticRegression(max_iter=10000)
model.fit(vec_train_x, train_y)

predictions = model.predict(vec_test_x)
confusion_matrix = confusion_matrix(test_y, predictions)

print(confusion_matrix)



