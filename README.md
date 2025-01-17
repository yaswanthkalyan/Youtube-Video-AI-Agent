# Phidata Video AI Summarizer Agent 🔗

## Overview
The **Phidata Video AI Summarizer Agent** is a Streamlit-based application that leverages advanced AI models (Gemini 2.0 Flash Exp) to analyze YouTube videos. Users can input YouTube links and query the content for specific insights, enabling efficient understanding of video material. The application is powered by Google Generative AI and incorporates tools like DuckDuckGo for supplementary research.

## Features
- **YouTube Video Analysis**: Analyze content from YouTube videos by providing a link.
- **AI-Powered Insights**: Gain detailed and actionable insights using the Gemini 2.0 Flash Exp model.
- **User-Friendly Interface**: An intuitive Streamlit interface for uploading video links and entering queries.
- **Supplementary Web Research**: Integrated DuckDuckGo support for enriched responses.

## Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **AI Models**: Google Gemini 2.0 Flash Exp
- **Tools**: DuckDuckGo API, Google Generative AI
- **Video Processing**: yt-dlp

## Prerequisites
1. Python 3.8+
2. Pip (Python package manager)
3. [Google API Key](https://console.cloud.google.com/) for Generative AI
4. Environment variables configured via `.env` file:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/phidata-video-ai-summarizer.git
   cd phidata-video-ai-summarizer
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   ```bash
   touch .env
   ```
   Add the following content to `.env`:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the application in your browser (default: `http://localhost:8501`).
2. Paste a YouTube video link in the input field.
3. Enter your query about the video content.
4. Click the "Analyze Video" button to receive insights.

## File Structure
```
phidata-video-ai-summarizer/
├── app.py                 # Main application file
├── app2.py                # Main Application file for youtube video reading
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (ignored in Git)
└──README.md              # Project documentation
```

## Dependencies
- [Streamlit](https://streamlit.io/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Google Generative AI](https://console.cloud.google.com/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)

## Known Issues
1. **Video Processing Timeout**:
   - Large videos may take longer to process. If the file doesn't transition to `ACTIVE`, increase the timeout in `app.py`.
2. **File Compatibility**:
   - Ensure videos are in supported formats (e.g., MP4 with H.264 codec).

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added feature X"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- [Google Generative AI](https://ai.google/) for providing robust AI capabilities.
- [Streamlit](https://streamlit.io/) for the easy-to-use web application framework.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for reliable YouTube video downloads.

