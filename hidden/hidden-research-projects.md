---
layout: article
title: Research Projects (Hidden Page)
---

{% assign projects = site.data.projects | sort %}

## Projects

{% for project in projects %}

### {{project.title}}

Project Lead: {{project.project-lead}}
 
{% endfor %}
