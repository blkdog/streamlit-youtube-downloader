import streamlit as st
from pytubefix import YouTube


def main():
    st.title("YouTube Video Downloader")

    video_url = st.text_input("Enter the YouTube video URL:")

    try:
        if video_url:
            yt = YouTube(video_url)
            st.write(f"**Title:** {yt.title}")

            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

            if st.button("Download Video"):
                try:
                    with st.spinner("Downloading..."):
                        stream.download(output_path='/Users/rdm/Downloads')
                    st.success("Downloaded successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")




if __name__ == "__main__":
    main()
