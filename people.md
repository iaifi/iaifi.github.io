---
layout: article
title: People
---


The IAIFI is comprised of both physics and AI researchers at MIT, Harvard, Northeastern, and Tufts.


{% for category in site.data.categories.categories  %}

## {{site.data[category].name}}

<div class="card-columns">
  <!--<div class="row">-->
  {% for member in site.data[category].personnel  %}
     {% assign person = site.data.people[member] %}
     <div class="card" style="width: 17rem; height: 27rem; justify-content: center;">
         <img class="card-img-top" src="{{person.photo}}" alt="{{person.name}}" height="210rem">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="{{person.website}}">{{person.name}}</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> {{person.title}} </em> <br>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 100%">
         <small>
   <small>
         <em> {{person.interests}} </em> <br>
         </small>
         </small>
         </div>

         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <small>
         <em>{{person.institution}}</em><br>
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