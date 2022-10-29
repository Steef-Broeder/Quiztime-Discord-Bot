import requests
import json

#----------SETUP----------
#keeps the token secret in config.json
with open('config.json', 'r') as cfg:
  data = json.load(cfg) 
token = data["notion_token"]

database_id = 'b1f65b437a8f4ee280071c0a5db20d06'
headers = {
    'Authorization': 'Bearer ' + token,
    'Notion-Version': '2022-06-28'
}

#----------FUNCTIONS----------
def read_database(database_id:str, headers:dict):
    read_url = f'https://api.notion.com/v1/databases/{database_id}/query'
    
    res = requests.request('POST', read_url, headers=headers)
    data = res.json()
    print(res.status_code)

    with open('./data/db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    

def create_page():
    pass

def update_page():
    pass

#----------PROGRAM----------
read_database(database_id=database_id, headers=headers) #json object is written to db.json

