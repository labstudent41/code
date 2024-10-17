from pandas import read_csv, DataFrame
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

df = read_csv('GroceryStoreDataSet.csv', names=['products'])
data = list(df["products"].apply(lambda x: x.split(',')))

a = TransactionEncoder()
a_data = a.fit(data).transform(data)

df = DataFrame(a_data, columns=a.columns_).replace(False, 0)
df = apriori(df, min_support=0.2, use_colnames=True, verbose=1)
df_ar = association_rules(df, metric="confidence", min_threshold=0.6)
print(df_ar)
