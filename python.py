from flask import Flask, render_template, request
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)

# Initialize chat history globally (or you can manage it per session)
chat_history_ids = None

@app.route("/")
def index():
    return render_template('new.html')

@app.route("/get", methods=["POST"])
def chat():
    global chat_history_ids  # Use global to maintain history
    if request.method == "POST":
        msg = request.form["msg"]
        return get_chat(msg)

def get_chat(text):
    global chat_history_ids

    # Encode the new user input and add the eos_token
    new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')

    # Append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids

    # Generate a response while limiting the total chat history to 1000 tokens
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode and return the last output tokens from the bot
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    app.run(debug=True)
