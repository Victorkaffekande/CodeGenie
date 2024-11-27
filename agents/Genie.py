import autogen
from autogen.coding import LocalCommandLineCodeExecutor
from Config import LLM_CONFIG


assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=LLM_CONFIG,
    system_message="""You are a helpful code assistant who writes code and makes sure it works.""",
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        # the executor to run the generated code
        "executor": LocalCommandLineCodeExecutor(work_dir="coding"),
    },
)

chat_res = user_proxy.initiate_chat(
    assistant,
    message="""Write a Python function that takes a list of numbers and returns the average of the numbers.""",
    summary_method="reflection_with_llm",
)
