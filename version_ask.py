from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigcode/starcoder2-3b"
device = "cuda"

libs = ['numpy', '']
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# for multiple GPUs install accelerate and do `model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto")`
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

# import ipdb; ipdb.set_trace()

prompt = "def print_hello_world():"
inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs, pad_token_id=tokenizer.eos_token_id,eos_token_id=tokenizer.eos_token_id)
print(f"USER: {prompt}")
print(f"BOT: {tokenizer.decode(outputs[0])}")
print("--------------------------------------------------------------------------------")

prompt = "show me the numpy version you knows"
inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs, pad_token_id=tokenizer.eos_token_id,eos_token_id=tokenizer.eos_token_id)
print(f"USER: {prompt}")
print(f"BOT: {tokenizer.decode(outputs[0])}")
print("--------------------------------------------------------------------------------")

prompt = "what's the latest numpy version"
inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs, pad_token_id=tokenizer.eos_token_id,eos_token_id=tokenizer.eos_token_id)
print(f"USER: {prompt}")
print(f"BOT: {tokenizer.decode(outputs[0])}")
print("--------------------------------------------------------------------------------")

prompt = "implement a function similar to numpy.unstack"
inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs, pad_token_id=tokenizer.eos_token_id,eos_token_id=tokenizer.eos_token_id)
print(f"USER: {prompt}")
print(f"BOT: {tokenizer.decode(outputs[0])}")