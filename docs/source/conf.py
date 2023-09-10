# Configuration file for the Sphinx documentation builder.

# -- Project information

import sys 
import os

project = 'Pas-à-Pas Nubo'
copyright = '2023, MMoussaoui'
author = 'MMoussaoui'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'button',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
}
html_logo = '_static/logo.png'
html_css_files = [
    '_static/custom.css',
]
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

sys.path.insert(0, os.path.abspath('..'))