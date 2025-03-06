import streamlit as st
import pandas as pd
import os  # Importiere das os-Modul

st.set_page_config(page_title='DNB Katalog Abfrage')

st.markdown("# DNB Katalog Klickdummy Testergebnisse")

# 0. Wie alt bist Du?
st.subheader("0. Wie alt bist Du?")
alter = st.number_input("0. Wie alt bist Du?", min_value=0, max_value=120, key="alter")

# 1. Kennst Du den neuen DNB Katalog?
st.subheader("1. Kennst Du den neuen DNB Katalog https://katalog.dnb.de/?")
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

# 4. Zusätzliche Fragen zum Online-Exemplar
st.subheader("4. Zusätzliche Fragen zum Online-Exemplar")
format_online = st.text_input("Welches Format hat das Online Exemplar?", key="format_online")
lizenz_online = st.text_input("Welche Lizenz hat das Online Exemplar?", key="lizenz_online")
nachnutzung_online = st.radio("Kann ich das Online Exemplar beliebig nachnutzen?", ("Ja", "Nein", "Eingeschränkt"), key="nachnutzung_online")
fehlende_informationen = st.text_area("Welche Informationen zu dem Exemplar fehlen?", key="fehlende_informationen")

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
        "Format Online": format_online,
        "Lizenz Online": lizenz_online,
        "Nachnutzung Online": nachnutzung_online,
        "Fehlende Informationen": fehlende_informationen,
    }

    # Daten in ein DataFrame umwandeln
    df = pd.DataFrame([data], index=[0])

    # In CSV-Datei speichern
    try:
        existing_data = pd.read_csv("dnb_umfrage.csv", index_col=0)
        df = pd.concat([existing_data, df], ignore_index=False)
    except FileNotFoundError:
        pass

    df.to_csv("dnb_umfrage.csv", index=True, encoding="utf-8")
    st.success("Daten erfolgreich gespeichert!")

    st.subheader("Gespeicherte Daten:")
    st.dataframe(df)

# Versteckter Button zum Löschen der Daten
delete_password = st.text_input("Daten löschen:", type="password")

if delete_password == "dnb": # Ändern Sie dies zu einem sicheren Passwort!
    if st.button("Daten löschen"):
        try:
            os.remove("dnb_umfrage.csv")
            st.success("Daten erfolgreich gelöscht!")
        except FileNotFoundError:
            st.warning("Keine Daten zum Löschen gefunden.")
