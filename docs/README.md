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
