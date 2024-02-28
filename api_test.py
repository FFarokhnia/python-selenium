import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com/"

# exercise 1
# response = requests.get(BASE_URL)
# res_status_code = response.status_code
# res_header = response.headers
# print(f'Status Code : {res_status_code}')
# print(f'Response Headers : {res_header}')
# print(f'Response Body : {response.content}')

# Example 1-1
# url = f'{BASE_URL}/users/1'
# response = requests.get(url=url)
# resp_status_code = response.status_code
# resp_header = response.headers
# resp_body = response.content
# print(f'Status Code : {resp_status_code}')
# print(f'Response Headers : {resp_header}')
# print(f'response content type : {resp_header["Content-Type"]}')
# print(f'Response Body : {resp_body}')
# print(f'Formated Response Body : {json.dumps(response.json(),indent=4)}')

# Example 1-2
# url = f'{BASE_URL}/posts/1/comments'
# response = requests.get(url=url)
# resp_status_code = response.status_code
# resp_header = response.headers
# resp_body = response.content
# print(f'Status Code : {resp_status_code}')
# print(f'Response Headers : {resp_header}')
# print(f'response content type : {resp_header["Content-Type"]}')
# print(f'Response Body : {resp_body}')
# print(f'Formated Response Body : {json.dumps(response.json(),indent=4)}')

# Example 1-3
url = f'{BASE_URL}/posts'
payload= {
    "userid": 1,
    "fff": "new post title foroogh",
    "body": "new post body foroogh"
}
response = requests.post(url=url, json=payload)
print(response.json())
print(response.status_code)