import numpy as np
import pandas as pd
import streamlit as st


st.header('Искусственный Интеллект для определения авторства текста.')

with st.sidebar:
    st.markdown(''' # Содержание:''')
    st.markdown("## [1. Актуальность тематики](#about)", unsafe_allow_html=True)
    st.markdown("## [2. Этапы разработки кейса](#pipeline)", unsafe_allow_html=True)
    st.markdown("## [3. Задача](#task)", unsafe_allow_html=True)
    st.markdown("## [4. Линейная регрессия](#datadata)", unsafe_allow_html=True)
    st.markdown("## [5. База данных ](#bagofwords)", unsafe_allow_html=True)
    st.markdown("## [6. Демонстрация работы](#neuronwork)", unsafe_allow_html=True)
    st.markdown("## [7. Тест](#voprosi)", unsafe_allow_html=True)

st.subheader('Актуальность тематики', anchor='about')
st.subheader('Кому будет полезно изучить данную работу ?')
st.write('1.Студентам экономических специальностей. Интересующимся оценкой недвижимости.')
st.write('2.Студентам, изучающим принципы математического обоснования ценообразования товаров.')
st.write('3.Студентам других специальностей, интересующимся возможностями применением искусственного интеллекта в области ценообразования.')




