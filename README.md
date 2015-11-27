# django-pipstatus

django-pipstatus provides simple templatetag and page that shows the status of your pip installation.

## Installation

Add 'pipstatus' to your INSTALLED_APP.

## Setup dedicated URL

add pipstatus.url to your urls.py

```python
  urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pipstatus/', include(pipstatus.urls)),
]
```

## Setup own view

Define a view and a template somewhere

```python
def pipconfig2(request):
    return render(request, "my_template.html")
```
```html
{% extends "base.html" %}
{% block content %}
<h1>My PIP Page</h1>
{% include "pipstatus.html" %}
{% endblock %}
```

## Define your own template structure

```html
{% load pipstatus %}
{% get_pipstatus as config %}
{% for x in config.entries %}
  {% if x.outdated %}
    x.name is outdated!<br>
  {% endif %}
{% endfor %}
```

