# LightGCN_hm
hm products' recommendation through LightGCN model
Before training the LightGCN model on hm dataset, remember to unzip file "train.txt.zip"
"data/hm/item_list.txt" including all the products' org_id and remap_id
"data/hm/user_list.txt" including all the customers' org_id and remap_id 
"data/hm/train.txt" including 80% of all the transaction records(including all the customers having 5 or more transaction records)
"data/hm/test.txt" including the left 20% of all the transaction records(including all the customers having 5 or more transaction records)
"data/hm/transaction_list_more_10.ipynb" is all the data processing code according to the original datasets: "articles.csv", "customers.csv" and "transactions_train.csv" downloaded from Kaggle: "https://www.kaggle.com/c/h-and-m-personalized-fashion-recommendations/data"