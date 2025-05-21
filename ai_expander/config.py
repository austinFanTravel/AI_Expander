"""Configuration settings and default values for the AI Expander module."""

# Default model to use for embeddings (using a lightweight model)
DEFAULT_MODEL = "all-MiniLM-L6-v2"  # Small but effective model for semantic similarity

# Default similarity threshold for semantic matching
DEFAULT_SIMILARITY_THRESHOLD = 0.75

# Common location-based synonyms
LOCATION_SYNONYMS = {
    # US Cities
    "NYC": ["New York", "New York City", "The Big Apple", "NY"],
    "LA": ["Los Angeles", "City of Angels"],
    "SF": ["San Francisco", "The City", "Frisco"],
    "CHI": ["Chicago", "Windy City"],
    "MIA": ["Miami"],
    "LAS": ["Las Vegas", "Vegas"],
    
    # International
    "LON": ["London", "London, UK", "London, England"],
    "PAR": ["Paris", "Paris, France"],
    "TYO": ["Tokyo", "Tokyo, Japan"],
    "SYD": ["Sydney", "Sydney, Australia"],
    
    # Common abbreviations
    "US": ["USA", "United States", "United States of America"],
    "UK": ["United Kingdom", "Great Britain", "Britain", "England", "GB"],
}

# Common travel-related terms that might need expansion
TRAVEL_TERMS = {
    "hotel": ["accommodation", "lodging", "inn", "motel"],
    "flight": ["airfare", "airline ticket", "plane ticket"],
    "vacation": ["holiday", "trip", "getaway"],
    "beach": ["seaside", "shore", "coast"],
    "mountain": ["alpine", "highland", "peak"],
}

# Combine all default synonyms
DEFAULT_SYNONYMS = {**LOCATION_SYNONYMS, **TRAVEL_TERMS}
