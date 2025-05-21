import spacy
from typing import List, Dict, Set, Optional

class SemanticExpander:
    """
    A class for semantically expanding search terms using NLP and custom synonym mappings.
    
    This class provides functionality to expand terms based on built-in NLP capabilities
    and a customizable dictionary of location-based synonyms.
    """
    
    def __init__(self, custom_mapping: Optional[Dict[str, List[str]]] = None):
        """
        Initialize the SemanticExpander with optional custom mappings.
        
        Args:
            custom_mapping: Optional dictionary of custom term mappings to extend or override defaults.
        """
        # Load the English language model
        self.nlp = spacy.load('en_core_web_md')
        
        # Default location-based mappings (can be extended or overridden)
        self.location_mapping = {
            'nyc': ['New York', 'New York City', 'NYC', 'The Big Apple', 'Manhattan'],
            'la': ['Los Angeles', 'LA', 'City of Angels', 'LAX'],
            'sf': ['San Francisco', 'SF', 'Bay Area', 'Frisco'],
            'dc': ['Washington DC', 'Washington', 'District of Columbia', 'The Capital'],
            'chi': ['Chicago', 'Windy City', 'Chi-Town'],
        }
        
        # Update with any custom mappings provided
        if custom_mapping:
            self.location_mapping.update(
                {k.lower(): [v.lower() if isinstance(v, str) else [i.lower() for i in v] 
                for v in vs] for k, vs in custom_mapping.items()}
            )
    
    def expand(self, term: str, include_original: bool = True) -> Set[str]:
        """
        Expand a search term into a set of related terms.
        
        Args:
            term: The input term to expand
            include_original: Whether to include the original term in the results
            
        Returns:
            A set of expanded terms including the original term (if include_original is True)
        """
        term = term.strip()
        if not term:
            return set()
            
        # Initialize results with the original term if requested
        results = {term} if include_original else set()
        
        # Check for direct matches in location mapping (case-insensitive)
        lower_term = term.lower()
        if lower_term in self.location_mapping:
            results.update(self.location_mapping[lower_term])
        
        # Also check if any key contains or is contained within the term
        for key, expansions in self.location_mapping.items():
            if key in lower_term or lower_term in key:
                results.update(expansions)
        
        # Use spaCy to find similar terms based on word vectors
        doc = self.nlp(term)
        
        # Add similar terms based on word vectors
        if doc.vector_norm:
            similar_words = [w.text for w in self.nlp.vocab.vectors.most_similar(
                doc.vector.reshape(1, -1), n=3)[0][0]]
            results.update(similar_words)
        
        return results
    
    def add_mapping(self, term: str, expansions: List[str]):
        """
        Add or update a term mapping.
        
        Args:
            term: The term to map from (case-insensitive)
            expansions: List of terms to map to
        """
        self.location_mapping[term.lower()] = [e.lower() for e in expansions]
    
    def get_mapping(self, term: str) -> List[str]:
        """
        Get the expansions for a given term.
        
        Args:
            term: The term to look up
            
        Returns:
            List of expanded terms, or empty list if term not found
        """
        return self.location_mapping.get(term.lower(), [])
