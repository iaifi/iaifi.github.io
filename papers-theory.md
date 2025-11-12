---
layout: article
title: IAIFI Theoretical Physics Papers
aside:
  toc: true
---

View high energy physics IAIFI papers [on INSPIRE](https://inspirehep.net/institutions/1862936?ui-citation-summary=true)
{:.info}

## Theoretical Physics

{% assign products = site.data.products | sort | reverse %}
{% for product in products %}
{% assign paper = product %}
{% if paper.type == "paper" %}
{% if paper.iaifi-thrust == "T" %}
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

