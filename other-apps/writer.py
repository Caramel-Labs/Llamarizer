import streamlit as st
import letter_writer
import model

# Page name, favicon and layout
st.set_page_config(page_title="LlamaWriter", page_icon=":llama:", layout="centered")

# Page title and description
st.title("🦙 LlamaWriter")
st.markdown("Lorem Ipsum")

# Tabs
letter, email, cover_letter, resume = st.tabs(
    ["Letter", "Email", "Cover Letter", "Resume"]
)

with letter:
    letter_writer.render_letter_writer()


with email:
    st.header("Write an Email")
    st.markdown("Provide the details of your email below.")

    st.text_input(label="Who should this email go to?", placeholder="The recipient")

    st.text_input(
        label="What is the subject of this letter?", placeholder="The subject"
    )

    st.text_area(
        label="Anything important to mention?", placeholder="", key="email-info"
    )

    st.button(label="Write Email")

with cover_letter:
    st.header("Write a Cover Letter")
    st.markdown("Provide the details of your cover letter below.")

    st.text_input(
        label="Who should this cover letter go to?", placeholder="The recipient"
    )
