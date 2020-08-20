---
layout: article
title: People
---


The IAIFI is comprised of both physics and AI researchers at MIT, Harvard, Northeastern, and Tufts.

## Senior Investigators

<div class="card-columns">
  <!--<div class="row">-->
  {% for member in site.data.senior-investigators.personnel  %}
     {% assign person = site.data.people[member] %}
       <div class="card" style="width: 13rem; height: 29rem; justify-content: center;">
         <img class="card-img-top" src="{{person.photo}}" alt="{{person.name}}" height="210rem">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 6rem;">
         <a href="{{person.website}}">{{person.name}}</a><br>
         <em> {{person.title}} </em> <br>
         </div>
         <div class="card-text" style="text-align: center; min-height: 5rem; line-height: 120%">
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

Coming soon: IAIFI Fellows and PhD Students.
{:.info}
