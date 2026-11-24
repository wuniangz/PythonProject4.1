import os
from dotenv import load_dotenv

# 加载同目录下的 .env 文件
load_dotenv()

user_id = os.getenv("MYUSER_ID")
secret_key = os.getenv("MYx_api_key")


import pytest
import requests

from utils.excel_read import get_data

# from utils.excel_read import get_data


data = [
    {
        "method":"post",
        "url": f"https://reqres.in/api/app-users/{user_id}/sessions/simulate",
        "params":None,
        "data":None,
        "json":None,
        "headers":{}
    },
    {
        "method":"get",
        "url": "https://reqres.in/app/collections/products/records",
        "params":None,
        "data":None,
        "json":None,
        "headers":{},

    }
        ]

print(data[0]["url"])

# dataed = get_data()
# print(dataed)



# @pytest.mark.parametrize("case", dataed)
# def test_request(case):
#     method = case["method"]
#     url = case["url"]
#     params = case["params"]
#     data = case["data"]
#     headers = case["headers"]
#     if isinstance(headers, str):
#         headers = eval(headers)
#     if isinstance(headers, str):
#         headers = eval(headers)
#
#     login_data = {
#         "method": method,
#         "url": url,
#         "params": params,
#         "data": data,
#         "headers": headers
#     }
#     requests.request(**login_data)