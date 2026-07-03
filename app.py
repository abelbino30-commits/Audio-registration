import streamlit as st
from pydub import AudioSegment
import io

# Page Configuration
st.set_page_config(
    page_title="Audio Speed Studio",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Audio Speed Studio")
st.write("Upload an audio file and change its playback speed.")

# Upload Audio
uploaded_file = st.file_uploader(
    "Choose an audio file...",
    type=["mp3", "wav", "ogg"]
)

if uploaded_file is not None:

    # Load audio
    audio = AudioSegment.from_file(uploaded_file)

    st.sidebar.header("🎚 Audio Controls")

    speed = st.sidebar.slider(
        "Playback Speed",
        min_value=0.5,
        max_value=2.0,
        value=1.0,
        step=0.1
    )

    # Change playback speed
    modified_audio = audio._spawn(
        audio.raw_data,
        overrides={
            "frame_rate": int(audio.frame_rate * speed)
        }
    ).set_frame_rate(audio.frame_rate)

    # Audio Information
    st.subheader("🎧 Audio Information")
    st.write(f"Duration: {len(audio)/1000:.2f} seconds")
    st.write(f"Channels: {audio.channels}")
    st.write(f"Frame Rate: {audio.frame_rate} Hz")

    st.subheader("▶ Original Audio")
    st.audio(uploaded_file)

    # Export modified audio
    buffer = io.BytesIO()
    modified_audio.export(buffer, format="mp3")
    buffer.seek(0)

    st.subheader("⏩ Modified Audio")
    st.audio(buffer)

    st.download_button(
        label="📥 Download Modified Audio",
        data=buffer,
        file_name="modified_audio.mp3",
        mime="audio/mpeg"
    )

else:
    st.info("🎶 Upload an audio file to begin.")
