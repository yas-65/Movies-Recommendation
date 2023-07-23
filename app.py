import streamlit as st 
import pandas as pd 
import pickle
import requests



def poster(movie_id):
    x=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    q=x.json()
    
    f="https://image.tmdb.org/t/p/w780" + q["poster_path"]
    return f
  
def Recom(movie):
    movie_index = data[data["title"]==movie].index[0]
    distance=sim[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:16]
    
    recomn = []
    recom_movie_poster=[]
    for i in movie_list:
        movie_id=data["id"][i[0]]

        recomn.append(data["title"][i[0]])
        recom_movie_poster.append(poster(movie_id))
    return recomn,recom_movie_poster

movied=pickle.load(open("moviee.pkl","rb"))
sim = pickle.load(open("similarity.pkl","rb"))
data=pd.DataFrame(movied)

st.title("Movie Recommendation System")


selected_movies=st.selectbox("select movie",data["title"].values)


if st.button("Recommend"):

    names,poster= Recom(selected_movies)
    col=st.columns(spec=1,gap="medium")
    col=st.columns(5)
    for i in range(5):
        with col[i]:
            st.write(names[i])
            st.image(poster[i])
    
    col=st.columns(5)
    for i in range(5,10):
        with col[i-5]:
            st.write(names[i])
            st.image(poster[i])
           
    
   

    
   



