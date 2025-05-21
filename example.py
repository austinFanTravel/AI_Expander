"""
Example usage of the SemanticExpander class from the ai_expander package.
"""

from ai_expander import SemanticExpander
import torch

def main():
    # Check if CUDA is available
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")
    
    # Initialize the expander
    expander = SemanticExpander(device=device)
    
    # Example 1: Basic usage with predefined synonyms
    print("Example 1: Basic synonym expansion")
    terms = ["NYC", "hotel"]
    expanded = expander.expand_terms(terms)
    print(f"Original terms: {terms}")
    print(f"Expanded terms: {expanded}")
    print("-" * 80)
    
    # Example 2: Adding custom synonyms
    print("Example 2: Adding custom synonyms")
    custom_synonyms = {
        "beach": ["seaside", "shore"],
        "vacation": ["holiday"]
    }
    expander.add_synonyms(custom_synonyms)
    
    terms = ["beach vacation"]
    expanded = expander.expand_terms(terms)
    print(f"Original terms: {terms}")
    print(f"Expanded terms: {expanded}")
    print("-" * 80)
    
    # Example 3: Semantic expansion for terms not in the synonyms dictionary
    print("Example 3: Semantic expansion")
    terms = ["The Big Apple"]  # Not in our synonyms, but should match "NYC"
    expanded = expander.expand_terms(terms)
    print(f"Original terms: {terms}")
    print(f"Expanded terms: {expanded}")
    print("-" * 80)
    
    # Example 4: Expand multiple terms at once
    print("Example 4: Multiple terms expansion")
    terms = ["NYC", "hotel", "beach"]
    expanded = expander.expand_terms(terms)
    print(f"Original terms: {terms}")
    print(f"Expanded terms: {expanded}")
    print("-" * 80)

if __name__ == "__main__":
    main()
