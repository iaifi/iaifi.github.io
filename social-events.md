---
layout: article
title: IAIFI Social Events
aside:
  toc: true
---

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign events = site.data.internal-events %}

## Upcoming Social Events

{% for event in events %}
  {% assign event-date = event.event-date | date: '%s' | plus: 0 %}
  {% unless event-date >= now %}{% continue %}{% endunless %}

  {% if event.type == "social" %}
  {% include internal-event_item.html event=event %}
  {% endif %}
{% endfor %}

## Past Social Events

{% for event in events %}
  {% assign event-date = event.event-date | date: '%s' | plus: 0 %}
  {% unless event-date < now %}{% continue %}{% endunless %}

  {% if event.type == "social" %}
  {% include internal-event_item.html event=event %}
  {% endif %}
{% endfor %}
