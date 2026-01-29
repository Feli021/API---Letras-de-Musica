import requests
import streamlit as st
from requests.utils import quote

def buscar_letra(banda, musica):
    banda = quote(banda)
    musica = quote(musica)

    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        letra = response.json()["lyrics"]
        return letra
    else: 
        return None
    
st.image("https://i.imgur.com/SmktDIH.png")
banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar:
    # You wil going to make this search for lyrics 
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Encontramos a letra da música!")
        st.text(letra)
    else:
        st.error("Infelizmente não encontramos a letra da música")
    

