# template
# 1. DATASETS: Grab your data
from sklearn.datasets import load_digits

# 2. PREP/SPLIT: Cut it into training and testing chunks
from sklearn.model_selection import train_test_split

# 3. MODELS: Pick your brain
from sklearn.linear_model import LogisticRegression

# 4. METRICS: Grab your scorekeeping tools
from sklearn.metrics import confusion_matrix, classification_report

# --- Quick setup ---
digits = load_digits()
X, y = digits.data, digits.target
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=10000)
model.fit(x_train, y_train)
predictions = model.predict(x_test)

# --- Evaluate ---
print(confusion_matrix(y_test, predictions))