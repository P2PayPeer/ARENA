# oniimaid.py

from common import load_model, generate_text

class OniiMaid:
    def __init__(self, model_name):
        self.model, self.tokenizer = load_model(model_name)

    def respond_to_prompt(self, prompt):
        return generate_text(self.model, self.tokenizer, prompt)

# Usage
# oniimaid = OniiMaid('model_name_here')
# response = oniimaid.respond_to_prompt("Hello, OniiMaid!")

# Models
# https://huggingface.co/Undi95/OniiMaid-alpha-13B-GGUF/

# https://huggingface.co/Undi95/OniiMaid-alpha-13B-GGUF/resolve/main/OniiMaid-alpha-13B.q4_k_s.gguf
# https://huggingface.co/Undi95/OniiMaid-alpha-13B-GGUF/resolve/main/OniiMaid-alpha-13B.q5_k_m.gguf
# https://huggingface.co/Undi95/OniiMaid-alpha-13B-GGUF/resolve/main/OniiMaid-alpha-13B.q6_k.gguf
# https://huggingface.co/Undi95/OniiMaid-alpha-13B-GGUF/resolve/main/OniiMaid-alpha-13B.q8_0.gguf
