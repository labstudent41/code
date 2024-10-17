from pandas import read_csv
from six import StringIO
from pydotplus import graph_from_dot_data

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

col_names = ["Reservation", "Raining", "Bad Service", "Saturday", "Results"]
features = col_names[:-1]
target = col_names[-1]

df = read_csv('hoteldata.csv', header=None, names=col_names)
x = df[features]
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                test_size=0.3, random_state=1)

clf = DecisionTreeClassifier(criterion="entropy", max_depth=5)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, feature_names=features,
                class_names=["Leave", "Wait"], filled=True, rounded=True)

graph = graph_from_dot_data(dot_data.getvalue())
graph.write('hotel.png', format='png')
