import dill
from data.dataset import PromptDataset
from core.search_engine import PromptSearchEngine


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
