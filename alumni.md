---
layout: article
title: Alumni
aside:
  toc: true
---


{% for category in site.data.alumni-category.categories  %}

## {{category.name}}

{% assign personnel = '' | split: '' %}

{% for block in category.blocks %}
{% assign personnel = personnel | concat: site.data[block].personnel %}
{% endfor %}

{% assign members = '' | split: '' %}
{% for tag in personnel  %}
{% assign member = site.data.people[tag] %}
{% assign members = members | push: member %}
{% endfor %}

{% if category.alphabetize %}
{% assign members = members | sort: "name" %}
{% endif %}

<div class="card-columns">
  <!--<div class="row">-->
  {% for person in members  %}

     <!-- test code for commas -->
     {% assign name = person.name %}
     {% if name contains "," %}
        {% assign name = name | split: "," | reverse | join: " " | strip %}
     {% endif %}
     
     <div class="card" style="width: 17rem; height: 23rem; justify-content: center;">
         <img class="my-card-img-top" src="{{person.photo}}" alt="{{name}}" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         {% if person.website %}
         <a href="{{person.website}}">{{name}}</a>
         {% else %}
         {{name}}
         {% endif %}
         </div>
         <div class="card-text" style="text-align: center; min-height: 3rem; line-height: 140%">
         <em> {{person.title}} </em> <br>
         </div>
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <small>
         <strong>{{person.institution}}</strong><br>
         </small>
         </div>

         {% if person.e-mail %}
         <div class="card-text" style="text-align: center">
         <small><small>
      <a href="mailto:{{person.e-mail}}">
        <em>{{person.e-mail}}</em>
      </a>
     </small></small>
     <br>
     </div>
         {% endif %}
         </div>
       </div>
  {% endfor %}
  <!--
  </div>
<br> -->
</div>

{% endfor %}
