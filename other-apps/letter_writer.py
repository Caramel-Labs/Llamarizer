import streamlit as st
import model


def render_letter_writer():
    st.header("Write a Letter")
    st.markdown("Provide the details of your letter below.")

    toggle = st.toggle(label="This is a formal letter", value=False)

    recipient_name = st.text_input(
        label="Who should this letter go to?", placeholder="The recipient's name"
    )

    recipient_address = st.text_input(
        label="What is their address?", placeholder="The recipient's address"
    )

    subject = ""

    if toggle:
        subject = st.text_input(
            label="What is the subject of this letter?",
            placeholder="The subject",
            key="letter-subject",
        )

    sender_name = st.text_input(label="What is your name?", placeholder="Your name")

    sender_address = st.text_input(
        label="What is your address?", placeholder="Your address"
    )

    additional_info = st.text_area(
        label="Anything important to mention?", placeholder="", key="letter-info"
    )

    submit = st.button(
        label="Write Letter",
        on_click=lambda: prepare_prompt(
            recipient_name,
            recipient_address,
            sender_name,
            sender_address,
            subject,
            additional_info,
        ),
    )


def prepare_prompt(
    recipient_name,
    recipient_address,
    sender_name,
    sender_address,
    subject,
    additional_info,
):
    prompt = f"""
    You are an AI assistant who helps in writing. You must write a letter by considering the following facts:\n\n
    1. The recipient is {recipient_name}. Their address is {recipient_address}.\n
    2. The sender is {sender_name}. Their address is {sender_address}.\n
    3. The subject of the letter is {subject}. If the subject is empty, this is a personal letter.\n
    4. Other information you need to know about this letter: {additional_info}\n\n
    The generated letter:\n\n
    """

    model_response = model.get_response(prompt)
    response = st.markdown(model_response)
