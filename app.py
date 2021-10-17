import streamlit as st
import pickle
import requests

st.set_page_config(page_title='lol', layout = 'wide', initial_sidebar_state = 'auto')

def fetch_poster(movie_name):
    response = requests.get('https://api.themoviedb.org/3/search/movie?'
                            'api_key=8265bd1679663a7ea12ac168da84d2e8'
                            '&language=en-US&query={}'.format(movie_name))
    data=response.json()
    return data

new_df = pickle.load(open('df.pkl', 'rb'))
def recommend(movie,similarity):
    index_pos = new_df[new_df['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[index_pos])), key=lambda x: x[1], reverse=True)[1:6]

    return movie_list

new_df=pickle.load(open('df.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movie=st.selectbox('Select a movie',new_df['title'].values)

if st.button('Recommend'):
    movie_list = recommend(selected_movie,similarity)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        movie_name = new_df.iloc[movie_list[0][0]]['title']
        st.text(movie_name)
        data = fetch_poster(movie_name)
        st.image('https://image.tmdb.org/t/p/w500/' + data['results'][0]['poster_path'])

    with col2:
        movie_name = new_df.iloc[movie_list[1][0]]['title']
        st.text(movie_name)
        data = fetch_poster(movie_name)
        st.image('https://image.tmdb.org/t/p/w500/' + data['results'][0]['poster_path'])

    with col3:
        movie_name = new_df.iloc[movie_list[2][0]]['title']
        st.text(movie_name)
        data = fetch_poster(movie_name)
        st.image('https://image.tmdb.org/t/p/w500/' + data['results'][0]['poster_path'])

    with col4:
        movie_name = new_df.iloc[movie_list[3][0]]['title']
        st.text(movie_name)
        data = fetch_poster(movie_name)
        st.image('https://image.tmdb.org/t/p/w500/' + data['results'][0]['poster_path'])

    with col5:
        movie_name = new_df.iloc[movie_list[4][0]]['title']
        st.text(movie_name)
        data = fetch_poster(movie_name)
        st.image('https://image.tmdb.org/t/p/w500/' + data['results'][0]['poster_path'])






#https://image.tmdb.org/t/p/w500/