# Notes

First things first, you have to create and register your app with reddit by following [these steps.](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)

```python
import requests
import requests.auth
client_auth = requests.auth.HTTPBasicAuth('RiAlAzjZFIBxrg', 'm0U4CQlncXooEnoQn-l0jREYhB13oQ')
post_data = {"grant_type": "password", "username": "slash64-api", "password": "pay1SEFT-toft6stid"}
headers = {"User-Agent": "redditmon/0.1 by slash64-api"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

print(response.json())
```

https://packaging.python.org/tutorials/packaging-projects/
