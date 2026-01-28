# pelican-renn

A Pelican theme tailored for my personal needs. It is designed to be tightly integrated to a custom plugin I made, [`pelican-renn-plugin`](https://github.com/gjorando/pelican-renn-plugin).

## Installation

Using git submodules:

```bash
# In the project root
git submodule add git@github.com:gjorando/pelican-renn.git theme
```

The easiest way to get started is then to copy the content of [the example Pelican configuration file](pelicanconf_template.py). This configuration file assumes that `pelican-renn-plugin` is configured as well.

## Features

### Additional article metadata

#### `subtitle`

Adds a subtitle below the article title.

### Lander page

To generate the lander page, you must add a page with the following content:

```rest
<Lander page title>
###################

:status: hidden
:save_as: index.html
:template: lander
:nav: a link <sci-hub.ru>, another-link.com

<content>
```

The `nav` metadata is optional, and can be populated with a list of `text <uri>` or `uri` links that will be added to the navbar. `save_as` can be set as you want, but if you mean the lander page to be your root index page, you must at least redefine `INDEX_SAVE_AS`. This is already configured in the example configuration file.

### Per-category templates for article and category pages

The [category](templates/category.html) and [article](templates/article.html) templates allow for category specific templates. They are to be defined in `templates/category/{category_slug}.html` and `templates/article/{category_slug}.html` respectively, the default fallback being named `_.html`. Hidden categories from [`pelican-renn-plugin`](https://github.com/gjorando/pelican-renn-plugin) are supported: A hidden category gets the same custom template as its base category.

### An example of customized category: Gallery

The theme comes with a pre-made custom category, an image gallery. Each article in this category is an image with a description, and the category page displays them as a grid. The image is set via the `img` metadata, and the `source` metadata can optionally be set as a url to a source reference for the image.

### Compatibility with `pelican-renn-plugin` overrides feature

These configuration variables do not make much sense without the overrides feature of [`pelican-renn-plugin`](https://github.com/gjorando/pelican-renn-plugin). This allows you to define per-category values, and they are reflected in the rendered templates. Putting them in the global settings namespace will overrides the value for all categories that do not redefine it in `OVERRIDES`. See [the example Pelican configuration file](pelicanconf_template.py) for more details.

#### `CATEGORY_NAME`

Replace the name of the category with this value.

#### `CATEGORY_TITLE`

Replace the default content title of the category page with this value.

#### `CATEGORY_DESCRIPTION`

Add a category description below the content title page.

### Additional configuration variables

#### `INDEX_URL`, `ARCHIVES_URL`, `AUTHORS_URL`, `CATEGORIES_URL`, `TAGS_URL`

URLs for direct template pages are not hardcoded, and can be customized following the same `*_URL` setting as the other URL settings.

#### `STYLESHEET_URL`

Additional stylesheet to load. For instance, the colors can be adjusted with the following directives:

```css
/* Colors are to be modified according to your needs */
:root {
    --bg-color: #161413;
    --fg-color: #FBF9FF;
    --link-color: #B8A1CE;
    --title-color: #F58F29;
    --footer-color: #2B2A30;
}
```

Check [the base stylesheet](static/css/style.css) for more details.

#### `SITE_SUBTITLE`

Optional subtitle displayed under the site title in the header.

### `DISPLAY_PAGES_ON_MENU`

Whether to list all published pages in the navbar

### `DISPLAY_CATEGORIES_ON_MENU`

Whether to display all categories in the menu.

### `MENUITEMS`

List of `(text, url)` links to add to the navbar.

#### `SOCIAL`, `DISPLAY_SOCIALS_IN_FOOTER`

`SOCIAL` defines a list of `(text, url)` social links, that are displayed in the footer as small icons if `DISPLAY_SOCIALS_IN_FOOTER` is set to `True`. See the list of available social media icons [here](static/images/).

#### `NAV_ICON`

Optional clickable icon for the navbar that links back to the website root.

