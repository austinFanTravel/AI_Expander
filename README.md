# AI Expander

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python module for semantic expansion of search terms using OpenAI's embeddings. This package helps improve search relevance by expanding queries with synonyms and semantically similar terms.

## Features

- **Semantic Expansion**: Uses OpenAI's embeddings to find semantically similar terms
- **Custom Synonyms**: Built-in support for location-based synonyms and custom term mappings
- **Easy Integration**: Simple API that can be easily integrated into existing projects
- **Configurable**: Adjust similarity thresholds and models to suit your needs

## Installation

1. Install the package using pip:
   ```bash
   pip install git+https://github.com/yourusername/ai_expander.git
   ```

2. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Quick Start

```python
from ai_expander import SemanticExpander

# Initialize the expander
expander = SemanticExpander()

# Expand a single term
expanded = expander.expand_terms("NYC")
print(expanded)
# Output: ['new york', 'new york city', 'nyc', 'the big apple']

# Add custom synonyms
custom_synonyms = {
    "beach": ["seaside", "shore"],
    "vacation": ["holiday"]
}
expander.add_synonyms(custom_synonyms)

# Expand multiple terms
expanded = expander.expand_terms(["beach vacation"])
print(expanded)
# Output: ['beach', 'holiday', 'seaside', 'shore', 'vacation']
```

## Documentation

### SemanticExpander Class

#### Initialization

```python
expander = SemanticExpander(
    api_key=None,               # Optional: Your OpenAI API key
    model="text-embedding-3-small",  # The OpenAI model to use
    similarity_threshold=0.75,   # Minimum similarity score (0-1)
    custom_synonyms=None        # Optional: Dictionary of custom synonyms
)
```

#### Methods

- `add_synonyms(synonyms)`: Add custom synonyms to the expander
- `expand_term(term)`: Expand a single term
- `expand_terms(terms)`: Expand a list of terms

### Configuration

The module comes with default configurations in `config.py`, including:

- Default model: `text-embedding-3-small`
- Default similarity threshold: `0.75`
- Predefined location-based synonyms (e.g., "NYC" → ["New York", "New York City"])
- Common travel-related terms

## Examples

See the [example.py](example.py) file for more usage examples.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
