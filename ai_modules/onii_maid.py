# onii_maid.py

from common import load_model, generate_text

class OniiMaid:
    def __init__(self, model_name):
        self.model, self.tokenizer = load_model(model_name)

    def respond_to_prompt(self, prompt):
        return generate_text(self.model, self.tokenizer, prompt)

# Usage
# onii_maid = OniiMaid('model_name_here')
# response = onii_maid.respond_to_prompt("Hello, OniiMaid!")
