---
layout: article
title: Physics/AI Jobs
aside:
  toc: true
---

As a hub for the intersection of Physics and AI in the Boston area and beyond, we are happy to share job opportunities at this intersection as we become aware of them. 

To include a job post on this page, email [iaifi@mit.edu](mailto:iaifi@mit.edu), including the job title, job description, and application deadline. 
{:.info}

Note: These are jobs external to IAIFI. For IAIFI-related job opportunities, see our [IAIFI Jobs page](\iaifi-jobs.html).


## Academic Opportunities
{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign jobs = site.data.jobs | sort | reverse %}
{% for job in jobs %}
  {% capture date %}{{job.expire | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
{% assign academic = job %}
{% if job.type == "academic" %}
**{{job.title}}** <br>
*{{job.employer}}* <br>
{%if job.deadline %} Deadline: {{job.deadline}} | {% endif %} [Apply]({{job.link}}) <br>
<div style = "position:relative; top:-1em;" >
<details>
<summary>Details</summary>
<em>{{job.details}}</em>
</details>
</div>
{% endif %}
{% endif %}
{% endfor %}

## Industry Opportunities

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign jobs = site.data.jobs | sort | reverse %}
{% for job in jobs %}
  {% capture date %}{{job.expire | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
{% assign industry = job %}
{% if job.type == "industry" %}
**{{job.title}}** <br>
*{{job.employer}}* <br>
{%if job.deadline %} Deadline: {{job.deadline}} | {% endif %} [Apply]({{job.link}})
<div style = "position:relative; top:-1em;" >
<details>
<summary>Details</summary>
<em>{{job.details}}</em>
</details>
</div>
{% endif %}
{% endif %}
{% endfor %}
