---
layout: article
title: Internal Discussion Seminars
aside:
  toc: true
---

***The IAIFI Seminar series has been combined with the IAIFI Colloquium series beginning in Fall 2024.*** [View the Colloquium schedule](http://iaifi.org/events).
{:.info}

[Access recordings of past seminars](https://docs.google.com/document/d/1ZGLuC_-eqMwyeeJNbwR5YhEg_S18E8akbDE9m39oYsY/edit?usp=sharing)  (for IAIFI members only)

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign talks = site.data.seminars %}



## Upcoming Seminars 

{% for talk in talks %}
  {% assign talk-date = talk.talk-date | date: '%s' | plus: 0 %}
  {% unless talk-date > now %}{% continue %}{% endunless %}

  {% include seminar_item.html talk=talk %}

{% endfor %}

## Past Seminars 

{% for semester in site.data.calendar.semesters %}

### {{semester.name}}

{% for talk in talks %}
  {% assign talk-date = talk.talk-date | date: '%s' | plus: 0 %}
  {% unless talk-date < now and talk.semester == semester.tag %}{% continue %}{% endunless%}

  {% include seminar_item.html talk=talk is_previous=true %}

{% endfor %}

{% endfor %}
