---
layout: article
title: IAIFI Experimental Physics Papers
aside:
  toc: true
---

## Experimental Physics

{% assign products = site.data.products | sort | reverse %}
{% for product in products %}
{% assign paper = product %}
{% if paper.type == "paper" %}
{% if paper.iaifi-thrust == "E" %}
***{{paper.title}}*** <br>
{{paper.authors}} <br>
{%if paper.doi %} [{{paper.journal}}]({{paper.doi}}) {% elsif paper.alt-url %} [{{paper.journal}}]({{paper.alt-url}}) {% endif %}[ {% if paper.arxiv %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}) {% endif %} {% if paper.code %} | [code]({{paper.code}}) {% endif %} ] {% if paper.doi %} `published` {% endif %}
<div style = "position:relative; top:-1em;" >
<details>
<summary>Abstract</summary>
<em>{{paper.abstract}}</em>
</details>
</div>
{% endif %}
{% endif %}
{% endfor %}

