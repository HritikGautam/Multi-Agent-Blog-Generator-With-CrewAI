import os
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer, llm
from crewai.memory import Memory

memory = Memory(
    llm=llm
)

## Forming the tech focused crew with some enhanced configuration
blog_crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    #Token limit for the crew's operations, ensuring efficient use of resources
    memory=False,
)

## starting the task execution process wiht enhanced feedback

# result = blog_crew.kickoff(inputs={"topic": "AI in space and cosmology"})
# print(result)
