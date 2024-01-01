
import datetime
import os
import sys

sys.path.insert(0, os.path.abspath('../'))

autodoc_mock_imports = ['glyphify']

from glyphify.classes.application import GlyphifyApplication

project = "Glyphify"
author = "Witch Software"
copyright = f"{datetime.date.today().year}, {author}"
release = GlyphifyApplication.APPLICATION_VERSION

templates_path = ['_templates']
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_title = f"{project} Documentation"
htmlhelp_basename = project
highlight_language = "python3"

html_theme_options = {
    "repository_url": "https://github.com/witch-software/glyphify",
    "use_repository_button": True
}

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

