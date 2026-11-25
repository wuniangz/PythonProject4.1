import os
from dotenv import load_dotenv
import pytest
import requests
load_dotenv()
user_id = os.getenv("MYUSER_ID")
secret_key = os.getenv("MYx_api_key")
# print(user_id)1
from utils.excel_read import get_data
dataed = get_data()
print(dataed)
print("断点")
# @pytest.mark.parametrize("case", dataed)
def test_request():
    # print(case)
    method = dataed[0]["method"]
    url = dataed[0]['url']
    params = dataed[0]["params"]
    data = dataed[0]["data"]
    headers = dataed[0]["headers"]
    if isinstance(headers, str):
        headers = eval(headers)
    # print(case['jsondata'])
    # print(type(case['jsondata']))
    # if case["jsondata"]:
    #     for key, value in eval(case["jsondata"]).items():
    #         print(key, value)
    request_data = {
        "method": method,
        "url": url.replace("{user_id}", user_id),
        "params": params,
        "data": data,
        "headers": headers
        }
    # print(request_data)
    response = requests.request(**request_data)
    # print(response.text)
    # print(dataed[0]["check"])
    # print(response.json())
    # print(response.json()['data']['note'])
    # print(type(response.json()['data']["note"]))
    print(type(response.json()['data']["note"]))
    print(type(dataed[0]["check"]))
    print(dataed[0]["check"])
    print(response.json()['data']["note"])
    assert dataed[0]["check"] in response.json()['data']["note"]








# data = [
#     {
#         "method":"post",
#         "url": f"https://reqres.in/api/app-users/{user_id}/sessions/simulate",
#         "params":None,
#         "data":None,
#         "json":None,
#         "headers":{}
#     },
#     {
#         "method":"get",
#         "url": "https://reqres.in/app/collections/products/records",
#         "params":None,
#         "data":None,
#         "json":None,
#         "headers":{},
#
#     }
#         ]

# print(data[0]["url"])