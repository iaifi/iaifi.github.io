---
layout: article
title: Industry Lunches
aside:
  toc: true
---

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign talks = site.data.internal-events %}

## Upcoming Industry Lunches

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds >= now %}{% continue %}{% endunless %}

  {% if talk.type == "industry-lunch" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

## Past Industry Lunches

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now %}{% continue %}{% endunless %}

  {% if talk.type == "industry-lunch" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

