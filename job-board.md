---
layout: article
title: Physics/AI Jobs
aside:
  toc: true
---

As a hub for the intersection of Physics and AI in the Boston area and beyond, we are happy to share job opportunities at this intersection as we become aware of them. 

To include a job post on this page, email [iaifi@mit.edu](mailto:iaifi@mit.edu), including the job title, job description, and application deadline. 
{:.info}

# IAIFI Jobs

## Faculty Opportunities

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign jobs = site.data.jobs | sort | reverse %}
{% for job in jobs %}
  {% capture date %}{{job.expire | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
{% assign iaifi-faculty = job %}
{% if job.type == "iaifi-faculty" %}
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

## Postdoc Opportunities
Postdoctoral researchers at any of the partner institutions may collaborate with IAIFI researchers to become a Junior Investigator.

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign jobs = site.data.jobs | sort | reverse %}
{% for job in jobs %}
  {% capture date %}{{job.expire | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
{% assign iaifi-postdoc = job %}
{% if job.type == "iaifi-postdoc" %}
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

## Graduate Student Opportunities
IAIFI does not have a dedicated PhD program, but PhD students at any of the partner institutions may collaborate with IAIFI researchers to become a Junior Investigator.

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign jobs = site.data.jobs | sort | reverse %}
{% for job in jobs %}
  {% capture date %}{{job.expire | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
{% assign iaifi-grad = job %}
{% if job.type == "iaifi-grad" %}
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

# Academic Opportunities

## Faculty Opportunities
{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign jobs = site.data.jobs | sort | reverse %}
{% for job in jobs %}
  {% capture date %}{{job.expire | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
{% assign faculty = job %}
{% if job.type == "faculty" %}
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

## Postdoc Opportunities
{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign jobs = site.data.jobs | sort | reverse %}
{% for job in jobs %}
  {% capture date %}{{job.expire | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
{% assign postdoc = job %}
{% if job.type == "postdoc" %}
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

<!---
## Other Academic Opportunities
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
--->

# Industry Opportunities

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
