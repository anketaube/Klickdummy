import streamlit as st

def main():
    st.title("Mein Streamlit Formular")

    # Formular erstellen
    with st.form(key='mein_formular'):
        st.write("Bitte füllen Sie das Formular aus:")
        
        # Textfeld
        name = st.text_input(label='Name')
        
        # Dropdown-Menü
        option = st.selectbox(
            'Wie möchten Sie kontaktiert werden?',
            ('E-Mail', 'Telefon', 'Post'))
        
        # Slider
        alter = st.slider("Alter", 0, 100, 25)
        
        # Checkbox
        zustimmung = st.checkbox("Ich stimme den Nutzungsbedingungen zu")
        
        # Submit Button
        submit_button = st.form_submit_button(label='Absenden')

    # Verarbeitung nach dem Absenden
    if submit_button:
        if zustimmung:
            st.success("Formular erfolgreich abgesendet!")
            st.write(f"Hallo {name}, Sie sind {alter} Jahre alt und möchten per {option} kontaktiert werden.")
        else:
            st.error("Bitte stimmen Sie den Nutzungsbedingungen zu.")

if __name__ == "__main__":
    main()
