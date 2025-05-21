from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai_expander",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A semantic term expander for search and data enrichment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai_expander",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'spacy>=3.0.0',
    ],
    entry_points={
        'console_scripts': [
            'ai_expander=ai_expander.expander:main',
        ],
    },
)
