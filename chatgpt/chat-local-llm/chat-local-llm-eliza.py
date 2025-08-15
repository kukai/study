import streamlit as st
import requests
import json

# Streamlitページの設定
st.title('Llama2 APIとの対話')

# ユーザー入力
user_input = st.text_input("質問を入力してください:")

# リクエストと応答処理

if user_input:
    url = "http://localhost:8080/completion"
    headers = {'Content-Type': 'application/json'}
    data = {
        "prompt": user_input,
        "n_predict": 1024
    }

    # APIリクエストを送信
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)

    # 応答表示用のプレースホルダーを作成
    response_placeholder = st.empty()
    
    # ストリーム応答の処理
    if response.status_code == 200:
        last_response = ""
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                json_response = json.loads(decoded_line)
                if 'content' in json_response:
                    current_response = json_response['content']
                    last_response += current_response
                    response_placeholder.write(last_response)
    else:
        st.error("APIからの応答に問題があります。")
