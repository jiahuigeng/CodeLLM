import os
import torch
import openai
from openai import OpenAI
from transformers import AutoModelForCausalLM, AutoTokenizer
from api_resource import *




# from transformers import AutoModelForCausalLM, AutoTokenizer


def get_codemodel(model_name):
    #  device = "cuda"
    if model_name == "starcoder_3b":
        checkpoint = "bigcode/starcoder2-3b"
        
    elif model_name == "starcoder_7b":
        checkpoint = "bigcode/starcoder2-3b"
        
    elif model_name == "codellama":
        checkpoint = "codellama/CodeLlama-7b-Instruct-hf"

    elif model_name == "qwen":
        checkpoint = "Qwen/Qwen2.5-Coder-7B-Instruct"
        
    elif model_name == "deepseeker":
        checkpoint = "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"
        
    
    tokenizer = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True)
    if model_name in ['starcoder_7b', 'qwen']:
        model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True, torch_dtype=torch.bfloat16).cuda()
    else: 
        model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True,).cuda()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # model = model.to(device)

    
    prompt = "def fibonacci(n):\n"

    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    # Generate code completion
    output = model.generate(
        inputs.input_ids, 
        max_length=100,  # Adjust the max_length as needed
        num_return_sequences=1,  # Adjust how many sequences you want to generate
        temperature=0.8,  # Optional: tune this parameter to control randomness
        top_p=0.95,  # Optional: top-p sampling for diversity
    )

    # Decode the generated tokens back to text
    generated_code = tokenizer.decode(output[0], skip_special_tokens=True)

    print("Generated Code:\n", generated_code)
    
    return tokenizer, model

def get_gpt_model():
    client = OpenAI(api_key=OPENAI_API) 
    return client

def prompt_gpt(client,prompt):
    
    # Make a request to GPT-4
    MODEL = "gpt-4o"
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    results = completion.choices[0].message.content
    print("Assistant: ", results)
    return results

    
if __name__ == "__main__":
    # prompt_gpt("what is 1 + 2?")
    # print("starcoder")
    get_codemodel('starcoder_7b')
    print("deepseeker")
    get_codemodel('deepseeker')
    
    # print("codellama")
    # get_codemodel('codellama')
    # print("qwen")
    # get_codemodel('qwen')
    
    
    

