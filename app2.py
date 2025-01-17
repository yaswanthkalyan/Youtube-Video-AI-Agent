import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai

import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
import os
import yt_dlp  # Use yt-dlp for video downloads

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# Streamlit page configuration
st.set_page_config(
    page_title="Multimodal AI Agent - Video Summarizer",
    page_icon="🎥",
    layout="wide"
)
st.title("Youtube Video AI Summarizer Agent 🔗🎞️⏯️")
st.header("Using by Gemini 2.0 Flash Exp")


@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )


# Initialize the agent
multimodal_Agent = initialize_agent()


def download_youtube_video(video_url, output_path):
    ydl_opts = {
        'outtmpl': output_path,  # Use the provided output path
        'format': 'mp4',  # Ensure it downloads an MP4 format
        'overwrites': True,  # Force overwrite if the file exists
        'noprogress': True,  # Disable progress bar for cleaner logs
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


# Video link input
video_link = st.text_input(
    "Enter a YouTube video link",
    placeholder="Paste the YouTube video link here...",
    help="Provide a YouTube video link for AI analysis."
)

if video_link:
    try:
        with st.spinner("Downloading video..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
                output_path = temp_video.name
                download_youtube_video(video_link, output_path)
                video_path = output_path

        st.video(video_path, format="video/mp4", start_time=0)

        user_query = st.text_area(
            "What insights are you seeking from the video?",
            placeholder="Ask anything about the video content. The AI agent will analyze and gather additional context if needed.",
            help="Provide specific questions or insights you want from the video."
        )

        if st.button("🔍 Analyze Video", key="analyze_video_button"):
            if not user_query:
                st.warning("Please enter a question or insight to analyze the video.")
            else:
                try:
                    with st.spinner("Processing video and gathering insights..."):
                        # Upload and process video file
                        st.write("Uploading video for processing...")
                        processed_video = upload_file(video_path)
                        st.write(f"Initial file state: {processed_video.state.name}")

                        # Wait for the file to become ACTIVE
                        max_retries = 30
                        retries = 0
                        while processed_video.state.name == "PROCESSING" and retries < max_retries:
                            time.sleep(1)
                            retries += 1
                            processed_video = get_file(processed_video.name)
                            st.write(f"Current file state: {processed_video.state.name}")

                        # Check if the file is ACTIVE
                        if processed_video.state.name != "ACTIVE":
                            raise ValueError("The uploaded video file is not in an ACTIVE state.")

                        # Prompt generation for analysis
                        analysis_prompt = (
                            f"""
                            Analyze the uploaded video for content and context.
                            Respond to the following query using video insights and supplementary web research:
                            {user_query}

                            Provide a detailed, user-friendly, and actionable response. Please do not hallucinate.
                            """
                        )

                        # AI agent processing
                        response = multimodal_Agent.run(analysis_prompt, videos=[processed_video])

                    # Display the result
                    st.subheader("Analysis Result")
                    st.markdown(response.content)

                except Exception as error:
                    st.error(f"An error occurred during analysis: {error}")
                finally:
                    # Clean up temporary video file
                    Path(video_path).unlink(missing_ok=True)
    except Exception as error:
        st.error(f"An error occurred while downloading the video: {error}")
else:
    st.info("Enter a YouTube video link to begin analysis.")

# Customize text area height
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
