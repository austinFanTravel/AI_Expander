# AI Expander

A Python module for semantically expanding search terms using NLP and custom mappings. This module is particularly useful for web scraping applications where you want to improve search result relevance by including synonyms and related terms.

## Features

- **Semantic Expansion**: Uses spaCy's word vectors to find semantically similar terms
- **Custom Mappings**: Easily add your own term mappings
- **Location-Aware**: Built-in support for common location-based expansions
- **Case Insensitive**: Handles case variations automatically
- **Extensible**: Simple API for adding new expansion rules

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ai_expander.git
   cd ai_expander
   ```

2. Install the package in development mode:
   ```bash
   pip install -e .
   ```

3. Install the required spaCy model:
   ```bash
   python -m spacy download en_core_web_md
   ```

## Quick Start

```python
from ai_expander import SemanticExpander

# Create an instance
# You can optionally pass custom mappings
expander = SemanticExpander()

# Expand a term
expanded_terms = expander.expand("NYC")
print(expanded_terms)
# Output might include: {'New York', 'New York City', 'NYC', 'The Big Apple'}

# Add custom mappings
expander.add_mapping("austin", ["ATX", "Live Music Capital"])
print(expander.expand("austin"))
# Output: {'austin', 'ATX', 'Live Music Capital'}
```

## API Reference

### SemanticExpander

#### `__init__(self, custom_mapping: Optional[Dict[str, List[str]]] = None)`
Initialize the SemanticExpander with optional custom mappings.

#### `expand(self, term: str, include_original: bool = True) -> Set[str]`
Expand a search term into a set of related terms.

#### `add_mapping(self, term: str, expansions: List[str])`
Add or update a term mapping.

#### `get_mapping(self, term: str) -> List[str]`
Get the expansions for a given term.

## Running Tests

```bash
python -m unittest ai_expander/test_expander.py
```

## License

MIT

