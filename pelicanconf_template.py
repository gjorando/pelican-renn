## GENERAL SETTINGS ##

AUTHOR = "<AUTHOR>"
SITENAME = "<SITE NAME>"
# SITESUBTITLE = "<SITE SUBTITLE>"
SITEURL = ""

# Jinja2 extensions
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.do", "jinja2.ext.i18n"]
}

# Docutils configuration
DOCUTILS_SETTINGS = {
    "initial_header_level": 3
}

# Plugins
PLUGINS = ["i18n_subsites", "full_gallery"]

# Extract some more metadata about the source file path, ie. the full path, directory, file name, and file name without the extension
PATH_METADATA = r"(?P<full_path>(?P<directory_path>.*)\/(?P<filename_full>(?P<filename_no_ext>.*)\..*))"

## URLs ##

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# /index.html is redefined as the lander page by the special page lander_enable.rst
# So the article list is set under posts/
INDEX_URL = "posts/"
INDEX_SAVE_AS = INDEX_URL + "index.html"

# Archives page is accessible under archives/
ARCHIVES_SAVE_AS = "archives/index.html"

# Authors page is accessible under authors/
AUTHORS_SAVE_AS = "authors/index.html"

# Categories page is accessible under categories/
CATEGORIES_SAVE_AS = "categories/index.html"

# Tags page is accessible under tags/
TAGS_SAVE_AS = "tags/index.html"

# Articles are accessible under post/{yyyy}/{mm}/{dd}/{slug}/
ARTICLE_URL = "post/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = ARTICLE_URL + "index.html"

# Pages are accessible under {path of the source file}/{slug}/
PAGE_URL = "{directory_path}/{slug}/"
PAGE_SAVE_AS = PAGE_URL + "index.html"

# Authors are accessible under author/{slug}/
AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = AUTHOR_URL + "index.html"

# Categories are accessible under category/{slug}/
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = CATEGORY_URL + "index.html"

# Categories are accessible under category/{slug}/
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = TAG_URL + "index.html"

## I18N/L10N SETTINGS ##

TIMEZONE = "America/Montreal"
# The theme is written in French
I18N_TEMPLATES_LANG = "fr"
DEFAULT_LANG = "en"
LOCALE = "en_CA"

## FEED GENERATION ##

# Disabled for development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## CONTENT ##

# Source files
PATH = "content"

# Source static files
# STATIC_PATHS = [
#     "css",
#     "images"
# ]

DEFAULT_ORPHANS = 10  # Minimum number of articles for the last page
DEFAULT_PAGINATION = 10  # Number of articles per page

# Access subsequent pages via <url>/page/<page number>/
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social links
SOCIAL = (
    ("Twitter", "#"),
)

## THEME ##

THEME = "theme"
# STYLESHEET_URL = "/css/custom.css"  # Theme overrides
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ("Foo", "https://perdu.com")
]
DISPLAY_SOCIALS_IN_FOOTER = True
LANDER_DISPLAY_SOCIALS_IN_FOOTER = False
NAV_ICON = "icon.png"
