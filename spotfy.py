import streamlit as st

# Dados de exemplo
generos = ["GOSPEL", "POP INTERNACIONAL", "TRAP", "DISNEY"]




# Dicionário relacionando gêneros A SUAS MUSICAS
musica_por_genero = {
    "GOSPEL": ["QUEM È ESSE", "EM MEIO AO VENDAVAL", "TOCA-ME"],
    "POP INTERNACIONAL": [ "Die With A Smile","Treat you Better","WHEN|WAS YOUR MAN","Locked Out Of Heaven"],
    "TRAP": ["SUPERMAN", "SMACK THAT", "BUTTERFLY EFFECT"],
    "DISNEY": ["VEJO EM FIM A LUZ BRILHAR", "UM MUNDO IDEAL", "VEJO UMA PORTA ABRIR"]
}

# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero musical:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionada= st.sidebar.selectbox(
        "Selecione o livro:", 
        musica_por_genero[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and musica_selecionada:
    st.write(f"**MUSICA SELECIONADA:** {musica_selecionada}")
    st.write(f"**gênero:** {genero_selecionado}")
    # st.image(f"{musica_selecionada}.png")



if genero_selecionado == "GOSPEL" and musica_selecionada == "QUEM È ESSE" :
    st.video('https://www.youtube.com/watch?v=0ZF5em0MTwY&list=RD0ZF5em0MTwY&start_radio=1')
 

elif genero_selecionado == "GOSPEL" and musica_selecionada == "EM MEIO AO VENDAVAL" :
    st.video("https://www.youtube.com/watch?v=peitGcdyukA")  

elif genero_selecionado == "GOSPEL" and musica_selecionada == "TOCA-ME" :
    st.video("https://www.youtube.com/watch?v=Ul4dgaXy4Ps&list=RDUl4dgaXy4Ps&start_radio=1")  

elif genero_selecionado == "POP INTERNACIONAL" and musica_selecionada == "Die With A Smile" :
    st.video("https://www.youtube.com/watch?v=kPa7bsKwL-c&list=RDkPa7bsKwL-c&start_radio=1") 

elif genero_selecionado == "POP INTERNACIONAL" and musica_selecionada == "Treat you Better" :
    st.video("https://www.youtube.com/watch?v=lY2yjAdbvdQ&list=RDlY2yjAdbvdQ&start_radio=1")

elif genero_selecionado == "POP INTERNACIONAL" and musica_selecionada == "WHEN|WAS YOUR MAN" :
    st.video("https://www.youtube.com/watch?v=ekzHIouo8Q4&list=RDekzHIouo8Q4&start_radio=1")

elif genero_selecionado == "POP INTERNACIONAL" and musica_selecionada == "Locked Out Of Heaven" :
    st.video("https://youtu.be/e-fA-gBCkj0")

elif genero_selecionado == "TRAP" and musica_selecionada == "SUPERMAN" :
    st.video("http://youtube.com/watch?v=lPlePBCS6Ic&list=RDlPlePBCS6Ic&start_radio=1")

elif genero_selecionado == "TRAP" and musica_selecionada == "BUTTERFLY EFFECT" :
    st.video("https://www.youtube.com/watch?v=_EyZUTDAH0U&list=RD_EyZUTDAH0U&start_radio=1")

elif genero_selecionado == "TRAP" and musica_selecionada == "SMACK THAT" :
    st.video("https://www.youtube.com/watch?v=bKDdT_nyP54&list=RDbKDdT_nyP54&start_radio=1")    

elif genero_selecionado == "DISNEY" and musica_selecionada == "VEJO EM FIM A LUZ BRILHAR" :
    st.video("https://www.youtube.com/watch?v=sRITrFmTT3s")    

elif genero_selecionado == "DISNEY" and musica_selecionada == "UM MUNDO IDEAL" :
    st.video("https://youtu.be/uXu-pB_OOV4")    

elif genero_selecionado == "DISNEY" and musica_selecionada == "VEJO UMA PORTA ABRIR" :
    st.video("https://youtu.be/78KnNoyYFSk")   


