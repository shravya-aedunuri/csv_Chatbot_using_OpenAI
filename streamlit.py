import requests

import streamlit as st


def send_message(prompt):
    url = 'https://31ef-34-41-218-240.ngrok-free.app/send_message'
    data = {'prompt': prompt}
    response = requests.post(url, data=data)
    return response.json()

def main():
    st.title('Pathology Report Analysis using LLM')

    prompt = st.text_input('Enter your prompt:')
    if st.button('Send to LLM'):
        if prompt:
            response = send_message(prompt)
            st.subheader('Response - Without Index:')
            st.write(response['withOutIndex'])

            st.subheader('Response - With Index:')
            if 'withIndex' in response and response['withIndex']:
                withIndex = response['withIndex']
                st.subheader('With Index Chroma DB:')
                st.write(withIndex['withIndexChromaDB'])
        else:
            st.warning('Please enter a prompt.')

if __name__ == '__main__':
    main()
