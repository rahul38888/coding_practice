import tiktoken
from transformers import GPT2Tokenizer

# gpt2_tokenizer = AutoTokenizer.from_pretrained("gpt2", use_fast=True)
gpt2_tokenizer = GPT2Tokenizer.from_pretrained("openai-community/gpt2")
oai_tokenizer = tiktoken.get_encoding("gpt2")

orig = "Is this restaurant family-friendly ? Yes No Unsure ? This is an other sentence ."

hf_enc = gpt2_tokenizer(orig)["input_ids"]
hf_dec = gpt2_tokenizer.decode(hf_enc)

oai_enc = oai_tokenizer.encode(orig)
oai_dec = oai_tokenizer.decode(oai_enc)

if __name__ == '__main__':
    print(hf_dec)
    print(oai_dec)
