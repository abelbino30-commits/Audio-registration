import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Audio Player Studio",
    page_icon="🎵",
    layout="centered",
)

st.title("🎵 Audio Player Studio")
st.write("Upload an audio file and listen to it instantly!")

# Upload Audio
uploaded_file = st.file_uploader(
    "Choose an audio file...",
    type=["mp3", "wav", "ogg"],
)

if uploaded_file is not None:
    st.subheader("🎧 Audio Player")
    st.audio(uploaded_file)

    st.subheader("📄 File Information")
    st.write(f"**Filename:** {uploaded_file.name}")
    st.write(f"**File Type:** {uploaded_file.type}")
    st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")

    st.download_button(
        label="📥 Download Audio",
        data=uploaded_file.getvalue(),
        file_name=uploaded_file.name,
        mime=uploaded_file.type,
        use_container_width=True,
    )
else:
    st.info("🎶 Upload an audio file to begin.")
