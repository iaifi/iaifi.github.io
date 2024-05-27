---
layout: article
title: Research Projects
aside:
  toc: true
---

<!-- Check that all projects have a valid subthrust -->

{% assign subthrust_list = '' %}
{% for thrust in site.data.research.thrusts %}
{% for subthrust in thrust.subthrusts %}
{% assign subthrust_list = subthrust_list | append: ',' | append: subthrust.key %}
{% endfor %}
{% endfor %}


{% assign subthrust_list = subthrust_list | remove_first: ',' | split: ',' %}

{% for project in site.data.research-projects %}
{% unless subthrust_list contains project.subthrust %}
**{{project.title}}** has unknown subthrust: **{{project.subthrust}}**
{% endunless %}
{% endfor %}

<!-- Now print out everything -->

{% for thrust in site.data.research.thrusts %}

## {{thrust.name}}

{% for subthrust in thrust.subthrusts %}

### {{subthrust.name}}

{% for project in site.data.research-projects %}
{% if project.subthrust == subthrust.key %}
  * **{{project.title}}**
{% endif %}
{% endfor %}

{% endfor %}
{% endfor %}
