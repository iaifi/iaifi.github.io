---
layout: article
title: Alumni
aside:
  toc: true
---


{% for category in site.data.alumni-category.categories  %}

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

<div class="card-columns">
  <!--<div class="row">-->
  {% for member in personnel  %}
     {% assign person = site.data.people[member] %}
     <div class="card" style="width: 17rem; height: 23rem; justify-content: center;">
         <img class="my-card-img-top" src="{{person.photo}}" alt="{{person.name}}" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         {% if person.website %}
         <a href="{{person.website}}">{{person.name}}</a>
         {% else %}
         {{person.name}}
         {% endif %}
         </div>
         <div class="card-text" style="text-align: center; min-height: 3rem; line-height: 140%">
         <em> {{person.title}} </em> <br>
         </div>
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <strong>{{person.institution}}</strong><br>
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
