---
layout: article
title: Research Projects
aside:
  toc: true
---

<!-- Check that all projects have a valid subthrust -->

{% assign subthrust_list = '' %}
{% for thrust in site.data.research.thrusts %}
{% for subthrust in thrust.subthrusts %}
{% assign subthrust_list = subthrust_list | append: ',' | append: subthrust.key %}
{% endfor %}
{% endfor %}


{% assign subthrust_list = subthrust_list | remove_first: ',' | split: ',' %}

{% for project in site.data.research-projects %}
{% unless subthrust_list contains project.subthrust %}
**{{project.title}}** has unknown subthrust: **{{project.subthrust}}**
{% endunless %}
{% endfor %}

<!-- Trying to make graphically representation of projects -->
<!--
```chart
{
  "type": "bubble",
  "data": {
    "datasets": [{
      "label": "My dataset",
      "data": [
        {"x": 0, "y": 7},
        {"x": 1, "y": 3}
      ],
      "backgroundColor": [
        "#FF6384",
        "#4BC0C0",
        "#FFCE56",
        "#E7E9ED",
        "#36A2EB"
      ]
    }]
  },
  "options": {
    "aspectRatio": 1,
    "plugins": {
      "title": {
        "display": "true",
        "text": "Custom Chart Title"
      }
    },
    "scales": {
      "x": {
        "beginAtZero": "true",
        "min": 0,
        "max": 10
      },
      "yAxis": {
        "title": { "display": "true", "text": "Number of Articles"},
        "type": "logarithmic",
        "position": "right",
        "beginAtZero": "true",
        "min": 0,
        "max": 10
      }
    },
    "elements": {
      "point": {
        "radius": 10
      }
    }
  }
}
```
-->

<!-- Now print out everything -->

{% for thrust in site.data.research.thrusts %}

## {{thrust.name}}

{% for subthrust in thrust.subthrusts %}

### {{subthrust.name}}

<div class="card-columns">
{% for project in site.data.research-projects %}
{% if project.subthrust == subthrust.key %}
     <div class="card" style="width: 17rem; height: 25rem; justify-content: center;">
         <img class="my-card-img-top" src="{{project.project-figure}}" alt="{{project.figure-caption}}" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="{{project.project-code}}">{{project.title}}</a> <br>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em>{{project.project-lead}}, {{other-iaifi-leads}}, {{other-iaifi-members}}</em> <br>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 100%">
         <small>
   <small>
         {{project.project-tags}} <br>
         </small>
         </small>
         </div>
         </div>
         </div>
{% endif %}
{% endfor %}
</div>
{% endfor %}
{% endfor %}
