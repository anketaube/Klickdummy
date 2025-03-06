import streamlit as st
import pandas as pd

st.set_page_config(page_title='DNB Katalog Abfrage')

st.markdown("# DNB Katalog Klickdummy Testergebnisse")

# 0. Wie alt bist Du?
alter = st.number_input("0. Wie alt bist Du?", min_value=0, max_value=120, key="alter")

# 1. Kennst Du den neuen DNB Katalog?
st.write("1. Kennst Du den neuen DNB Katalog? (https://katalog.dnb.de/)")
dnb_kenntnis = st.slider("Antwort 0 bis 5 (0 = gar nicht, 5 = sehr gut)", 0, 5, 3, key="dnb_kenntnis")

# 2. Du bist zuhause und möchtest das digitale Exemplar aufrufen
st.subheader("2. Testaufgabe: Du bist zuhause und möchtest die Online-Ausgabe aufrufen")
klickpfad_digital_a = st.text_area("a) Beschreibe Deinen Klickpfad:", key="klickpfad_digital_a")
gedanken_digital_b = st.text_area("b) Beschreibe Deine Gedanken beim Klicken:", key="gedanken_digital_b")
zufriedenheit_digital_c = st.radio("c) Bist Du zufrieden mit der Benutzungsführung?", ("Ja", "Nein", "Teils"), key="zufriedenheit_digital_c")
aenderung_digital_d = st.text_area("d) Was würdest Du anders machen/erwarten?", key="aenderung_digital_d")

# 3. Du möchtest das Medium physisch einsehen
st.subheader("3. Testaufgabe: Du möchtest das physische Medium einsehen")
klickpfad_physisch_a = st.text_area("a) Beschreibe Deinen Klickpfad:", key="klickpfad_physisch_a")
gedanken_physisch_b = st.text_area("b) Beschreibe Deine Gedanken beim Klicken:", key="gedanken_physisch_b")
zufriedenheit_physisch_c = st.radio("c) Bist Du zufrieden mit der Benutzungsführung?", ("Ja", "Nein", "Teils"), key="zufriedenheit_physisch_c")
aenderung_physisch_d = st.text_area("d) Was würdest Du anders machen/erwarten?", key="aenderung_physisch_d")

if st.button("Absenden"):
    # Daten in ein Dictionary speichern
    data = {
        "Alter": alter,
        "DNB Kenntnis": dnb_kenntnis,
        "Klickpfad Digital": klickpfad_digital_a,
        "Gedanken Digital": gedanken_digital_b,
        "Zufriedenheit Digital": zufriedenheit_digital_c,
        "Aenderung Digital": aenderung_digital_d,
        "Klickpfad Physisch": klickpfad_physisch_a,
        "Gedanken Physisch": gedanken_physisch_b,
        "Zufriedenheit Physisch": zufriedenheit_physisch_c,
        "Aenderung Physisch": aenderung_physisch_d,
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
