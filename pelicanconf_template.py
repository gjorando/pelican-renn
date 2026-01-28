## GENERAL SETTINGS ##

AUTHOR = "<AUTHOR>"
SITENAME = "<SITE NAME>"
# SITESUBTITLE = "<SITE SUBTITLE>"
SITEURL = ""

# Jinja2 extensions
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.do", "jinja2.ext.i18n"]
}

# Plugins
PLUGIN_PATHS = ["plugin/pelican/plugins/"]
PLUGINS = ["pelican_renn_plugin", "i18n_subsites"]

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
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = "archives/index.html"

# Authors page is accessible under authors/
AUTHORS_URL = "authors/"
AUTHORS_SAVE_AS = "authors/index.html"

# Categories page is accessible under categories/
CATEGORIES_URL = "categories/"
CATEGORIES_SAVE_AS = "categories/index.html"

# Tags page is accessible under tags/
TAGS_URL = "tags/"
TAGS_SAVE_AS = "tags/index.html"

# Articles are accessible under post/{yyyy}/{mm}/{dd}/{slug}/
ARTICLE_URL = ARTICLE_LANG_URL = "post/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = ARTICLE_LANG_SAVE_AS = ARTICLE_URL + "index.html"

# Pages are accessible under {path of the source file}/{slug}/
PAGE_URL = PAGE_LANG_URL = "{directory_path}/{slug}/"
PAGE_SAVE_AS = PAGE_LANG_SAVE_AS = PAGE_URL + "index.html"

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
I18N_UNTRANSLATED_ARTICLES = "hide"

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

# We put our articles in a subdirectory, for a clearer separation
ARTICLES_PATHS = [
    "articles"
]

# Source static files
STATIC_PATHS = [
    "css",
    "images",
]

DEFAULT_ORPHANS = 10  # Minimum number of articles for the last page
DEFAULT_PAGINATION = 10  # Number of articles per page

# Access subsequent pages via <url>/page/<page number>/
PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{save_as}"),
    (2, "{base_name}/{number}/", "{base_name}/{number}/index.html"),
)

# Social links
SOCIAL = (
    ("Mastodon", "#"),
)

## HIDDEN CATEGORIES ##

HIDDENCATEGORY_ENABLE = True

# Hidden categories are accessible under {base_name}/full/
HIDDENCATEGORY_URL = "{base_category.url}full/"

# Per-category settings
HIDDENCATEGORY_OVERRIDES = {
    "gallery": {
        "PER_CATEGORY_CONTEXT": {
            "gallery": {
                "page_desc": "A description for the hidden category.",
            }
        },
        "HIDDENCATEGORY_NAME": "{base_category.name} (full)"
    }
}

## NOINDEX CATEGORIES ##

# Categories whose articles are not in the index page
NOINDEX_CATEGORIES = ["gallery"]

## THEME ##

THEME = "theme"
# STYLESHEET_URL = "/css/custom.css"  # Theme overrides
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SOCIALS_IN_FOOTER = True
MENUITEMS = [
    ("Gallery", "/" + CATEGORY_URL.format(slug="gallery"))
]
NAV_ICON = "images/icon.png"

# Variables for category specific templates
PER_CATEGORY_CONTEXT = {
    "gallery": {
        "page_desc": "A description for the category.",
    },
}

# Overrides for the lander template
LANDER_OVERRIDES = {
    "MENUITEMS": [
        ("Blog", "/" + INDEX_URL),
        ("Gallery", "/" + CATEGORY_URL.format(slug="gallery")),
    ],
    "DISPLAY_SOCIALS_IN_FOOTER": False,
    "NAV_ICON": None
}

## TAILWIND CSS ##

TAILWINDCSS_ENABLE = True
TAILWINDCSS_VERSION = "v4.1.18"
TAILWINDCSS_MINIFY = False
TAILWINDCSS_INPUT_FILES = [f"{THEME}/static/css/style.css"]

## THUMBNAILS ##

THUMBNAIL_ENABLE = True
THUMBNAIL_PATHS = [
    "images/gallery/"
]
gallery_thumbnail_width = 384
THUMBNAIL_RESIZES = {
    # Gallery icon
    "gallery": (gallery_thumbnail_width, round(gallery_thumbnail_width/(16/9)), True),
    # Small size thumbnail
    "thumbnail": (768, None, True),
}

## OVERRIDES ##

# Main site (english) overrides
OVERRIDES = {
    ("lander-page", "Page"): {
        "MENUITEMS": [
            # ("Blog", "/" + INDEX_URL),
            ("Gallery", "/" + CATEGORY_URL.format(slug="gallery")),
        ],
        "DISPLAY_SOCIALS_IN_FOOTER": False,
        "NAV_ICON": None
    },
    ("gallery", "Category"): {
        "CATEGORY_DESCRIPTION": "I've commissioned a lot of artists over the years. This gallery compiles all (all?) artworks of Renn.",
    },
    ("gallery", "HiddenCategory"): {
        "CATEGORY_DESCRIPTION": "Oooooh, so there was more than meets the eye here.",
    }
}

I18N_SUBSITES = {
    # French overrides
    "fr": {
        "THUMBNAIL_ENABLE": False,
        "LOCALE": "fr_CA",
        "MENUITEMS": [
            ("Galerie", "/fr/" + CATEGORY_URL.format(slug="gallery")),
        ],
        "OVERRIDES": {
            ("lander-page", "Page"): {
                "MENUITEMS": [
                    ("Blog", "/fr/" + INDEX_URL),
                    ("Galerie", "/fr/" + CATEGORY_URL.format(slug="gallery")),
                ],
                "DISPLAY_SOCIALS_IN_FOOTER": False,
                "NAV_ICON": None
            },
            ("gallery", "Category"): {
                "CATEGORY_DESCRIPTION": "Une description en français!",
                "CATEGORY_NAME": "Galerie",
            },
            ("gallery", "HiddenCategory"): {
                "CATEGORY_DESCRIPTION": "La galerie cachée en français!",
                "CATEGORY_NAME": "Galerie cachée",
            }
        }
    }
}