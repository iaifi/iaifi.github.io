---
layout: article
title: Hackathons and Workshops
aside:
  toc: true
---

{% assign now = 'now' | date: '%s' | plus: 0 %}

## Upcoming Hackathons and Workshops
{% assign talks = site.data.internal-events | sort: "start-date-time" %}

{% for talk in talks %}
 {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds > now %}{% continue %}{% endunless %}
  {% if talk.type == "internal-workshop" %}
      {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

## Past Hackathons and Workshops
{% assign talks = site.data.internal-events | sort: "start-date-time" | reverse %}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now %}{% continue %}{% endunless %}

  {% if talk.type == "internal-workshop" %}
  {% include internal-event_item.html talk=talk %}
  {% endif %}
{% endfor %}


