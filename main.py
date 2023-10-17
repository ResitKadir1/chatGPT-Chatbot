

#pip3 install openai
#pip3 install gradio
#https://platform.openai.com/account/api-keys

import openai
import gradio

openai.api_key = "sk-"

messages = [{"role": "system",
 "content": "You are a programmer expert"}]

def CustomChatGPT(rekas):
    messages.append({"role": "user", "content": rekas})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Resit GPT")

demo.launch(share=True)


