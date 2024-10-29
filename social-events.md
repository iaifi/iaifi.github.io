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
  {% assign talk-date = talk.talk-date | date: '%s' | plus: 0 %}
  {% unless talk-date >= now %}{% continue %}{% endunless %}

  {% if talk.type == "social" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

## Past Social Events

{% for talk in talks %}
  {% assign talk-date = talk.talk-date | date: '%s' | plus: 0 %}
  {% unless talk-date < now %}{% continue %}{% endunless %}

  {% if talk.type == "social" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}
