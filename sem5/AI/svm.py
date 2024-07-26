import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
print("Features:-\n%s\n" % iris["feature_names"])

df = pd.DataFrame(iris["data"], columns=iris["feature_names"])
print(df.head())

x = df
y = iris["target"]
print("\n=== x ===\n", x)
print("\n=== y ===\n", y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.3,
                                                    random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.svm import SVC
svc_clf = SVC(kernel='linear', random_state=0)
svc_clf.fit(x_train, y_train)

y_pred = svc_clf.predict(x_test)
print("\nY Prediction :-\n%s\n" %y_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix :-\n%s\n" %cm)

from sklearn.metrics import accuracy_score, classification_report
print("\nAccuracy :-\n%s\n" %accuracy_score(y_test, y_pred))
print("\nClassification Report :-\n%s\n" %classification_report(y_test, y_pred))
