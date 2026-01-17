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
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "github_url": "https://github.com/YOUR_USERNAME/YOUR_REPO",  # Update this
    "show_toc_level": 2,
    "navigation_depth": 3,
    "show_nav_level": 2,
    "navbar_align": "left",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/YOUR_USERNAME/YOUR_REPO",  # Update this
            "icon": "fa-brands fa-github",
        },
    ],
    "logo": {
        "text": "Deep Learning Journey",
    },
    "footer_start": ["copyright"],
    "footer_end": ["theme-version"],
}

html_static_path = ['_static']
html_css_files = ['custom.css']

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
