import streamlit as st
import requests
import random

st.set_page_config(
    page_title = "Dad Joke Generator", 
    page_icon = "😂",
    layout = "centered")

st.title("Jayelle's Laughter Options 🎉")
st.write("Choose your daily dose of joy:")

# --- Dropdown to choose content type
options = ["Dad Jokes", "Funny Meme", "Bible Verse", "Christian Meme", "Meet Jayelle!"]
choice = st.selectbox("Pick a content type", options)

# --- Dad joke function
def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept" : "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['joke']
    else:
        return "Couldn't fetch a dad joke. Try again later."
    
# --- Meme Function (from meme-api.com)
def get_funny_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['title'], data['url']
    else:
        return "Funny Meme", None

# --- Bible Verse Function (from dailyverses.net unofficial API)
def get_bible_verse():
    url = "https://beta.ourmanna.com/api/v1/get/?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        verse = data['verse']['details']['text']
        reference = data['verse']['details']['reference']
        return f"📖 {verse} — {reference}"
    else:
        return "Couldn't fetch a Bible verse. Try again later."

# --- Christian Meme Function (from GitHub backend)
def get_christian_meme():
    memes = [
        {
            "title": "Jesus Take the Wheel",
            "url": "https://i.imgflip.com/4t0m5d.jpg"
        },
        {
            "title": "Modern Problems Require Ancient Solutions",
            "url": "https://i.imgur.com/K1ZUJ6L.jpeg"
        },
        {
            "title": "That’s not very Christian of you",
            "url": "https://i.imgur.com/KzGMlCy.jpg"
        },
        {
            "title": "Bible Study Be Like",
            "url": "https://i.redd.it/zf6cd9p7sjv41.jpg"
        },
        {
            "title": "When you pray but still mess up",
            "url": "https://i.imgur.com/tGvRdc1.jpeg"
        },
    ]
    meme = random.choice(memes)
    return meme['title'], meme['url']

# --- Introduction / Jayelle option
def show_jayelle_intro():
    st.image("jayelle.png", caption="👋 Hi, I'm Jayelle!", use_column_width=True)
    st.markdown("""
    **A quick introduction to me!**
                   My real name is Jia Ling. I am an aspiring statistician, exploring how automation can be used to simplify repetitive analysis tasks.
                I graduated with a Bachelors in Social Science in Economics (Honours) from National University of Singapore in 2023.
                Since then, I have been working as a teacher/tutor, but I am currently looking to challenge myself and expand my horizon back into the world of statistics, related to my undergrad studies.
                This web-app was created as a sample, to test how I can deploy future repetitive analysis and web scraping tasks, such as APIs and time series analysis.
                Meanwhile, have fun on my page!
                
   [Click here to view my resume and projects](https://github.com/jayelle0609)
    """)
                
# --- Logic to show content
if st.button("Let's go!"):
    if choice == "Dad Joke":
        st.success(get_dad_joke())

    elif choice == "Funny Meme":
        title, img_url = get_funny_meme()
        st.subheader(title)
        if img_url:
            st.image(img_url, use_column_width=True)
        else:
            st.error("Couldn't load meme.")

    elif choice == "Christian Meme":
        title, img_url = get_christian_meme()
        st.subheader(title)
        if img_url:
            st.image(img_url, use_column_width=True)
        else:
            st.warning("Couldn't load a Christian meme at the moment.")

    elif choice == "Bible Verse":
        st.info(get_bible_verse())

    elif choice == "Meet Jayelle!":
        show_jayelle_intro()