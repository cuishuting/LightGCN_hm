import pandas as pd
import numpy as np
import csv
from pandasql import sqldf
"""
create "item_list.txt" including only the item's original id and re-map id
"""
# item_data = pd.read_csv("../data/hm/articles.csv", header=0)
# item_list = pd.DataFrame(np.asarray(item_data["article_id"]), columns=["org_id"])
# item_list['remap_id'] = item_list.index
# item_list.to_csv(r'../data/hm/item_list.txt', index=None, sep='\t', mode='a')

"""
create "customer_list.txt" including only the customer's original id and re-map id 
(including customers who had at least 10 purchase)
"""
# transactions = pd.read_csv("../data/hm/transactions_train.csv")
# transactions = transactions["customer_id"].value_counts()
# transaction_data = transactions.rename_axis('customer_id').reset_index(name='purchase_counts')
# transaction_data_morethan10 = transaction_data[transaction_data['purchase_counts'] >= 10]
# customer_list = pd.DataFrame(np.asarray(transaction_data_morethan10["customer_id"]), columns=["org_id"])
# customer_list['remap_id'] = customer_list.index
# customer_list.to_csv(r'../data/hm/customer_list.txt', index=None, sep='\t', mode='a')


"""
create train.txt and test.txt. Firstly create the transaction matrix of each customer and their purchase. 
Then randomly select 80% of each customer's transction data as training data
"""
customer_list = pd.read_table('../data/hm/customer_list.txt', sep='\t')
transaction = pd.read_csv("../data/hm/transactions_train.csv", header=0)
new_transaction = pd.DataFrame(transaction, columns=["customer_id", "article_id"])
customer_purchase_detail = sqldf("""SELECT remap_id as customer, article_id 
        FROM customer_list as c
        INNER JOIN new_transaction as t
        on c.org_id = t.customer_id
        group by remap_id, article_id
    """)
print(customer_purchase_detail)





