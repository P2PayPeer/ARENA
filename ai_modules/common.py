# common.py 

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model(model_name):
    """
    Load a model and its tokenizer from Hugging Face.

    Args:
    - model_name (str): The name of the model on Hugging Face.

    Returns:
    - model: The loaded model.
    - tokenizer: The tokenizer for the model.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def generate_text(model, tokenizer, prompt, max_length=50):
    """
    Generate text using the model.

    Args:
    - model: The language model.
    - tokenizer: The tokenizer for the model.
    - prompt (str): Starting text for generation.
    - max_length (int): Maximum length for the generated text.

    Returns:
    - generated_text (str): The text generated by the model.
    """
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=max_length)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

if __name__ == '__main__':
    model, tokenizer = load_model("gpt2")
    prompt = ""
    generated_text = generate_text(model, tokenizer, prompt)[len(prompt):]

    print(generated_text)

