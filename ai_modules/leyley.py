# leyley.py 

from common import load_model, generate_text

class Leyley:
    def __init__(self, model_name):
        self.model, self.tokenizer = load_model(model_name)

    def respond_to_prompt(self, prompt):
        return generate_text(self.model, self.tokenizer, prompt)

# Usage
# leyley = Leyley('model_name_here')
# response = leyley.respond_to_prompt("Hello, Leyley!")

# Models  
# https://huggingface.co/Undi95/Leyley-13B

# https://huggingface.co/Undi95/Leyley-13B-GGUF/resolve/main/Leyley-13B-09.q5_k_m.gguf
# https://huggingface.co/Undi95/Leyley-13B-GGUF/resolve/main/Leyley-13B-09.q8_0.gguf 
