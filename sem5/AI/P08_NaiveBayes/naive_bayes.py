from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)


iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                        test_size=0.3, random_state=0)
clf = GaussianNB()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("Test Precision (macro):", precision_score(y_test, y_pred, average='macro'))
print("Recall Score (macro):", recall_score(y_test, y_pred, average='macro'))
print("F1 Score (macro):", f1_score(y_test, y_pred, average='macro'))

print("\nClassification Report :-\n",
      classification_report(y_test, y_pred))
