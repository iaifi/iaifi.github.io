---
layout: article
title: Industry Lunches
aside:
  toc: true
---

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign events = site.data.internal-events %}

## Upcoming Industry Lunches

{% for event in events %}
  {% assign event-date = event.event-date | date: '%s' | plus: 0 %}
  {% unless event-date >= now %}{% continue %}{% endunless %}

  {% if event.type == "industry-lunch" %}
  {% include internal-event_item.html event=event %}
  {% endif %}
{% endfor %}

## Past Industry Lunches

{% for event in events %}
  {% assign event-date = event.event-date | date: '%s' | plus: 0 %}
  {% unless event-date < now %}{% continue %}{% endunless %}

  {% if event.type == "industry-lunch" %}
  {% include internal-event_item.html event=event %}
  {% endif %}
{% endfor %}

