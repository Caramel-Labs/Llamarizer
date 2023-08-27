import streamlit as st
import model

st.title("Llamarizer")

print(st.session_state)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Enter text to summarize"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


modified_prompt = ""
response = ""

if prompt:
    modified_prompt = f"""Summarize the following text: \n\n{prompt} \n\nSummary: """
    print(modified_prompt)
    response = model.get_response(modified_prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
