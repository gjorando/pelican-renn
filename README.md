# pelican-renn

A simple Pelican theme tailored for my personal needs.

The easiest way to get started is to copy the content of [the example Pelican configuration file](pelicanconf_template.py).

To generate the lander page, you must add a page with the following content:

```rest
<Lander page title>
###################

:status: hidden
:slug: lander-page
:lang: en
:save_as: index.html
:template: lander
```

This special page is populated with sections; each of these sections is actually a page with a special slug. It is strongly advised to hide these special pages.

```rest
<Section name>
##############

:status: hidden
:nav: <section nav name>
:slug: landing-section-hidden-<section-name>

<Section content
```

If the `nav` metadata is set, an anchor to the section is added to the lander page navbar.

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
- `LANDER_MENUITEMS` - `MENUITEMS`, but for the lander page (Default: unset).
- `NAV_ICON` - Icon for the navbar (Default: unset).
