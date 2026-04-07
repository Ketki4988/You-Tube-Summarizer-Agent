pip uninstall youtube-transcript-api -y
pip install youtube-transcript-api

# !pip install Phidata Groq youtube_transcript_api dotenv jira pycountry
!pip install Phidata Groq dotenv jira pycountry

import os
# from google.colab import userdata

# os.environ["GROQ_API_KEY"] = userdata.get('GROQ_API_KEY')
# os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')

os.environ["GROQ_API_KEY"] = "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"

from phi.agent import Agent
from phi.model.groq import Groq
# from phi.model.openai import OpenAIChat
from phi.tools.youtube_tools import YouTubeTools
from dotenv import load_dotenv

agent = Agent(
    # model=Groq(id="llama-3.1-8b-instant"),
    model=Groq(id="llama-3.3-70b-versatile"),  ## Toggle with different LLM model
    # model=OpenAIChat(id="gpt-4o"),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    # debug_mode=True,
    description="""
                  You are a YouTube summarization agent.

                  Steps:
                  1. First try to get captions using get_youtube_video_captions.
                  2. If captions are available → summarize using them.
                  3. If captions are NOT available:
                    - Use get_youtube_video_data
                    - Use title, description, and metadata
                    - Generate a meaningful summary (do NOT say captions unavailable)
                  4. Always provide a useful summary to the user.
"""
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=tPYj3fFJGjk", markdown=True, stream=True)
# agent.print_response("Use the tool to get captions and summarize this video. URL: https://www.youtube.com/watch?v=tPYj3fFJGjk", markdown=True, stream=True)

### Different models in Groq (optional)**
# Few models in Groq.  More on - https://console.groq.com/docs/models
# 1. gemma2-9b-it
# 2. llama-3.3-70b-versatile
# 3. llama-3.1-8b-instant
# 4. llama3-70b-8192
