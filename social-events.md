---
layout: article
title: IAIFI Social Events
aside:
  toc: true
---

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign talks = site.data.internal-events %}

## Upcoming Social Events

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds >= now %}{% continue %}{% endunless %}

  {% if talk.type == "social" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

## Past Social Events

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now %}{% continue %}{% endunless %}

  {% if talk.type == "social" %}
  {% unless talk.event-name == "Weekly Coffee Hour" %}
  {% include internal-event_item.html talk=talk %}
  {% endunless %}
  {% endif %}
{% endfor %}
