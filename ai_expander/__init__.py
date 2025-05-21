"""
AI Expander - A Python module for semantic expansion of search terms.

This module provides the SemanticExpander class which can be used to expand
search terms semantically using OpenAI's embeddings and custom synonym mappings.
"""

from .expander import SemanticExpander

__version__ = "0.1.0"
__all__ = ['SemanticExpander']
