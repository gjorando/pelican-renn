# pelican-renn

A simple Pelican theme tailored for my personal needs.

In order to use it, some Jinja extensions must be enabled in your `pelicanconf.py`:

```python
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.do"]
}
```

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

