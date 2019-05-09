
#import hive from pyhive
from pyhive import hive
import setuptools
import logging
import pandas as pd
import sys



#establish the connection to the db
# hive.server.thrift.socket.timeout=1000
# hive.client.thrift.socket.timeout=1000

conn = hive.Connection(host='103.14.99.246', port='8889', auth='NOSASL', database='vertoz')
thrift.server.socket.read.timeout
#prepare the cursor for the queries
cursor = conn.cursor()

logging.basicConfig(level=logging.DEBUG)

#execute a query
# cursor.execute("SHOW TABLES")
df = pd.read_sql("Show Tables",conn)
print(sys.getsizeof(df))
df.head()

#navigate and display the results
for table in cursor.fetchall():
    print(table)