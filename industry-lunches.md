---
layout: article
title: Industry Lunches
aside:
  toc: true
---

{% assign now = 'now' | date: '%s' | plus: 0 %}

## Upcoming Industry Lunches
{% assign talks = site.data.internal-events | sort: "start-date-time" %}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds >= now %}{% continue %}{% endunless %}

  {% if talk.type == "industry-lunch" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

## Past Industry Lunches
{% assign talks = site.data.internal-events | sort: "start-date-time" | reverse %}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now %}{% continue %}{% endunless %}

  {% if talk.type == "industry-lunch" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

