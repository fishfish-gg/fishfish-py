# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'fishfish'
copyright = '2022, fishfish.gg'
authors = ['fishfish-gg']
release = '0.1.0'

# might not need this
# master_doc = "index"

# thanks, Danny
with open("../fishfish/__init__.py", "r") as fp:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fp.read(), re.MULTILINE
    ).group(1)


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
}

autodoc_mock_imports = ["requests", "aiohttp"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_static_path = ['_static']


# hi, I hope you like the docs
#  - nwunder
