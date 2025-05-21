"""
SemanticExpander class for expanding search terms using semantic similarity with SentenceTransformers.
"""

import os
from typing import Dict, List, Optional, Union, Set, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
from . import config


class SemanticExpander:
    """
    A class for expanding search terms semantically using OpenAI's embeddings.
    
    This class provides methods to expand search terms using both predefined synonyms
    and semantic similarity from OpenAI's embeddings.
    """
    
    def __init__(
        self,
        model_name: str = config.DEFAULT_MODEL,
        similarity_threshold: float = config.DEFAULT_SIMILARITY_THRESHOLD,
        custom_synonyms: Optional[Dict[str, List[str]]] = None,
        device: str = 'cpu'
    ):
        """
        Initialize the SemanticExpander with SentenceTransformers.
        
        Args:
            model_name: The name of the SentenceTransformer model to use.
            similarity_threshold: The minimum similarity score (0-1) for semantic matches.
            custom_synonyms: Optional dictionary of custom synonyms to add to the default ones.
            device: Device to run the model on ('cpu' or 'cuda' for GPU).
        """
        self.similarity_threshold = similarity_threshold
        self.device = device
        
        # Load the SentenceTransformer model
        print(f"Loading model: {model_name}")
        self.model = SentenceTransformer(model_name, device=device)
        
        # Initialize synonyms with defaults and any custom ones
        self.synonyms = config.DEFAULT_SYNONYMS.copy()
        if custom_synonyms:
            self.add_synonyms(custom_synonyms)
            
        # Pre-compute embeddings for all known terms
        self._init_embeddings()
    
    def add_synonyms(self, synonyms: Dict[str, Union[str, List[str]]]) -> None:
        """
        Add custom synonyms to the expander.
        
        Args:
            synonyms: Dictionary where keys are terms and values are either a single 
                    synonym or a list of synonyms.
        """
        for term, values in synonyms.items():
            if term not in self.synonyms:
                self.synonyms[term] = []
            
            if isinstance(values, str):
                values = [values]
                
            # Add only unique values
            for value in values:
                if value not in self.synonyms[term]:
                    self.synonyms[term].append(value)
    
    def _init_embeddings(self) -> None:
        """Pre-compute embeddings for all known terms."""
        self.term_embeddings = {}
        all_terms = set()
        
        # Collect all unique terms from synonyms
        for term, synonyms in self.synonyms.items():
            all_terms.add(term)
            all_terms.update(synonyms)
            
        # Convert to list and compute embeddings in batches
        if all_terms:
            term_list = list(all_terms)
            embeddings = self.model.encode(term_list, convert_to_numpy=True, show_progress_bar=False)
            self.term_embeddings = {term: emb for term, emb in zip(term_list, embeddings)}
    
    def _get_embedding(self, text: str) -> np.ndarray:
        """
        Get the embedding vector for a given text using SentenceTransformer.
        
        Args:
            text: The text to get the embedding for.
            
        Returns:
            A numpy array representing the embedding vector.
        """
        return self.model.encode([text], convert_to_numpy=True)[0]
    
    def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """
        Calculate the cosine similarity between two vectors.
        
        Args:
            vec1: First vector.
            vec2: Second vector.
            
        Returns:
            The cosine similarity between the two vectors (0-1).
        """
        # Reshape for sklearn's cosine_similarity
        vec1 = vec1.reshape(1, -1)
        vec2 = vec2.reshape(1, -1)
        return cosine_similarity(vec1, vec2)[0][0]
    
    def expand_term(self, term: str) -> Set[str]:
        """
        Expand a single term using both predefined synonyms and semantic similarity.
        
        Args:
            term: The term to expand.
            
        Returns:
            A set of expanded terms including the original term.
        """
        # Start with the original term and any direct synonyms
        expanded = {term.lower()}
        
        # Add any direct synonyms (case-insensitive)
        term_lower = term.lower()
        for key, values in self.synonyms.items():
            if key.lower() == term_lower:
                expanded.update(v.lower() for v in values)
        
        # If we already have synonyms, return them
        if len(expanded) > 1:
            return expanded
        
        # Otherwise, try to find semantically similar terms
        try:
            # Get embedding for the input term
            query_embedding = self._get_embedding(term)
            
            # Check against all known terms
            for key, key_embedding in self.term_embeddings.items():
                similarity = self._cosine_similarity(query_embedding, key_embedding)
                
                if similarity >= self.similarity_threshold:
                    expanded.add(key.lower())
                    if key in self.synonyms:
                        expanded.update(v.lower() for v in self.synonyms[key])
                    
        except Exception as e:
            # If there's an error, just return what we have
            print(f"Warning: Could not get semantic expansion for '{term}': {str(e)}")
        
        return expanded
    
    def expand_terms(self, terms: Union[str, List[str]]) -> List[str]:
        """
        Expand a list of terms, removing duplicates in the result.
        
        Args:
            terms: A single term or a list of terms to expand.
            
        Returns:
            A list of expanded terms, with duplicates removed.
        """
        if isinstance(terms, str):
            terms = [terms]
            
        expanded_terms = set()
        for term in terms:
            expanded_terms.update(self.expand_term(term))
            
        return sorted(list(expanded_terms))
