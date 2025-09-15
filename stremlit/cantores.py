import streamlit as st

# Dados
generos = ["GOSPEL", "POP INTERNACIONAL", "RAP", "DISNEY"]

musicas = {
    "JULLIANY SOUSA": ["QUEM É ESSE", "LINDO MOMENTO", "CASINHA FAVORITA"],
    "PAULO NETO": ["NAO FOI POR ACASO", "EM MEIO AO VENDAVAL", "TUA PRESENÇA"],
    "JEFERSON E SUELLEN": ["ACENDE OUTRA VEZ", "O ENCONTRO", "VEM ME BUSCAR", "LABAREDA"],
    "TAYLOR SWIFT": ["CARDIGAN", "AUGUST", "LOVE STORY", "LOVER"],
    "ARIANA GRANDE": ["INTO YOU", "EVERYDAY"],
    "SHAWN MENDES": ["IN MY BLOOD", "MONSTER", "TREAT YOU BETTER", "NEVER BE ALONE", "MERCY"],
    "BRUNO MARS": ["LOCKED OUT OF HEAVEN", "THE LAZY SONG", "WHEN I WAS YOUR MAN", "THAT'S WHAT I LIKE"],
    "TRAVIS SCOTT": ["ASTROTHUNDER", "STARGAZING", "STOP TRYING TO BE GOD"],
    "EMINEM": ["MONSTER", "WITHOUT ME", "TILL I COLLAPSE", "SUPERMAN"],
    "2 PAC": ["THUG NIGGA", "CHANGES", "CALIFORNIA", "DEAR MAMA"],
    "KANYE WEST": ["I WONDER", "DEVIL IN A NEW DRESS", "EVERYTHING I AM"],
    "ICE CUB": ["IT WAS A GOOD DAY", "NO VASELINE", "CHECK YO SELF"],
    "FROZEN": ["VEJO UMA PORTA ABRIR"],
    "MOANA": ["saber quem eu sou"],
    "ENCANTO": ["familia madrigal"],
    "RAPUNZEL": ["VEJO EM FIM A LUZ BRILHAR",] }

cantores_por_genero = {
    "GOSPEL": ["JULLIANY SOUSA", "PAULO NETO", "JEFERSON E SUELLEN"],
    "POP INTERNACIONAL": ["BRUNO MARS", "TAYLOR SWIFT", "ARIANA GRANDE", "SHAWN MENDES"],
    "RAP": ["TRAVIS SCOTT", "EMINEM", "2 PAC", "KANYE WEST", "ICE CUB"],
    "DISNEY": ["FROZEN", "ENCANTO", "MOANA", "RAPUNZEL"]}

# Sidebar
genero = st.sidebar.selectbox("Selecione o gênero musical:", generos)
cantor = st.sidebar.selectbox("Selecione o cantor:", cantores_por_genero[genero])
musica = st.sidebar.selectbox("Selecione a música:", musicas[cantor])

# Exibir seleção
st.write(f"🎶 Música selecionada: **{musica}**")
st.write(f"👤 Cantor: **{cantor}**")
st.write(f"🎼 Gênero: **{genero}**")

#### GOSPEL
if genero=="GOSPEL" and cantor=="JULLIANY SOUSA" and musica=="QUEM É ESSE":
    st.video('https://www.youtube.com/watch?v=0ZF5em0MTwY&list=RD0ZF5em0MTwY&start_radio=1')

elif genero=="GOSPEL" and cantor=="JULLIANY SOUSA" and musica=="LINDO MOMENTO":
    st.video('https://youtu.be/xcC3Xh3PFcE')    

elif genero=="GOSPEL" and cantor=="JULLIANY SOUSA" and musica=="CASINHA FAVORITA":
    st.video('https://youtu.be/owtxVwa32AY') 

elif genero=="GOSPEL" and cantor=="PAULO NETO" and musica=="EM MEIO AO VENDAVAL":
    st.video('https://youtu.be/peitGcdyukA') 

elif genero=="GOSPEL" and cantor=="PAULO NETO" and musica=="TUA PRESENÇA":
    st.video('https://youtu.be/gs-V3_9eqX8')     

elif genero=="GOSPEL" and cantor=="PAULO NETO" and musica=="NAO FOI POR ACASO":
    st.video('https://youtu.be/LjtXgDuBKGo') 

elif genero=="GOSPEL" and cantor=="JEFERSON E SUELLEN" and musica=="ACENDE OUTRA VEZ":
    st.video('https://youtu.be/01nrJxiJT8k')

elif genero=="GOSPEL" and cantor=="JEFERSON E SUELLEN" and musica== "O ENCONTRO":
    st.video('https://youtu.be/3DyPaHTcSMU')  

elif genero=="GOSPEL" and cantor=="JEFERSON E SUELLEN" and musica== "VEM ME BUSCAR":
    st.video('https://youtu.be/t6Pd8gXIASU')    


#---------------------POP INTERNACIONAL

elif genero=="POP INTERNACIONAL" and cantor=="BRUNO MARS"and musica== "LOCKED OUT OF HEAVEN":
    st.video('https://youtu.be/e-fA-gBCkj0')        

elif genero=="POP INTERNACIONAL" and cantor=="BRUNO MARS"and musica==  "THE LAZY SONG":
    st.video('https://youtu.be/fLexgOxsZu0')   

elif genero=="POP INTERNACIONAL" and cantor=="BRUNO MARS"and musica== "WHEN I WAS YOUR MAN":
    st.video('https://youtu.be/ekzHIouo8Q4')   

elif genero=="POP INTERNACIONAL" and cantor=="BRUNO MARS"and musica== "THAT'S WHAT I LIKE":
    st.video('https://youtu.be/PMivT7MJ41M') 

elif genero=="POP INTERNACIONAL" and cantor=="TAYLOR SWIFT"and musica=="CARDIGAN":
    st.video('https://youtu.be/K-a8s8OLBSE')

elif genero=="POP INTERNACIONAL" and cantor=="TAYLOR SWIFT"and musica=="AUGUST":
    st.video('https://youtu.be/nn_0zPAfyo8')

elif genero=="POP INTERNACIONAL" and cantor=="TAYLOR SWIFT"and musica=="LOVE STORY":
    st.video('https://youtu.be/8xg3vE8Ie_E')

elif genero=="POP INTERNACIONAL" and cantor=="TAYLOR SWIFT"and musica=="LOVER":
    st.video('https://youtu.be/8xg3vE8Ie_E')

elif genero=="POP INTERNACIONAL" and cantor=="ARIANA GRANDE"and musica=="LOVER":
    st.video('https://youtu.be/8xg3vE8Ie_E')


 


