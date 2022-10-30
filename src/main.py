import requests
import json

# ----------SETUP----------
# keeps the token secret in config.json
with open("config.json", "r") as cfg:
	data = json.load(cfg)
token = data["notion_token"]

database_id = "b1f65b437a8f4ee280071c0a5db20d06"

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

def read_page(page_id:str, headers:dict):
	read_url = f"https://api.notion.com/v1/pages/{page_id}"

	res = requests.request(method="GET", url=read_url, headers=headers)
	data = res.json()
	print(res.status_code)

	with open("./data/pg.json", "w", encoding="utf8") as f:
		json.dump(data, f, ensure_ascii=False)

def create_page(database_id:str, headers:dict):
	create_url = "https://api.notion.com/v1/pages"
	page_data_new = {
	"parent": { "database_id": database_id },
	"icon": {
		"emoji": "🥬"
	},
		"cover": {
			"external": {
				"url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
			}
		},
		"properties": {
			"Name": {
				"title": [
					{
						"text": {
							"content": "Tuscan Kale"
						}
					}
				]
			},
			"Description": {
				"rich_text": [
					{
						"text": {
							"content": "A dark green leafy vegetable"
						}
					}
				]
			},
			"Tags": {
				"select": {
					"name": "Vegetable"
				}
			},
			"Price": { "number": 2.5 }
		},
		"children": [
			{
				"object": "block",
				"type": "heading_2",
				"heading_2": {
					"rich_text": [{ "type": "text", "text": { "content": "Lacinato kale" } }]
				}
			},
			{
				"object": "block",
				"type": "paragraph",
				"paragraph": {
					"rich_text": [
						{
							"type": "text",
							"text": {
								"content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
								"link": { "url": "https://en.wikipedia.org/wiki/Lacinato_kale" }
							}
						}
					]
				}
			}
		]
	}
	data = json.dumps(page_data_new)

	res = requests.request("POST", create_url, headers=headers, data=data)

	print(res.status_code)
	print(res.content)

# ----------PROGRAM----------
