from pydantic import BaseModel,Field

class File(BaseModel):
    path: str= Field(description="The name of app to be built")
    filename: str= Field(description="The purpose of file . eg 'main application logic' 'data processing logic'")



from pydantic import BaseModel,Field

class Plan(BaseModel):
    name: str = Field(
        description="Unique and meaningful name of the software project."
    )

    description: str = Field(
        description="Detailed project requirements, business objective, user workflow, and expected behavior of the application."
    )

    tech_stack: list[str] = Field(
        description="Recommended technology stack including frontend, backend, database, APIs, and deployment tools."
    )

    features: list[str] = Field(
        description="Complete list of functional requirements and user-facing features that the application must support."
    )

    files: list[File] = Field(
        description="Structured list of all files required for the project implementation, including file paths, purposes, and code contents."
    )
