# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'Deep Learning Journey'
copyright = '2025, Fatih Onay, PhD'
author = 'Fatih Onay'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',                    # Markdown support
    'sphinx.ext.autodoc',             # Auto-generate API docs
    'sphinx.ext.napoleon',            # Google/NumPy docstring support
    'sphinx.ext.viewcode',            # Add links to source code
    'sphinx.ext.mathjax',             # Math rendering
    'sphinx.ext.intersphinx',         # Link to other projects
    'sphinx_copybutton',              # Copy button for code blocks
    'nbsphinx',                       # Jupyter notebook support
]

# MyST Parser configuration for Markdown
myst_enable_extensions = [
    "dollarmath",      # $...$ and $$...$$ for math
    "amsmath",         # LaTeX math environments
    "colon_fence",     # ::: for admonitions
    "deflist",         # Definition lists
    "html_image",      # HTML image syntax
    "tasklist",        # GitHub-style task lists
]

# Source file suffixes
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/YOUR_USERNAME/YOUR_REPO",
    "use_repository_button": True,
    "use_download_button": True,
    "show_navbar_depth": 2,
    "home_page_in_toc": True,
    # This hides the secondary sidebar on the right if it's empty, making it cleaner
    "show_toc_level": 2, 
    'logo_width': '20px',
}

# Keep these lines
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = "_static/logoDeep.png"

# -- Intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'mne': ('https://mne.tools/stable/', None),
}

# -- nbsphinx configuration --------------------------------------------------
nbsphinx_execute = 'never'  # Don't execute notebooks during build
nbsphinx_allow_errors = True

# -- Copy button configuration -----------------------------------------------
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
