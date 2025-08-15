from langchain.llms import LlamaCpp

llm = LlamaCpp(
    model_path = "./Downloads/ELYZA-japanese-Llama-2-7b-fast-instruct-q2_K.gguf",
    temperature=0.2,
    max_tokens=100,
    n_gpu_layers = 1,
    verbose = False,
    
)

output = llm("""
地球の半径は？
""")
print(output)