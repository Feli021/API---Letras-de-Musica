import requests
import streamlit as st


endpoint = "https://lyrics.ovh"
response = requests.get(endpoint)
print(response.status_code)

