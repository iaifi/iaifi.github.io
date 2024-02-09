---
layout: article
title: Paper Tracking (Hidden Page)
aside:
  toc: true
---

{% for category in site.data.categories.categories  %}

## {{category.name}}

{% if category.type3 %}
{% assign personnel1 = site.data[category.type1].personnel %}
{% assign personnel2 = site.data[category.type2].personnel %}
{% assign personnel3 = site.data[category.type3].personnel %}
{% assign personnel = personnel1 | concat: personnel2 | concat: personnel3 %}
{% elsif category.type2 %}
{% assign personnel1 = site.data[category.type1].personnel %}
{% assign personnel2 = site.data[category.type2].personnel %}
{% assign personnel = personnel1 | concat: personnel2 %}
{% else %}
{% assign personnel = site.data[category.type1].personnel %}
{% endif %}

{% for member in personnel  %}
{% assign person = site.data.people[member] %}

### {{person.name}}

{% assign products = site.data.products | sort | reverse %}

<!-- First count the number of papers -->
{% assign paper_count = 0 %}
{% for product in products %}
{% assign paper = product %}
{% if paper.authors contains person.name %}
{% assign paper_count = paper_count | plus: 1 %}
{% endif %}
{% endfor %}


<!-- Then display the papers -->
{% for product in products %}
{% assign paper = product %}
{% if paper.authors contains person.name %}
 * [{{paper_count}}] **{{paper.title}}** <br>
{{paper.authors}} <br>
{%if paper.doi %} [{{paper.journal}}]({{paper.doi}}) {% elsif paper.alt-url %} [{{paper.journal}}]({{paper.alt-url}}) {% endif %}[ {% if paper.arxiv %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}) {% endif %} {% if paper.code %} | [code]({{paper.code}}) {% endif %} ]
{% assign paper_count = paper_count | plus: -1 %}
{% endif %}
{% endfor %}


{% endfor %}
{% endfor %}
