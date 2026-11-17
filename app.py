import streamlit as st
import random
import time

st.set_page_config(page_title="SBK Run Game", page_icon="🏃‍♀️", layout="centered")
st.title("🏃‍♀️ SBK Physics Girl - Run From Exams!")

# --- Start ---
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.girl = 5
    st.session_state.zombies = {"EXAM": 0, "QUIZ": 1, "PRESENTATION": 2, "ASSIGNMENT": 3}
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.jump = 0
    st.session_state.msg = "Press START to Run!"

if st.button("▶ START / RESTART"):
    st.session_state.started = True
    st.session_state.girl = 5
    st.session_state.zombies = {"EXAM": 0, "QUIZ": 1, "PRESENTATION": 2, "ASSIGNMENT": 3}
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.jump = 0
    st.session_state.msg = "Bhago! EXAM peeche hai! 😱"
    st.rerun()

if st.session_state.started:
    st.write(f"❤️ Lives: {st.session_state.lives} | 🏆 Score: {st.session_state.score} | 📏 Distance: {st.session_state.score}m")
    st.write(f"**{st.session_state.msg}**")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬆️ JUMP"):
            st.session_state.jump = 2
            st.session_state.msg = "Girl ne Jump kiya! 🎉"
    with col2:
        if st.button("➡️ FAST"):
            st.session_state.girl = min(9, st.session_state.girl + 1)
    with col3:
        if st.button("⬅️ SLOW"):
            st.session_state.girl = max(1, st.session_state.girl - 1)

    # Zombies move
    for name in st.session_state.zombies:
        speed = 1
        if name == "EXAM":
            speed = 1
        if name == "QUIZ":
            speed = 1
        st.session_state.zombies[name] += 0.5

    # Jump countdown
    if st.session_state.jump > 0:
        st.session_state.jump -= 1

    # Check catch
    caught = None
    for name, pos in st.session_state.zombies.items():
        if pos >= st.session_state.girl - 0.5 and st.session_state.jump == 0:
            caught = name
            break

    if caught:
        st.session_state.lives -= 1
        st.session_state.zombies[caught] = 0
        st.session_state.msg = f"Oh No! {caught} ne pakar liya! 😭 1 Life gayi"
        if st.session_state.lives <= 0:
            st.session_state.msg = f"💀 GAME OVER! {caught} ZOMBIE ne pakar liya! Physics Girl is DEAD..."
            st.session_state.started = False
    else:
        st.session_state.score += 5

    # --- Road Drawing ---
    st.markdown("### 🏫 FACULTY OF BASIC SCIENCES ➡️ - Is taraf bhago!")
    st.markdown("---")
    st.markdown("**SBK CAMPUS - BROAD ROAD**")

    # 10 boxes road
    road = ""
    for i in range(10):
        girl_here = (i == st.session_state.girl)
        zombie_here = ""
        for zname, zpos in st.session_state.zombies.items():
            if int(zpos) == i:
                if zname == "EXAM":
                    zombie_here += "🧟‍♂️👹"
                elif zname == "QUIZ":
                    zombie_here += "🧟"
                else:
                    zombie_here += "🧟‍♀️"
        if girl_here and st.session_state.jump > 0:
            road += " | 🦸‍♀️✨ "
        elif girl_here:
            road += " | 👧🏃‍♀️💖 "
        elif zombie_here:
            road += f" | {zombie_here} "
        else:
            road += " | ___ "
    st.markdown(f"### {road} | 🏁")
    st.markdown("---")

    st.write("**Zombies:** 👹 EXAM = Sab se BARA | 🧟 QUIZ = Medium | 🧟‍♀️ PRESENTATION + ASSIGNMENT = Chote")
    st.write("**Girl:** Pretty girl with forehead bangs 💖 Pink dress + SBK Bag")
    st.write("**Rule:** Jump dabao to zombie pakar nahi payega. Agar 3 baar pakri gayi to GAME OVER.")

    if st.session_state.score > 200:
        st.balloons()
        st.success("🎉 YOU ESCAPED! Tum Faculty of Basic Sciences pahunch gayi!")
        st.session_state.started = False

else:
    st.info("START dabao, phir JUMP / FAST dabate raho. EXAM sab se bara zombie hai, us se bacho!")
    st.markdown("### 👧🏃‍♀️ .......... 🧟‍♂️ EXAM 🧟 QUIZ 🧟‍♀️ PRESENTATION 🧟‍♀️ ASSIGNMENT")
    st.markdown("**Faculty of Basic Sciences samne hai, wahan pahunchna hai!**")
