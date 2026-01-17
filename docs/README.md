# Documentation

This directory contains the Sphinx documentation for the Neural Variability Research project.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Build Documentation Locally

```bash
# On Linux/macOS
make html

# On Windows
make.bat html
```

### 3. View Documentation

Open `_build/html/index.html` in your browser.

## Directory Structure

```
docs/
├── .github/
│   └── workflows/
│       └── docs.yml          # GitHub Actions for auto-deployment
├── source/
│   ├── _static/
│   │   ├── custom.css        # Custom styling
│   │   └── images/           # Tutorial images
│   ├── _templates/           # Custom Sphinx templates
│   ├── api/
│   │   └── index.md          # API reference
│   ├── tutorials/
│   │   ├── deep_learning/
│   │   │   ├── index.md
│   │   │   └── exploring_cnns.md
│   │   ├── signal_processing/
│   │   │   └── index.md
│   │   └── index.md
│   ├── conf.py               # Sphinx configuration
│   └── index.md              # Main landing page
├── Makefile                  # Build commands (Linux/macOS)
├── make.bat                  # Build commands (Windows)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Adding New Content

### Adding a New Tutorial

1. Create a new `.md` file in the appropriate directory under `source/tutorials/`
2. Add the filename (without extension) to the `toctree` in the parent `index.md`

Example:
```markdown
# In source/tutorials/deep_learning/index.md

```{toctree}
:maxdepth: 2

exploring_cnns
your_new_tutorial    # Add this line
```
```

### Adding Jupyter Notebooks

1. Place `.ipynb` files in the tutorials directory
2. Add the filename to the `toctree`
3. Notebooks will be rendered automatically (not executed during build)

### Adding Images

1. Place images in `source/_static/images/`
2. Reference them in your Markdown:

```markdown
```{figure} ../../_static/images/your_image.png
:alt: Description
:align: center
:width: 80%

Caption text here.
```
```

## GitHub Pages Deployment

The documentation automatically deploys to GitHub Pages when you push to `main`.

### Setup (One-time)

1. Go to your repository Settings → Pages
2. Set Source to "GitHub Actions"
3. Push to `main` branch

Your docs will be available at: `https://YOUR_USERNAME.github.io/YOUR_REPO/`

## Configuration

Edit `source/conf.py` to customize:

- Project name and author
- GitHub repository URL
- Theme options
- Extensions

## Key Features

- **MyST Parser**: Write documentation in Markdown with extended syntax
- **PyData Theme**: Modern, responsive design
- **Math Support**: LaTeX equations with MathJax
- **Code Highlighting**: Syntax highlighting with copy button
- **Jupyter Support**: Render notebooks directly
- **Auto-deployment**: GitHub Actions workflow included

## Useful Commands

```bash
# Clean build directory
make clean

# Live reload during development (requires sphinx-autobuild)
pip install sphinx-autobuild
make livehtml
```

## Troubleshooting

### Build fails with import errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Images not showing
- Check the path in your Markdown file
- Ensure images are in `source/_static/images/`
- Use relative paths starting with `../../_static/`

### Math not rendering
- Ensure `dollarmath` is in `myst_enable_extensions` in `conf.py`
- Use `$...$` for inline math and `$$...$$` for display math
