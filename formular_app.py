import streamlit as st
import pandas as pd

st.set_page_config(page_title='DNB Katalog Abfrage')

st.markdown("# DNB Katalog Umfrage")

# 0. Wie alt bist Du?
alter = st.number_input("0. Wie alt bist Du?", min_value=0, max_value=120)

# 1. Kennst Du den neuen DNB Katalog?
st.write("1. Kennst Du den neuen DNB Katalog? (https://katalog.dnb.de/)")
dnb_kenntnis = st.slider("Antwort 1 bis 5 (5 = sehr gut)", 1, 5, 3)

# 2. Du bist zuhause und möchtest das digitale Exemplar aufrufen
st.subheader("2. Digitales Exemplar zuhause aufrufen")
klickpfad_digital = st.text_area("a) Beschreibe Deinen Klickpfad:")
gedanken_digital = st.text_area("b) Beschreibe Deine Gedanken beim Klicken:")
zufriedenheit_digital = st.radio("c) Bist Du zufrieden mit der Benutzungsführung?", ("Ja", "Nein", "Teils"))
aenderung_digital = st.text_area("d) Was würdest Du anders machen/erwarten?")

# 3. Du möchtest das Medium physisch einsehen
st.subheader("3. Du möchtest das Medium physisch einsehen")
klickpfad_physisch = st.text_area("a) Beschreibe Deinen Klickpfad:")
gedanken_physisch = st.text_area("b) Beschreibe Deine Gedanken beim Klicken:")
zufriedenheit_physisch = st.radio("c) Bist Du zufrieden mit der Benutzungsführung?", ("Ja", "Nein", "Teils"))
aenderung_physisch = st.text_area("d) Was würdest Du anders machen/erwarten?")

if st.button("Absenden"):
    # Daten in ein Dictionary speichern
    data = {
        "Alter": alter,
        "DNB Kenntnis": dnb_kenntnis,
        "Klickpfad Digital": klickpfad_digital,
        "Gedanken Digital": gedanken_digital,
        "Zufriedenheit Digital": zufriedenheit_digital,
        "Aenderung Digital": aenderung_digital,
        "Klickpfad Physisch": klickpfad_physisch,
        "Gedanken Physisch": gedanken_physisch,
        "Zufriedenheit Physisch": zufriedenheit_physisch,
        "Aenderung Physisch": aenderung_physisch,
    }

    # Daten in ein DataFrame umwandeln
    df = pd.DataFrame([data])

    # In CSV-Datei speichern
    try:
        existing_data = pd.read_csv("dnb_umfrage.csv")
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        pass  # Wenn die Datei nicht existiert, wird sie neu erstellt

    df.to_csv("dnb_umfrage.csv", index=False, encoding="utf-8")
    st.success("Daten erfolgreich gespeichert!")

    st.subheader("Gespeicherte Daten:")
    st.dataframe(df)  # Zeigt das DataFrame in Streamlit an


