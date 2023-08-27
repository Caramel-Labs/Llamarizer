import streamlit as st
import llama

st.title("Llamarizer")

print(st.session_state)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

print(st.session_state.messages)

# React to user input
if prompt := st.chat_input("Enter text to summarize"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

print(st.session_state.messages)

modified_prompt = ""
response = ""

if prompt:
    modified_prompt = f"""Summarize the following text: \n{prompt} \n\nSummary: """
    print(modified_prompt)
    response = llama.get_response(modified_prompt)

# Display assistant response in chat message container
with st.chat_message("assistant"):
    st.markdown(response)

# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})

print(st.session_state.messages)
