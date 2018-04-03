BUCKET_NAME = "cbse"
STOCKS_FILE="nasdaq.csv"
# The list of nodes to use as 'AWS' nodes
AWS_NODES = ["10.142.180.101", "10.142.180.102"]
# The list of nodes to use as 'Azure' nodes
AZURE_NODES = [""]
# Whether the current cluster is on AWS
AWS = True
# Username of the data user
USERNAME = "Administrator"
# Password of the data user
PASSWORD = "password"
# Administrator username
ADMIN_USER = "Administrator"
# Administrator password
ADMIN_PASS = "password"
# Name of the design doc
DDOC_NAME = "orders"
# Name of the view
VIEW_NAME = "by_timestamp"
# Doc containing all stocks. 
# Single field called "symbols" which is a list containing all product keys.
PRODUCT_LIST="stock_list"
# How many stocks should we use?
NUM_STOCKS=20