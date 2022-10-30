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

def create_page(database_id:str, headers:dict, page_content:dict):
	create_url = "https://api.notion.com/v1/pages"
	data = json.dumps(page_content)

	res = requests.request("POST", create_url, headers=headers, data=data)

	print(res.status_code)
	print(res.content)

# ----------PROGRAM----------
read_page("f362fa40-177b-4324-ba6e-cb85da09af4e", headers)

page_content = {
    "object": "page",
    "id": "f362fa40-177b-4324-ba6e-cb85da09af4e",
    "created_time": "2022-10-30T22:27:00.000Z",
    "last_edited_time": "2022-10-30T23:18:00.000Z",
    "created_by": {
        "object": "user",
        "id": "1735f0bd-d9a6-40e3-9780-de77c88e145a"
    },
    "last_edited_by": {
        "object": "user",
        "id": "1735f0bd-d9a6-40e3-9780-de77c88e145a"
    },
    "cover": null,
    "icon": null,
    "parent": {
        "type": "database_id",
        "database_id": "b1f65b43-7a8f-4ee2-8007-1c0a5db20d06"
    },
    "archived": false,
    "properties": {
        "Source": {
            "id": "%40NFs",
            "type": "select",
            "select": {
                "id": "21d13b6f-e744-4511-b1d4-59f28e1e5eae",
                "name": "Marc Krueger",
                "color": "green"
            }
        },
        "Day": {
            "id": "DtR%3E",
            "type": "select",
            "select": {
                "id": "UnUD",
                "name": "#TuesdayQuiz",
                "color": "purple"
            }
        },
        "Status": {
            "id": "_kmJ",
            "type": "status",
            "status": {
                "id": "f11ee725-5d9c-4acf-a0ad-7478e2f22f31",
                "name": "Not started",
                "color": "default"
            }
        },
        "Name": {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Tuesday 25 October 2022",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Tuesday 25 October 2022",
                    "href": null
                }
            ]
        }
    },
    "url": "https://www.notion.so/Tuesday-25-October-2022-f362fa40177b4324ba6ecb85da09af4e"
}