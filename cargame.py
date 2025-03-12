import streamlit as st
import time
import random

def get_random_position():
    return random.randint(50, 250)

st.set_page_config(page_title="Car Game", layout="wide")

st.markdown(
    """
    <style>
        @keyframes moveBackground {
            from { background-position: 0px 0px; }
            to { background-position: 0px 1000px; }
        }

        @keyframes moveBuildings {
            from { transform: translateX(100%); }
            to { transform: translateX(-100%); }
        }

        .game-container {
            position: relative;
            height: 500px;
            width: 100%;
            background: linear-gradient(to bottom, #87CEEB, #4682B4);
            overflow: hidden;
            border-radius: 15px;
        }

        .road {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 200px;
            background: repeating-linear-gradient(
                black, black 20px, gray 20px, gray 40px
            );
            animation: moveBackground 5s linear infinite;
        }

        .buildings {
            position: absolute;
            bottom: 200px;
            width: 100%;
            height: 100px;
            background: repeating-linear-gradient(
                #2c3e50, #2c3e50 40px, #34495e 40px, #34495e 80px
            );
            animation: moveBuildings 10s linear infinite;
        }

        .car {
            position: absolute;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 100px;
            background: red;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="game-container">', unsafe_allow_html=True)
st.markdown('<div class="buildings"></div>', unsafe_allow_html=True)
st.markdown('<div class="road"></div>', unsafe_allow_html=True)
st.markdown('<div class="car"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write("### Use arrow keys to move the car!")
