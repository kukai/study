from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import SimpleMemory
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import SimpleMemory
from langchain.prompts import PromptTemplate
import openai
from langchain.llms import OpenAI

# OpenAI APIキーの設定
# openai.api_key = st.secrets["OPENAI_API_KEY"]

# LangChainの設定
llm = OpenAI(model="gpt-4")
memory = SimpleMemory()  # 会話の履歴を記憶するメモリオブジェクト

# プロンプトテンプレートの設定
prompt_template = PromptTemplate.from_template("""
{history}
You are a helpful assistant. Respond to the following input thoughtfully.
Input: {input}
""")

conversation_chain = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt_template,
    input_variables=["history", "input"],  # 正しい入力変数を設定
    output_key="response"  # 応答キーを設定
)

def get_response(user_input):
    # LangChainを使用して会話を続ける
    response = conversation_chain.run(input=user_input)
    return response

def main():
    st.title('対話型AIチャット with LangChain')

    user_input = st.text_input("メッセージを入力してください:")

    if st.button('返信を生成'):
        response = get_response(user_input)
        st.text_area("AIの返信:", value=response, height=200)

        # JavaScriptを使った読み上げボタンの追加
        st.markdown(f"""
            <button onclick="const utterance = new SpeechSynthesisUtterance('{response}');
            speechSynthesis.speak(utterance);">
            レスポンスを読み上げる
            </button>
        """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
