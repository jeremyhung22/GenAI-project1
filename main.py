import streamlit as st
from openai import OpenAI
from prompts import userInput

st.set_page_config(page_title="D&D Character Backstory Generator")
st.title('D&D Character Backstory Generator')

# API key input in sidebar
user_api_key = st.sidebar.text_input('API Key', type="password")


def generate_response(input_text):

    status_message = st.empty()
    status_message.info("Generating")

    try:
        # Initialize client only if API key is provided
        client = OpenAI(
            api_key=user_api_key,
            base_url="https://openrouter.ai/api/v1",
        )
        
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an expert in creating deep, immersive, and emotionally rich Dungeons & Dragons character backstories. Generate a compelling backstory, three adventure hooks, and an Adobe Firefly art prompt for the following character."},
                {"role": "user", "content": input_text}
                #{"role": "assistant", "content": prompt}
            ]
        )
        output = completion.choices[0].message.content
        # Display the generated response
        clean_output = output.split(r"\boxed{")[0].strip()
        st.markdown(clean_output)
        status_message.empty()
    except Exception as e:
        status_message.empty()  # Clear the "Generating" message
        st.error(f"An error occurred: {e}")
    return

# Create form for user input
with st.form('my_form'):
    text = userInput()
    submitted = st.form_submit_button('Submit')

if submitted: 
    # Process the form submission outside the form
    if not user_api_key:
        st.warning("Please enter an API key.")
    elif not user_api_key.startswith('sk-'):
        st.warning("Please enter a valid API key starting with 'sk-'.")
    else:
        generate_response(text)