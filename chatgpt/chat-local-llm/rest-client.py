import streamlit as st
import requests
import json


st.write("""
# My first app
Hello *world!*
""")

if st.button('このテキストについての処理を実行'):
    st.write('処理が実行されました。')


import streamlit as st
import requests
import json

# タイトルの設定
st.title('REST API Client')

# ユーザー入力の取得
url = st.text_input('Enter the URL')
request_type = st.selectbox('Request Type', ['GET', 'POST', 'PUT', 'DELETE'])

# 代表的なヘッダーの選択
content_type = st.selectbox('Content-Type', ['', 'application/json', 'application/xml', 'text/plain', 'text/html'])

# カスタムヘッダーの入力
custom_headers = st.text_area('Enter custom headers as JSON', '{}')
try:
    custom_headers = json.loads(custom_headers)
except json.JSONDecodeError:
    st.error("JSON format error in custom headers.")

# ヘッダーの組み立て
headers = {}
if content_type:
    headers['Content-Type'] = content_type
headers.update(custom_headers)

# リクエストパラメーターとボディ
params = st.text_area('Enter parameters as a JSON', '{}')
try:
    params = json.loads(params)
except json.JSONDecodeError:
    st.error("JSON format error in parameters.")

# リクエストボディの入力
if request_type in ['POST', 'PUT']:
    request_body = st.text_area('Enter request body as a JSON', '{}')
    try:
        request_body = json.loads(request_body)
    except json.JSONDecodeError:
        st.error("JSON format error in request body.")
else:
    request_body = None

# リクエストの送信
if st.button('Send Request'):
    if request_type == 'GET':
        response = requests.get(url, params=params, headers=headers)
    elif request_type == 'POST':
        response = requests.post(url, json=request_body, params=params, headers=headers)
    elif request_type == 'PUT':
        response = requests.put(url, json=request_body, params=params, headers=headers)
    elif request_type == 'DELETE':
        response = requests.delete(url, params=params, headers=headers)

    # レスポンスの表示
    st.text('Response:')
    st.write(response.status_code)
    st.write(response.json())
