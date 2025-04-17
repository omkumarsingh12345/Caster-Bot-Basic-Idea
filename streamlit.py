import streamlit as st
import cv2
from events import detect_event
from commentary import get_commentary
from tts_engine import speak

st.title("🎮 SpectraPlay - Real-Time AI Game Commentator")
tone = st.selectbox("Choose your Commentary Tone", ["Pro", "Funny", "Hype"])

video_file = "gameplay.mp4"
cap = cv2.VideoCapture(video_file)

frame_area = st.empty()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_area.image(frame, channels="BGR")

    event = detect_event(frame)
    if event:
        line = get_commentary(event, tone)
        st.write(f"🎙️ {line}")
        speak(line)
        break
