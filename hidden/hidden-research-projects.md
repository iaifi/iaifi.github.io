---
layout: article
title: Research Projects (Hidden Page)
aside:
  toc: true
---

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

{% assign projects = site.data.research-projects | sort | reverse %}

{% for project in projects %}
{% assign is_this_person = false %}
{% for name in name_list %}
  {% if project.project-lead contains name or project.iaifi-members contains name %}{% assign is_this_person = true %}{% endif %}
{% endfor %}
{% if is_this_person %}
**{{project.project-title}}**
{% endif %}  
{% endfor %}

{% endfor %}
{% endfor %}


{% assign projects = site.data.research-projects %}

{% for project in projects %}

**{{project.project-title}}**
 
{% endfor %}
