import requests
import json

# ----------SETUP----------
# keeps the token secret in config.json
with open("config.json", "r") as cfg:
	data = json.load(cfg)
token = data["notion_token"]

database_id = "b1f65b437a8f4ee280071c0a5db20d06"
test_page_url = "https://www.notion.so/Read_test-page-742250015e1640baa6056f4d3ffff056"
headers = {"Authorization": "Bearer " + token, "Notion-Version": "2022-06-28"}

# ----------FUNCTIONS----------
def read_database(database_id: str, headers: dict):
	read_url = f"https://api.notion.com/v1/databases/{database_id}/query"

	res = requests.request("POST", read_url, headers=headers)
	data = res.json()
	print(res.status_code)

	with open("./data/db.json", "w", encoding="utf8") as f:
		json.dump(data, f, ensure_ascii=False)

def read_page(test_page_url:str, headers:dict):
	read_url = test_page_url

	res = requests.request("GET", read_url, headers=headers)
	data = res.json()
	print(res.status_code)

	with open("./data/pg.json", "w", encoding="utf8") as f:
		json.dump(data, f, ensure_ascii=False)

def create_page(database_id:str, headers:dict):
	create_url = "https://api.notion.com/v1/pages"
	page_data_new = {

	}
	data = json.dumps(page_data_new)

	res = requests.request("POST", create_url, headers=headers, data=data)

	print(res.status_code)
	print(res.content)

def update_page():
	pass


# ----------PROGRAM----------
#read_database(database_id=database_id, headers=headers)
#create_page(database_id=database_id, headers=headers)
read_page(test_page_url=test_page_url, headers=headers)
