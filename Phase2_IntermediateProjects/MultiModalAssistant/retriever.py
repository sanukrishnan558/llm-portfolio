# retriever.py
from typing import List, Dict
import os

# Use sentence-transformers for text embeddings + faiss for vector search
try:
    from sentence_transformers import SentenceTransformer
    import faiss
    _HAS_SBT = True
except Exception:
    _HAS_SBT = False


class Retriever:
    def __init__(self, index_path: str = "faiss_index.bin", model_name: str = "all-MiniLM-L6-v2"):
        self.index_path = index_path
        self.model_name = model_name
        self.model = None
        self.index = None
        self.corpus = []  # list of dicts {"id":..., "text":...}

        if _HAS_SBT:
            self.model = SentenceTransformer(self.model_name)
            if os.path.exists(index_path):
                self._load_index(index_path)

    def _load_index(self, path: str):
        try:
            self.index = faiss.read_index(path)
            # corpus must be loaded by user or pre-saved. For starter, we'll assume corpus is saved next to index as .npy/.json
        except Exception as e:
            print("Failed to load index:", e)
            self.index = None

    def build(self, texts: List[str], ids: List[str] = None):
        """Build a FAISS index from list of texts. Overwrites existing index_path."""
        if not _HAS_SBT:
            raise RuntimeError("sentence_transformers / faiss not installed")

        if ids is None:
            ids = [str(i) for i in range(len(texts))]

        embeddings = self.model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
        dim = embeddings.shape[1]
        index = faiss.IndexFlatIP(dim)  # inner product (assume normalized)

        import numpy as np
        faiss.normalize_L2(embeddings)
        index.add(embeddings)
        faiss.write_index(index, self.index_path)
        self.index = index
        self.corpus = [{"id": ids[i], "text": texts[i]} for i in range(len(texts))]

    def retrieve(self, query: str, top_k: int = 4) -> List[Dict]:
        """Return list of {id, text, score} for top_k matches."""
        if not _HAS_SBT or self.index is None:
            # fallback: return empty list
            return []

        q_emb = self.model.encode([query], convert_to_numpy=True)
        import numpy as np
        faiss.normalize_L2(q_emb)
        D, I = self.index.search(q_emb, top_k)
        results = []
        for score, idx in zip(D[0], I[0]):
            try:
                doc = self.corpus[idx]
            except Exception:
                doc = {"id": str(idx), "text": ""}
            results.append({"id": doc.get("id"), "text": doc.get("text"), "score": float(score)})
        return results
