from datasets import load_dataset


class PromptDataset:
    """
    A class to manage the loading and processing of datasets from the Hugging Face `datasets` library.
    """

    def __init__(self, dataset_name: str):
        """
        Initializes the PromptDataset with a specific dataset name.

        Args:
            dataset_name (str): The name of the dataset to be loaded. This should be a valid identifier
            as recognized by the Hugging Face datasets library.
        """

        self.dataset_name = dataset_name
        self.dataset = None

    def load(self):
        """
        Loads the dataset specified by the dataset_name attribute from the Hugging Face datasets library,
        with additional arguments for configurations and dataset splits.

        Returns:
            Dataset: The loaded dataset object, which is also stored in the `dataset` attribute.
        """

        self.dataset = load_dataset(self.dataset_name)

        return self.dataset

    def get_prompts(self):
        """
        Retrieves a list of prompts from the loaded dataset. Assumes the dataset has a specified split containing the 'Prompt' field.

        Returns:
            List[str]: A list of prompts extracted from the dataset.

        Raises:
            ValueError: If the dataset is not loaded prior to calling this method.
        """

        if self.dataset is None:
            raise ValueError("Dataset not loaded. Call the load() method first.")

        return [item['Prompt'] for item in self.dataset['test']]

