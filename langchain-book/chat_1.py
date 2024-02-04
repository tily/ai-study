import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Ready! Input messages!").send()

@cl.on_message
async def on_message(input_message):
    print("Your input: ", input_message)
    await cl.Message(content="Hello!").send()
