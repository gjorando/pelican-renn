# pelican-renn

A simple Pelican theme tailored for my personal needs.

In order to use it, some Jinja extensions must be enabled in your `pelicanconf.py`:

```python
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.do", "jinja2.ext.i18n"]
}

# The theme templates are written in French
I18N_TEMPLATES_LANG = "fr"
```

Moreover, `pelican-i18n-subsites` plugin is required.

## Customization

The CSS can be customized by setting the `STYLESHEET_URL` config variable to your custom CSS file. For instance, the colors can be adjusted with the following directives:

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

Available configuration variables are listed below.

- `STYLESHEET_URL` - Custom CSS, loaded after the base stylesheets (Default: unset).
- `DISPLAY_SOCIALS_IN_FOOTER` - Whether to display the social icons (set with `SOCIAL`) in the footer (Default: `False`).
