---
layout: article
title: Paper Tracking (Hidden Page)
aside:
  toc: true
---


## Table of Contents

{% assign all_categories = site.data.categories.categories | concat: site.data.alumni-category.categories %}

{% for category in all_categories %}
  <div><details>
  
    {% assign personnel = '' | split: '' %}

    {% for block in category.blocks %}
      {% assign personnel = personnel | concat: site.data[block].personnel %}
    {% endfor %}

    <!-- Assign members based on the personnel list -->
    {% assign members = '' | split: '' %}
    {% for tag in personnel %}
      {% assign member = site.data.people[tag] %}
      {% assign members = members | push: member %}
    {% endfor %}

    <summary><b>{{ category.name }}</b></summary>
    <ul>
      {%- for member in members -%}
        {% assign name = member.name %}
        {% if name contains "," %}
          {% assign name = name | split: "," | reverse | join: " " | strip %}
        {% endif %}
        <li><a href="#{{ name | replace: " ", "-" }}">{{ name }}</a></li>
      {%- endfor -%}
    </ul><br>

  </details></div>
{% endfor %}

{% assign categories = site.data.categories.categories | concat: site.data.alumni-category.categories %}



{% for category in categories  %}

## {{category.name}} {#{{category.name | replace: " ", "-"}}}

{% assign personnel = '' | split: '' %}

{% for block in category.blocks %}
{% assign personnel = personnel | concat: site.data[block].personnel %}
{% endfor %}

{% assign members = '' | split: '' %}
{% for tag in personnel  %}
{% assign member = site.data.people[tag] %}
{% assign members = members | push: member %}
{% endfor %}

{% for member in personnel  %}
{% assign person = site.data.people[member] %}

{% assign name = person.name %}
{% if name contains "," %}
{% assign name = name | split: "," | reverse | join: " " | strip %}
{% endif %}

#### {{name}} {#{{name | replace: " ", "-"}}}

{% assign products = site.data.products | sort | reverse %}

<!-- Initialize paper counters -->
{% assign paper_count = 0 %}
{% assign doi_count = 0 %}
{% assign alt_url_count = 0 %}
{% assign arxiv_count = 0 %}
{% assign code_count = 0 %}

<!-- make list of names to use -->
{% assign name1 = name | split: "," %}
{% assign name2 = person.professional-name | split: "," %}
{% assign name_list = person.professional_names | concat: name1 | concat: name2 %}

<!-- Count number of papers with various properties -->
{% for product in products %}
{% assign paper = product %}
{% assign is_this_author = false %}
{% for name in name_list %}
  {% if paper.authors contains name %}{% assign is_this_author = true %}{% endif %}
{% endfor %}
{% if is_this_author %}
  {% assign paper_count = paper_count | plus: 1 %}
  {% if paper.doi %}{% assign doi_count = doi_count | plus: 1 %}{% endif %}
  {% if paper.alt-url %}{% assign alt_url_count = alt_url_count | plus: 1 %}{% endif %}
  {% if paper.arxiv %}{% assign arxiv_count = arxiv_count | plus: 1 %}{% endif %}
  {% if paper.code %}{% assign code_count = code_count | plus: 1 %}{% endif %}
{% endif %}
{% endfor %}

<!-- Display table -->

| Name | Total Papers | With DOI | With Alt URL | On ArXiv | With Code |
| ---- | ------------ | -------- | ------------ | -------- | --------- |
| {{name}} | {{paper_count}} | {{doi_count}} | {{alt_url_count}} | {{arxiv_count}} | {{code_count}} |

A.k.a.:  {{name_list  | join: ", "}}

<!-- Display the papers -->
{% for product in products %}
{% assign paper = product %}
{% assign is_this_author = false %}
{% for name in name_list %}
  {% if paper.authors contains name %}{% assign is_this_author = true %}{% endif %}
{% endfor %}
{% if is_this_author %}
 * [{{paper_count}}] **{{paper.title}}** <br>
{{paper.authors}} <br>
{%if paper.doi %} [{{paper.journal}}]({{paper.doi}}) {% elsif paper.alt-url %} [{{paper.journal}}]({{paper.alt-url}}) {% endif %}[ {% if paper.arxiv %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}) {% endif %} {% if paper.code %} | [code]({{paper.code}}) {% endif %} ]
{% assign paper_count = paper_count | plus: -1 %}
{% endif %}
{% endfor %}

{% endfor %}
{% endfor %}
