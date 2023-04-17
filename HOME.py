import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Webpage" , page_icon=":tada",layout="wide")
st.title("Main Page")
st.write("---")
st.subheader("**WELCOME** *to the page* :wave:")
st.title("About Me")
st.write("I am *RITIKA SATHUA* from Electronics and Telecommunication branch")
st.write("Ich besuche die neunte Klasse einer Dresdner Realschule, und es gefällt mir dort sehr. Ich habe fast nur nette und hilfsbereite Lehrer. Nur mein Religionslehrer ist so langweilig, dass ich fast immer mitten im Unterricht einschlafe und mein Sitznachbar mich immer anschubst, um mich aufzuwecken. Der Lehrer spricht immer ganz langsam und mit einer sehr monotonen Stimme. Da muss man ja einschlafen. Am meisten Spaß macht Kochen, da ich es einfach toll finde in der Schulküche. Da gibt es so viel zu entdecken, man ist die ganze Zeit aktiv und muss nicht nur zuhören. Außerdem passiert immer irgendein Missgeschick und das ist dann sehr lustig. Unsere Schulküche ist ganz modern, da unserer Schulleiter Spenden für neues Equipment gesammelt hat. Im Sommer verkaufen wir auch Kuchen und andere selbsgekochte Delikatessen auf unserem jährlichen Schulfest.")
st.markdown("[Instagram](https://www.instagram.com/ritika3151512/)")
st.markdown("[GMAIL](sathuaritika45@gmail.com)")
st.markdown("---")
with st.form("form1",clear_on_submit=True): 
 name=st.text_input("enter name")
 email=st.text_input("E-mail")
 message=st.text_area("enter any message")
 submit=st.form_submit_button("submit")
