---
layout: article
title: Journal Club
aside:
  toc: true
---

The IAIFI Journal Club is open to IAIFI members and affiliates. 

[Sign up to lead a discussion!](https://forms.gle/zfpT4QQdXg8tu6VB7)

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign talks = site.data.journal-club %}

## Upcoming Journal Clubs

{% for talk in talks %}
{% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
{% unless start_date_time_in_seconds > now %}{% continue %}{% endunless %}

{% include journal-club_item.html talk=talk %}

{% endfor %}

## Past Journal Clubs

{% for semester in site.data.calendar.semesters %}

### {{semester.name}}

{% for talk in talks %}
{% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
{% unless start_date_time_in_seconds < now and talk.semester == semester.tag %}{% continue %}{% endunless%}

{% include journal-club_item.html talk=talk is_previous=true %}

{% endfor %}

{% endfor %}
