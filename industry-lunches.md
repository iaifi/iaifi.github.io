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
  {% assign talk-date = talk.talk-date | date: '%s' | plus: 0 %}
  {% unless talk-date >= now %}{% continue %}{% endunless %}

  {% if talk.type == "industry-lunch" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

## Past Industry Lunches

{% for talk in talks %}
  {% assign talk-date = talk.talk-date | date: '%s' | plus: 0 %}
  {% unless talk-date < now %}{% continue %}{% endunless %}

  {% if talk.type == "industry-lunch" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

