---
layout: article
title: IAIFI Social Events
aside:
  toc: true
---

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign next_week = now | plus: 604800 %}

## Upcoming Social Events
{% assign talks = site.data.internal-events | sort: "start-date-time" %}

{% for talk in talks %}
 {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% if talk.type == "social" %}
    {% if talk.event-name != "Weekly Coffee Hour" and start_date_time_in_seconds >= now %}
      {% include internal-event_item.html talk=talk %}
    {% elsif talk.event-name == "Weekly Coffee Hour" and start_date_time_in_seconds >= now and start_date_time_in_seconds <= next_week %}
      {% include internal-event_item.html talk=talk %}
    {% endif %}
  {% endif %}
{% endfor %}

## Past Social Events
{% assign talks = site.data.internal-events | sort: "start-date-time" | reverse %}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now %}{% continue %}{% endunless %}

  {% if talk.type == "social" %}
  {% unless talk.event-name == "Weekly Coffee Hour" %}
  {% include internal-event_item.html talk=talk %}
  {% endunless %}
  {% endif %}
{% endfor %}
