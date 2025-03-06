import streamlit as st
import psycopg2
import os

# Lire l'URL de connexion de la base de données depuis les secrets
DB_URL = os.getenv("DB_URL")

def connect_db():
    # Utiliser l'URL de connexion pour établir la connexion
    return psycopg2.connect(DB_URL)

def insert_tester(first_name, last_name, email):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO beta_testers (first_name, last_name, email) VALUES (%s, %s, %s)",
                (first_name, last_name, email))
    conn.commit()
    cur.close()
    conn.close()

# Interface Streamlit
st.title("AIstethic - Devenez Bêta-Testeur !")
st.write("Testez notre technologie de placement de meubles en réalité augmentée.")

with st.form("beta_tester_form"):
    first_name = st.text_input("Prénom")
    last_name = st.text_input("Nom")
    email = st.text_input("Email")

    submitted = st.form_submit_button("S'inscrire")

    if submitted:
        if "@" not in email or "." not in email:
            st.error("Veuillez entrer une adresse email valide.")
        elif not first_name or not last_name:
            st.error("Tous les champs sont obligatoires.")
        else:
            insert_tester(first_name, last_name, email)
            st.success("Merci pour votre inscription ! Vous serez contacté prochainement.")

