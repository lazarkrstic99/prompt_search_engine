from typing import List, Sequence, Tuple
import numpy as np
import faiss
from core.vectorizer import Vectorizer


class PromptSearchEngine(object):
    """
    TODO
    """

    def __init__(self, prompts: Sequence[str]) -> None:
        """
        TODO
        """

        self.vectorizer = Vectorizer()
        self.corpus_vectors = self.vectorizer.transform(prompts)
        self.corpus = prompts

        self.corpus_vectors = self.corpus_vectors / np.linalg.norm(self.corpus_vectors, axis=1, keepdims=True)

        d = self.corpus_vectors.shape[1]
        self.index = faiss.IndexFlatIP(d)
        self.index.add(self.corpus_vectors.astype('float32'))

    def most_similar(self, query: str, n: int = 5) -> List[Tuple[float, str]]:
        """
        TODO
        """

        query_vector = self.vectorizer.transform([query]).astype('float32')
        query_vector = query_vector / np.linalg.norm(query_vector)
        distances, indices = self.index.search(query_vector, n)

        return [(distances[0][i], self.corpus[indices[0][i]]) for i in range(n)]
