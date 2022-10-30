import requests
import json

# ----------SETUP----------
# keeps the token secret in config.json
with open("config.json", "r") as cfg:
	data = json.load(cfg)
token = data["notion_token"]

database_id = "b1f65b437a8f4ee280071c0a5db20d06"
test_page_id = "74225001-5e16-40ba-a605-6f4d3ffff056"

headers = {
	"Authorization": "Bearer " + token, 
    "Content-Type": "application/json",
	"Notion-Version": "2022-06-28"
}

# ----------FUNCTIONS----------
def read_database(database_id: str, headers: dict):
	read_url = f"https://api.notion.com/v1/databases/{database_id}/query"

	res = requests.request(method="POST", url=read_url, headers=headers)
	data = res.json()
	print(res.status_code)

	with open("./data/db.json", "w", encoding="utf8") as f:
		json.dump(data, f, ensure_ascii=False)

""" def read_page(page_id:str, headers:dict):
	read_url = f"https://api.notion.com/v1/pages/{page_id}"

	res = requests.request(method="GET", url=read_url, headers=headers)
	data = res.json()
	print(res.status_code)

	with open("./data/pg.json", "w", encoding="utf8") as f:
		json.dump(data, f, ensure_ascii=False) """

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
create_page(database_id=database_id, headers=headers)
