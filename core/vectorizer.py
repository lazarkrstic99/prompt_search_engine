from typing import Sequence
import numpy as np
from sentence_transformers import SentenceTransformer


class Vectorizer(object):
    """
    TODO
    """

    def __init__(self, model_name: str = 'all-MiniLM-L6-v2') -> None:
        """
        Initialize the vectorizer with a pre-trained embedding model.
        """

        self.model = SentenceTransformer(model_name)

    def transform(self, prompts: Sequence[str]) -> np.ndarray:
        """
        Transform texts into numerical vectors using the specified model.
        """

        return self.model.encode(list(prompts))

    @staticmethod
    def cosine_similarity(query_vector: np.ndarray, corpus_vectors: np.ndarray) -> np.ndarray:
        """
        Calculate cosine similarity between prompt vectors.
        """
        
        query_norm = query_vector / np.linalg.norm(query_vector)
        corpus_norms = corpus_vectors / np.linalg.norm(corpus_vectors, axis=1, keepdims=True)

        return np.dot(corpus_norms, query_norm.T).flatten()
