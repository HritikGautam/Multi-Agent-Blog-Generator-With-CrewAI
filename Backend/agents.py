from crewai import Agent
from crewai import LLM
from tools import tool
from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
import os
load_dotenv()


# ## call the gemini models
# llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=os.getenv("GOOGLE_API_KEY"))
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=200,
    temperature=0.2,
)

# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    verbose=False,
    max_iter = 2,
    # memory=True,
    memory=False,
    backstory=(
      "Tech researcher discovering trends."
        # "Driven by curiosity, you're at the forefront of"
        # "innovation, eager to explore and share knowledge that could change"
        # "the world."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=False,
  max_iter = 2,
  # memory=True,
  memory=False,
  backstory=(
    "Tech writer crafting engaging stories."
    # "With a flair for simplifying complex topics, you craft"
    # "engaging narratives that captivate and educate, bringing new"
    # "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)

