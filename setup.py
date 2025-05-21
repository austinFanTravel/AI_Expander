from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai_expander",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python module for semantic expansion of search terms using OpenAI's embeddings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai_expander",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.20.0",
        "sentence-transformers>=2.2.2",
        "torch>=2.0.0",
        "scikit-learn>=1.0.0",  # For cosine similarity
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords="nlp semantic-search openai embeddings search-expansion",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ai_expander/issues",
        "Source": "https://github.com/yourusername/ai_expander",
    },
)
