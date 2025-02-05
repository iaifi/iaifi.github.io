---
layout: article
title: IAIFI Papers
aside:
  toc: true
---

View high energy physics IAIFI papers [on INSPIRE](https://inspirehep.net/institutions/1862936?ui-citation-summary=true)
{:.info}

[Foundational AI Papers](/papers-ai.html){:.button.button--outline-primary.button--pill.button--sm}    [Theoretical Physics Papers](/papers-theory.html){:.button.button--outline-primary.button--pill.button--sm}      [Experimental Physics Papers](/papers-experiment.html){:.button.button--outline-primary.button--pill.button--sm}    [Astrophysics Papers](/papers-astro.html){:.button.button--outline-primary.button--pill.button--sm}

{% assign products = site.data.products | sort | reverse %}
{% for product in products %}
{% assign paper = product %}
{% if paper.type == "paper" %}
***{{paper.title}}*** <br>
{{paper.authors}} <br>
{%if paper.doi %} [{{paper.journal}}]({{paper.doi}}) {% elsif paper.alt-url %} [{{paper.journal}}]({{paper.alt-url}}) {% endif %}[ {% if paper.arxiv %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}) {% endif %} {% if paper.code %} | [code]({{paper.code}}) {% endif %} ] {% if paper.doi %} `published` {% endif %} <br>
{% if paper.iaifi-thrust=="F" %}[Foundational AI](/papers-ai.html){:.button.button--outline-primary.button--pill.button--xs} {% endif %} {% if paper.iaifi-thrust=="T" %}[Theoretical Physics](/papers-theory.html){:.button.button--outline-primary.button--pill.button--xs} {% endif %} {% if paper.iaifi-thrust=="E" %}[Experimental Physics](/papers-experiment.html){:.button.button--outline-primary.button--pill.button--xs} {% endif %} {% if paper.iaifi-thrust=="A" %}[Astrophysics](/papers-astro.html){:.button.button--outline-primary.button--pill.button--xs} {% endif %}
<div style = "position:relative; top:-1em;" >
<details>
<summary>Abstract</summary>
<em>{{paper.abstract}}</em>
</details>
</div>
{% endif %}
{% endfor %}
