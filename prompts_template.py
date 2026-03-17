from langchain_core.prompts import PromptTemplate


template = PromptTemplate(
    template="""
    Please Summarize the Research paper titled "{paper_name}" with the following specifications:
    Explanation Style:{input_style}
    Explanation Length:{input_length}
    1.Mathematical details :
        Include relevant mathematical equations of present in the paper
        Explain the mathematical concept using simple,intuitive code snippets where applicable
    2.Analogies:
        Use relatable analogies to simplify complex idea
    If certain information is not available in the paper respond with :"Insufficient information available
    in the paper" instead of responding with random guesses.
    Ensure the summary is clear,accurate and aligned with the provided style and length.
    """,
    input_variables=["paper_name", "input_style", "input_length"],
)

template.save("template.json")
