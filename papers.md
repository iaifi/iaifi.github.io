---
layout: article
title: IAIFI Papers
---


{% for product in site.data.products  %}
{% assign paper = product[1] %}
{% if paper.type == "paper" %}
***{{paper.title}}*** <br>
{{paper.authors}} <br>
{%if paper.journal %} {{paper.journal}} {% endif %}[ {% if paper.arxiv %} [arxiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}) {% endif %} {% if paper.code %} | [code]({{paper.code}}) {% endif %} ]
<div style = "position:relative; top:-1em;" >
<details>
<summary>Abstract</summary>
<em>{{paper.abstract}}</em>
</details>
</div>
{% endif %}
{% endfor %}
