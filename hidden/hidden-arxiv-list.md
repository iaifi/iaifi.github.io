---
layout: article
title: ArXiv Lists (Hidden Page)
aside:
  toc: true
---

{% assign products = site.data.products | sort | reverse %}

## ArXiv Links for Unpublished Papers

{% for product in products %}
{% assign paper = product %}
{% if paper.doi or paper.alt-url %}{% continue %}{% endif %}
{% unless paper.arxiv %}{% continue %}{% endunless %}
[https://arxiv.org/abs/{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}})
{% endfor %}

## ArXiv Links for Published Papers

{% for product in products %}
{% assign paper = product %}
{% unless paper.doi or paper.alt-url %}{% continue %}{% endunless %}
{% unless paper.arxiv %}{% continue %}{% endunless %}
[https://arxiv.org/abs/{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}})
{% endfor %}
