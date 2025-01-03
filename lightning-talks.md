---
layout: article
title: Thematic Discussion Sessions
aside:
  toc: true
---

Unless otherwise noted, lightning talks will be held in person (MIT Kolker Room, Building 26, Room 414) and over [Zoom](https://mit.zoom.us/j/92183041364?pwd%3DN3pMelhpV3JUOVkzcjl1cTR4UVd6Zz09&sa=D&source=calendar&usd=2&usg=AOvVaw0SMrjNzSOUddjpaY3nOnCC). 

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign talks = site.data.thematic-discussions %}

## Upcoming Discussions
{% assign talks = site.data.thematic-discussions | sort: "start-date-time" %}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds > now %}{% continue %}{% endunless %}

  {% include discussion_item.html talk=talk %}

{% endfor %}

## Past Discussions
{% assign talks = site.data.thematic-discussions | sort: "start-date-time" | reverse %}

{% for semester in site.data.calendar.semesters %}

### {{semester.name}}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now and talk.semester == semester.tag %}{% continue %}{% endunless%}

  {% include discussion_item.html talk=talk is_previous=true %}

{% endfor %}

{% endfor %}

