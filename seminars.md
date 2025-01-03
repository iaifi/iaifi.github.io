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


## Past Seminars 
{% assign talks = site.data.seminars | sort: "start-date-time" | reverse %}

{% for semester in site.data.calendar.semesters %}
  {% assign has_events = false %}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now and talk.semester == semester.tag %}{% continue %}{% endunless%}
    {% assign has_events = true %}
{% endfor %}

{% if has_events %}
### {{semester.name}}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now and talk.semester == semester.tag %}{% continue %}{% endunless%}
  {% include seminar_item.html talk=talk is_previous=true %}
 {% endfor %}
 {% endif %}
{% endfor %}
