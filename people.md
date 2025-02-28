---
layout: article
title: People
aside:
  toc: true
---


The IAIFI is comprised of both physics and AI researchers at MIT, Harvard, Northeastern, and Tufts.

<!---
{% for category in site.data.categories.categories  %}

  * [{{category.name}}](#{{category.anchor}})

{% endfor %}
--->

We are currently accepting applications from senior researchers in both academia and industry to become IAIFI Affiliates.  If this interests you, see our [IAIFI Affiliates Application Form](https://app.smartsheet.com/b/form/b73212d8895c4436a947b2dfdd999da3).

If you are a junior researcher interested in becoming involved in IAIFI, see our [Junior Researcher Interest Page](https://iaifi.org/junior-researchers.html).

There are various levels of involvement in IAIFI: 

**Senior Investigators, Junior Investigators, IAIFI Affiliates**:  Members in these categories are actively working on IAIFI-related research and must report their IAIFI-related activities to the NSF. Everyone at these levels is listed on this page.
{:.info}

**Friend of IAIFI**:  Friends of IAIFI are Boston-area researchers interested in IAIFI's mission, but cannot receive NSF funding and have no reporting requirements. Friends of IAIFI are welcome to participate in internal IAIFI activities. If you are interested in becoming a Friend of IAIFI, [complete the interest form](https://app.smartsheet.com/b/form/3cff913c564141249c4292ad8c435774).
{:.info}

{% for category in site.data.categories.categories  %}

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
     
     <div class="card" style="width: 17rem; height: 27rem; justify-content: center;">
         <img class="my-card-img-top" src="{{person.photo}}" alt="{{name}}" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         {% if person.website %}
         <a href="{{person.website}}">{{name}}</a>
         {% else %}
         {{name}}
         {% endif %}
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
