import dill
from .search_engine import PromptSearchEngine
from .data.dataset import PromptDataset


def run():
    """
    TODO
    """

    prompt_dataset = PromptDataset("Gustavosta/Stable-Diffusion-Prompts")
    prompt_dataset.load()
    prompts = prompt_dataset.get_prompts()
    engine = PromptSearchEngine(prompts)

    serialized_engine = dill.dumps(engine)

    with open("engine.pickle", "wb") as file:
        file.write(serialized_engine)

run()
