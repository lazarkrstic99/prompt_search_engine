from typing import Sequence

import numpy as np
from sentence_transformers import SentenceTransformer


class Vectorizer:
    """
    The Vectorizers role is to transform textual prompts into numerical vectors that can be
    compared in a high-dimensional space. This transformation allows the system to quantify the
    similarity between different prompts effectively.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        """
        Initialize the vectorizer with a pre-trained embedding model.

        Args:
            model_name (str): The pre-trained embedding model to use for transforming prompts.
                This can be any model that provides a method to convert texts into numerical vectors.
        """

        self.model = SentenceTransformer(model_name)

    def transform(self, prompts: Sequence[str]) -> np.ndarray:
        """
        Transform texts into numerical vectors using the specified model.

        Args:
            prompts (Sequence[str]): The sequence of raw corpus prompts to be transformed.

        Returns:
            np.ndarray: A numpy array containing the vectorized prompts. Each row corresponds to the
                        vector representation of a prompt.
        """

        return self.model.encode(list(prompts))

    @staticmethod
    def cosine_similarity(
        query_vector: np.ndarray, corpus_vectors: np.ndarray
    ) -> np.ndarray:
        """
        Calculate cosine similarity between a query vector and a set of corpus vectors.

        Args:
            query_vector (np.ndarray): A numpy array representing the vector of the query prompt.
            corpus_vectors (np.ndarray): A numpy array representing the vectors of the corpus prompts.
                                         Each row corresponds to the vector representation of a corpus prompt.

        Returns:
            np.ndarray: A numpy array containing the cosine similarity scores between the query vector and each
                of the corpus vectors.
        """

        query_norm = query_vector / np.linalg.norm(query_vector)
        corpus_norms = corpus_vectors / np.linalg.norm(
            corpus_vectors, axis=1, keepdims=True
        )

        return np.dot(corpus_norms, query_norm.T).flatten()
