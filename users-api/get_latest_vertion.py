import json

json_data = '''{
    "count": 1,
    "results": [
        {
            "name": "0.0.2",
            "repository": 26690759,
            "full_size": 93886610,
            "images": [
                {
                    "architecture": "amd64",
                    "digest": "sha256:410083298a7cb28925c445ff5ef2311902ac94df11adfcc0d9e1560df4d182b6",
                    "os": "linux"
                }
            ]
        }
    ]
}'''

data = json.loads(json_data)

# Просто выводим версию, без лишнего текста
print(data['results'][0]['name'])

