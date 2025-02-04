import requests
url = "https://en.wikipedia.org/w/api.php"

params = {
            "action": "opensearch",
            "search": "book",
            "limit": "10",
            "namespace": "0",
            "format": "json"
        }
response = requests.get(url, params=params)
 
print(response)