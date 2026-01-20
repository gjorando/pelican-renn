# pelican-renn

A simple Pelican theme tailored for my personal needs.

The easiest way to get started is to copy the content of [the example Pelican configuration file](pelicanconf_template.py).

To generate the lander page, you must add a page with the following content:

```rest
<Lander page title>
###################

:status: hidden
:save_as: index.html
:template: lander
:nav: a link <sci-hub.ru>
```

The `nav` metadata is optional, and can be populated with a list of `text <uri>` or `uri` links that will be added to the navbar. `save_as` can be set as you want, but if you mean the lander page to be your root index page, you must at least redefine `INDEX_SAVE_AS`.

Moreover, `pelican-i18n-subsites` plugin is required.

## Customization

The CSS can be customized by setting the `STYLESHEET_URL` config variable to your custom CSS file. For instance, the  colors can be adjusted with the following directives:

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

Additional configuration variables are listed below.

- `DISPLAY_SOCIALS_IN_FOOTER` - Whether to display the social icons (set with `SOCIAL`) in the footer (Default: `False`).
- `LANDER_DISPLAY_SOCIALS_IN_FOOTER` - Whether to display the social icons (set with `SOCIAL`) in the lander footer (Default: `False`).
- `NAV_ICON` - Icon for the navbar (Default: unset).
