import dill
from .search_engine import PromptSearchEngine
from .data.dataset import PromptDataset


def run():
    """
    Initialize the PromptSearchEngine with prompts from the specified dataset,
    serialize the engine, and save it to a file.

    This function performs the following steps:
    1. Loads a dataset of prompts using the PromptDataset class.
    2. Initializes the PromptSearchEngine with the loaded prompts.
    3. Serializes the PromptSearchEngine instance using dill.
    4. Saves the serialized engine to a file named 'engine.pickle'.
    """

    prompt_dataset = PromptDataset("Gustavosta/Stable-Diffusion-Prompts")
    prompt_dataset.load()
    prompts = prompt_dataset.get_prompts()
    engine = PromptSearchEngine(prompts)

    serialized_engine = dill.dumps(engine)

    with open("engine.pickle", "wb") as file:
        file.write(serialized_engine)
