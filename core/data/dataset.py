from datasets import load_dataset


class PromptDataset:
    """
    TODO
    """

    def __init__(self, dataset_name: str):
        """
        TODO
        """

        self.dataset_name = dataset_name
        self.dataset = None

    def load(self):
        """
        TODO
        """

        self.dataset = load_dataset(self.dataset_name)

        return self.dataset

    def get_prompts(self):
        """
        TODO
        """

        if self.dataset is None:
            raise ValueError("Dataset not loaded. Call the load() method first.")

        return [item['Prompt'] for item in self.dataset['test']]

