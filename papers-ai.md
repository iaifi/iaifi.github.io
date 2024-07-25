---
layout: article
title: IAIFI Foundational AI Papers
aside:
  toc: true
---

## Foundational AI

{% assign products = site.data.products | sort | reverse %}
{% for product in products %}
{% assign paper = product %}
{% if paper.type == "paper" %}
{% if paper.iaifi-thrust == "F" %}
***{{paper.title}}*** <br>
{{paper.authors}} <br>
{%if paper.doi %} [{{paper.journal}}]({{paper.doi}}) {% elsif paper.alt-url %} [{{paper.journal}}]({{paper.alt-url}}) {% endif %}[ {% if paper.arxiv %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}) {% endif %} {% if paper.code %} | [code]({{paper.code}}) {% endif %} ]
<div style = "position:relative; top:-1em;" >
<details>
<summary>Abstract</summary>
<em>{{paper.abstract}}</em>
</details>
</div>
{% endif %}
{% endif %}
{% endfor %}
