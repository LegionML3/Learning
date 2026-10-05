import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
# Download latest version
df = pd.read_csv(r"C:\Users\user\Desktop\Common FIles\Datasets\email_spam.csv")
print(df.columns)

X = df['text']
y = df['type']

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=10000)
model.fit(train_x, train_y)

predictions = model.predict(test_x)
confusion_matrix = confusion_matrix(test_y, predictions)
print(confusion_matrix)



