import streamlit as st 

st.set_page_config(page_title= "Growth Mindset Project", page_icon="🌟")

# Custom CSS for Styling  
st.markdown("""  
    <style>  
        /* Background Color */  
        body {  
            background-color: #f5f7fa; /* Soft Light Gray */  
            color: #333333; /* Dark Gray Text */  
        }  

        /* Background Image (Optional) */  
        .stApp {  
            background: url('https://source.unsplash.com/1600x900/?nature,abstract') no-repeat center center fixed;  
            background-size: cover;  
        }  

        /* Custom Font & Center Alignment */  
        h1, h2, h3, h4 {  
            font-family: 'Arial', sans-serif;  
            text-align: center;  
            color: #2E86C1; /* Blue Headers */  
        }  

        /* Button Styling */  
        .stButton>button {  
            background-color: #ff6b6b; /* Coral Red */  
            color: white;  
            border-radius: 8px;  
            padding: 10px 20px;  
            font-weight: bold;  
            transition: 0.3s;  
        }  
        .stButton>button:hover {  
            background-color: #ff3b3b; /* Darker Red on Hover */  
        }  

        /* Text Input & Text Area Styling */  
        .stTextInput>div>div>input, .stTextArea>div>textarea {  
            border: 2px solid #2E86C1; /* Blue Border */  
            border-radius: 5px;  
            padding: 10px;  
        }  

    </style>  
""", unsafe_allow_html=True)

st.title("🧠GROWTH MINDSET CHALLENGE: Web App With Streamlit🌱")

st.header("🤍Welcome To Your Growth Journey!📊")
st.write("Unlock your true potential—because growth has no limits!🚀 This AI-powered app is your personal guide to self-improvement, reflection, and unstoppable success.💡📈")

st.header("💡Today's Growth Mindset Quote")
st.write("Your only limit is your mindset—think big, take action, and grow unstoppable!🔥")

st.header("🛠️ What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:⬇")

if user_input:
    st.success(f"💪Stay strong and keep moving forward toward your goal!🚀")
else:
    st.warning("Share your challenge with us to begin your journey!🔥")    

st.header("Reflect, Learn, and Elevate Your Growth!✨")
reflection = st.text_area("Share your thoughts and reflections here...📝") 

if reflection:
    st.success(f"Great Insight! Your Reflection: {reflection} 🎯✨")
else:
    st.info("Self-reflection fuels growth! Share your thoughts and challenges.✍️💭")

st.header("Celebrate Your Achievements! 🏆")
achievement = st.text_input("What's a recent milestone or success you're proud of? 🌟")


if achievement:
    st.success(f"Bravo! You accomplished: {achievement} 🎉 Keep soaring!🚀")
else:
    st.info("Every effort counts—small wins lead to big success! 💪🌱")

st.write("---")
st.write("_🥇Success is built on consistent effort and self-reflection. Stay committed to growth!✨_")
st.write("**© 2025 ⚡ Created by Zaryab Irfan | All Rights Reserved 🌍**")
