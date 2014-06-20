django-colors
=============

fork of https://code.google.com/p/django-colors/

Usage
=============

**Templating example**

```
<h1><b style="background-color:#{{ color }};"></b>#{{ color }}</h1>
<h2>Lightness</h2>
<ul class="color-test">
    {% for l in lightness_range %}
    <li style="background-color:#{{ color|lightness:l }};"><b>{{ l }}%</b></li>
    {% endfor %}
</ul>
<h2>Saturation</h2>
<ul class="color-test">
    {% for s in saturation_range %}
    <li style="background-color:#{{ color|saturation:s }};"><b>{{ s }}%</b></li>
    {% endfor %}
</ul>
<h2>Hue</h2>
<ul class="color-test">
    {% for h in hue_range %}
    <li style="background-color:#{{ color|hue:h }};"><b>{{ h }}&deg;</b></li>
    {% endfor %}
</ul>
```

###Template tags

###Color manipulation:

Tags       | Description
---------- | -----------------------
color	     | Returns the hexadecimal value of a named color (ex: black -> 000000)
lightness	 | Set lightness to x, accept hexadecimal or hsv tuple as value
hue	       | Set hue to x, accept hexadecimal or hsv tuple as value
opposite	 | Returns the opposite (complementary) color on the HSV color space
saturation | Set saturation to x, accept hexadecimal or hsv tuple as value

###Color spaces conversions & utils:

Tags       | Description
-----------|-----------------------
hex_to_rgb | Returns the opposite color on the HSV color space
hex_to_hsv | Returns the HSV value of a hexadecimal color
hsv_to_hex | Returns the hexadecimal value of a HSV color
expand_hex | Expands shorthand hexadecimal code, ex: c30 -> cc3300
short_hex  | Return shorthand hexadecimal code, ex: cc3300 -> c30

Real world examples:
====================

**Saturation example**
> In this example we take an hexadecimal string and set its saturation to 10.

```
{% load colors %}

h1 {
    background: #{{ hexcode|saturation:"10" }}
}
```

**Chaining example**
> We can chain transformation, in the next example we set the saturation to 50 and set the lightness to 40 on the result.

```
{% load colors %}

h1 {
    background: #{{ hexcode|saturation:"50"|lightness:"40" }};
}
```

**Using RGB values in CSS:**

```
{% load colors %}

h1 {
    background: {{ hexcode|hex_to_rgb:"rgb(%s, %s, %s)" }};
}
```

**Dynamically generated gradients**

```
{% load colors %}

#my_div {
    /* non-css3 */
    background: #{{ color }};
    /* IE */
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#{{ color }}', endColorstr='#{{ color|lightness:"30" }}'); 
    /* webkit */
    background: -webkit-gradient(radial, left top, left bottom, from(#{{ color }}), to(#{{ color|lightness:"30" }}));
    /* firefox 3.6+ */
    background: -moz-linear-gradient(top,  #{{ color }},  #{{ color|lightness:"30" }});
}
```

**Color field:**

```
from colors.fields import ColorField

class MyModel(ExtendedModel):
    title = models.CharField('Title', max_length=250)
    color = ColorField(default='ffffff')
```    

