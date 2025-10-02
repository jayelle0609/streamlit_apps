import streamlit as st
import requests
from pathlib import Path

st.set_page_config(
    page_title="Dad Joke Generator",
    page_icon="😂",
    layout="centered"
)

st.title("Jayelle's Laughter Options 🎉")
st.write("Choose your daily dose of joy:")

# --- Dropdown to choose content type
options = ["Dad Jokes", "Funny Meme", "Bible Verse", "Christian Meme", "Meet Jayelle!"]
choice = st.selectbox("Pick a content type", options)

# --- Track meme indices for ordered display (using session state)
if "funny_meme_index" not in st.session_state:
    st.session_state.funny_meme_index = 1
if "christian_meme_index" not in st.session_state:
    st.session_state.christian_meme_index = 1

# --- Dad joke function
def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['joke']
    else:
        return "Couldn't fetch a dad joke. Try again later."

# --- Bible Verse Function (NLT version)
def get_bible_verse():
    url = "https://beta.ourmanna.com/api/v1/get/"
    params = {
        "format": "json",
        "order": "random",
        "version": "nlt"  # New Living Translation
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            verse = data['verse']['details']['text']
            reference = data['verse']['details']['reference']
            return f"🩷 {verse} — {reference} (NLT)"
        else:
            return "Couldn't fetch a Bible verse. Try again later."
    except Exception as e:
        return f"Error fetching Bible verse: {e}"

# --- Show Jayelle intro
def show_jayelle_intro():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("jayelle.png",
                 caption="**👋 Hi, I'm Jayelle! It's very nice to meet ya~**",
                 width=300)

    st.markdown("""
    # **A quick introduction to Jayelle!**

    My full name is Teo Jia Ling. 

    I am an aspiring statistician, exploring how automation can be used to simplify repetitive analysis tasks.

    To me, there's something thrilling about unravelling hidden insights from complicated data!

    While data analysis can feel overwhelming to many, harnessing the power of Python and automation inspires me deeply -- automation is extremely powerful! 
    \n It simplifies difficult analysis tasks and has made me **awe in wonder multiple times.**""")

    # Centered mindblown.gif
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/mindblown.gif", use_container_width=True)

    st.markdown("""
                \n The journey of discovering meaningful insights from seemingly difficult data is deeply interesting to me, and it’s what sparked me to embark on this exciting path of analytics.
    ___

    ### Background and qualifications
    | Year | Qualifications                                   | University                                |
    |-------|------------------------------------------------|-----------------------------------------|
    | 2023  | Bachelors in Social Science in Economics (Honours) | National University of Singapore  |
    | 2024  | Teacher                                       | Self-employed                    |
    | 2025  | Professional Certificate in Data Analytics and Data Visualisation | National University of Singapore  |
    | 2026  | Graduate Certificate in Analytics and Visualisation | Singapore University of Social Science

    ___
                
    ### Skills Overview
    | Hard Skills            | Technical Skills                          |
    |----------------------- |-------------------------------------------|
    | Python                 | Data Cleaning                             |
    | Tableau                | Data Analysis & EDA                       |
    | SQL                    | Data Validation                           |
    | Excel                  | Data Visualisations                       |
    | R                      | Time Series Analysis                      |
    | Orange                 | Statistical Forecasting                   |
    | Stata                  |                                           |

    ___
    Since then I have been working as a tutor, but I am currently looking to challenge myself and expand my horizon back into the world of statistics and economics.
    ___
    This web-app was created to practice how I can deploy future apps for repetitive analysis tasks, web scraping tasks, and even APIs or time series visualisations.
    ___
    Meanwhile, have fun on my page!

   [Click here to view my resume and projects on Git Hub!](https://github.com/jayelle0609)
    """)

# --- Show funny meme (from local files, ordered 1-13)
def show_funny_meme():
    idx = st.session_state.funny_meme_index
    meme_path = f"images/normalmeme{idx}.png"
    if Path(meme_path).exists():
        st.image(meme_path, width=400)
    else:
        st.error(f"Funny meme {idx} not found.")
    # increment index
    st.session_state.funny_meme_index += 1
    if st.session_state.funny_meme_index > 13:
        st.session_state.funny_meme_index = 1

# --- Show christian meme (from local files 1-11, then videos 12-13)
def show_christian_meme():
    idx = st.session_state.christian_meme_index
    if idx <= 11:
        meme_path = f"images/christianmeme{idx}.png"
        if Path(meme_path).exists():
            st.image(meme_path, width=400)
        else:
            st.error(f"Christian meme image {idx} not found.")
    else:
        video_path = f"images/christianmeme{idx}.mp4"
        if Path(video_path).exists():
            video_file = open(video_path, "rb")
            video_bytes = video_file.read()
            col1, col2, col3 = st.columns([1, 2, 1])  # center video
            with col2:
                st.video(video_bytes, format="video/mp4", start_time=0)
        else:
            st.error(f"Christian meme video {idx} not found.")
    # increment index
    st.session_state.christian_meme_index += 1
    if st.session_state.christian_meme_index > 13:
        st.session_state.christian_meme_index = 1

# --- Show bible verse with background image
def show_bible_verse():
    if Path("images/bible_background.png").exists():
        st.image("images/bible_background.png", use_container_width=True)
    else:
        st.warning("Background image bible_background.png not found.")
    verse_text = get_bible_verse()
    st.info(verse_text)

# --- Show dad joke with gif before it
def show_dad_joke():
    if Path("images/dadjokes.gif").exists():
        st.image("images/dadjokes.gif", width=300)
    joke = get_dad_joke()
    st.success(joke)

# --- Logic to show content
if st.button("Let's go!"):
    if choice == "Dad Jokes":
        show_dad_joke()

    elif choice == "Funny Meme":
        show_funny_meme()

    elif choice == "Christian Meme":
        show_christian_meme()

    elif choice == "Bible Verse":
        show_bible_verse()

    elif choice == "Meet Jayelle!":
        show_jayelle_intro()

### /Users/jialing/anaconda_projects/jayelle_dad_jokes/jayelles_dad_jokes.py
### github pushing :
# cd /Users/jialing/anaconda_projects/jayelle_dad_jokes
# git status
# git add jayelles_dad_jokes.py
# git commit -m "Update skills overview table in show_jayelle_intro function"
# git push origin main
