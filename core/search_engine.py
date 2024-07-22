from typing import List, Sequence, Tuple

import faiss
import numpy as np

from core.vectorizer import Vectorizer


class PromptSearchEngine:
    """
    The PromptSearchEngine is responsible for finding the most similar prompts to a given query
    by leveraging vectorized representations of the prompts and a similarity search index.
    """

    def __init__(self, prompts: Sequence[str]) -> None:
        """
        Initialize the PromptSearchEngine with a list of prompts.

        Args:
            prompts (Sequence[str]): The sequence of raw corpus prompts to be indexed for similarity search.
        """

        self.vectorizer = Vectorizer()
        self.corpus_vectors = self.vectorizer.transform(prompts)
        self.corpus = prompts

        self.corpus_vectors = self.corpus_vectors / np.linalg.norm(
            self.corpus_vectors, axis=1, keepdims=True
        )

        d = self.corpus_vectors.shape[1]
        self.index = faiss.IndexFlatIP(d)
        self.index.add(self.corpus_vectors.astype("float32"))

    def most_similar(self, query: str, n: int = 5) -> List[Tuple[float, str]]:
        """
        Find the most similar prompts to a given query.

        Args:
            query (str): The query prompt to search for similar prompts.
            n (int, optional): The number of similar prompts to retrieve. Defaults to 5.

        Returns:
            List[Tuple[float, str]]: A list of tuples containing the similarity score and the corresponding prompt.
        """

        query_vector = self.vectorizer.transform([query]).astype("float32")
        query_vector = query_vector / np.linalg.norm(query_vector)
        distances, indices = self.index.search(query_vector, n)

        return [(distances[0][i], self.corpus[indices[0][i]]) for i in range(n)]
