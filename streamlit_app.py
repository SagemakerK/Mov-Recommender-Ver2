import streamlit as st


# --PAGE SETUP --
app_page = st.Page(
    page= 'views/app.py' ,
    title= "Movie Recommender System" ,
    default=True
)

about_us = st.Page(
    page='views/about_us.py' ,
    title= "About the Developers" ,
)


#NAVIGATON
pg = st.navigation(pages=[app_page, about_us])

#ALL PAGES
st.logo("Assets/Untitled-1.png", size="large" )


#RUN-NAVIGATION
pg.run()