# logger.py
import requests
import json
from datetime import datetime
import os
class Logger:
def __init__(self, service,logs_url,log_index,transaction_id,user_id):
self.service = service
self.url = logs_url
self.log_index = log_index
self.user_id = user_id
self.transaction_id = transaction_id
def log(self, message,log_level='INFO', error_details=None, additional_data={}):
obj = {
'timestamp': datetime.now().isoformat(),
'service': self.service,'instance': self.log_index,
'userId': self.user_id,
'transactionId': self.transaction_id,
'logLevel': log_level,
'message': message,
'errorDetails': error_details,
'additionalData': additional_data,
}
print(obj)
try:
response = requests.post(self.url, json=obj, headers={'Content-Type': 'application/json'})
response.raise_for_status()
print('Log successfully sent')
except Exception as e:
print(f'Error sending log: {e}')
if __name__ == '__main__':
log_index = 'disearch-app'
logger =
Logger(service='testing',logs_url='http://34.29.169.192:24224/myapp.logs',log_index=log_index,transaction_i
d='123',user_id='my_user')
logger.log('logs from Hassan Bashir disearchmt-dev')
1. Configuration of Logging in Application:
Define a Logger class with methods to log messages and send them to the specified endpoint.
Configure the logger to include necessary details such as timestamp, service, log level, message,
etc.
Instantiate the logger object with appropriate parameters like service name, endpoint URL, log
index, transaction ID, and user ID.
