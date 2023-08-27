# WARNING - this app does not function as intended. Please use 'app.py' as the Streamlit frontend.

import streamlit as st

# install 'streamlit-chat' in the virtualenv and uncomment this line
# from streamlit_chat import message
import model


def clear_chat():
    st.session_state.messages = [
        {"role": "assistant", "content": "Say something to get started!"}
    ]


st.title("Llama2 Clarifai Test App")


if "messages" not in st.session_state:
    print(f"st.session_state is {st.session_state}")
    print("Initializing session state")
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Say something to get started!"}
    ]


with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])

    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
    )

    b.form_submit_button("Send", use_container_width=True)


for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")


if user_prompt:
    print("user_prompt: ", user_prompt)

    st.session_state.messages.append({"role": "user", "content": user_prompt})

    message(user_prompt, is_user=True)
    print(f"Message passed to frontend: {user_prompt}")

    # get response from Llama2 API
    response = model.get_response(user_prompt)
    print(f'Response from Llama2 API: "{response}"')
    print(type(response))

    msg = {"role": "assistant", "content": response}

    print("st.session_state.messages: ", st.session_state.messages)

    st.session_state.messages.append(msg)

    print("msg.content: ", msg["content"])

    message(msg["content"])


if len(st.session_state.messages) > 1:
    st.button("Clear Chat", on_click=clear_chat)
