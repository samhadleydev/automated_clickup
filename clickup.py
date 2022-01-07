import requests
import json

headers = {'Content-Type': 'application/json'}

url = "https://private-anon-52235c7af1-clickup20.apiary-mock.com/api/v2/list/list_id/task?archived=false&page=&order_by=&reverse=&subtasks=&statuses%5B%5D=&include_closed=&assignees%5B%5D=&due_date_gt=&due_date_lt=&date_created_gt=&date_created_lt=&date_updated_gt=&date_updated_lt=&custom_fields%5B%5D="

response = requests.get(url, headers=headers)

response_text = response.text

response_json = json.loads(response_text) 

print(type(response_json))