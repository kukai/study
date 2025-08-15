from llama_cpp import Llama
import os

# モデルパスを環境変数から取得、デフォルトは相対パス
model_path = os.getenv("ELYZA_MODEL_PATH", "./models/ELYZA-japanese-Llama-2-7b-fast-instruct-q2_K.gguf")
llm = Llama(model_path = model_path, 
            n_gpu_layers = 1,
            verbose = False)
output = llm("""
富士山の高さは？
""")
# print(output)
print(output['choices'][0]['text'])