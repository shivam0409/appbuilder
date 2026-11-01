from ast import List

from dotenv import load_dotenv;load_dotenv()
from langchain_groq import ChatGroq

from prompts import *
from states import *


llm=ChatGroq(model="openai/gpt-oss-120b")

resp=llm.with_structured_output(Plan).invoke(prompt)

def display_project(project):
    print(f"# {project.name}\n")

    print("## Description")
    print(project.description)

    print("\n## Tech Stack")
    for tech in project.tech_stack:
        print(f"- {tech}")

    print("\n## Features")
    for feature in project.features:
        print(f"- {feature}")

    print("\n## Files")
    for file in project.files:
        print(f"- {file.path}")

display_project(resp)
