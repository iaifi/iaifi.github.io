---
layout: article
title: Lunch Discussions
aside:
  toc: true
---
<!-- Note that this pulls data from the journal-club.yml file, as of January 2026. There is no lunch-discussions.yml file.-->
The IAIFI Lunch Discussions are open to IAIFI members and affiliates. *Formerly called the IAIFI Journal Club.*

[Suggest a discussion topic, or sign up to lead a discussion!](https://forms.gle/zfpT4QQdXg8tu6VB7)

{% assign now = 'now' | date: '%s' | plus: 0 %}

## Upcoming Lunch Discussions
{% assign talks = site.data.journal-club | sort: "start-date-time" %}

{% for talk in talks %}
{% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
{% unless start_date_time_in_seconds > now %}{% continue %}{% endunless %}

{% include journal-club_item.html talk=talk %}

{% endfor %}

## Past Lunch Discussions
{% assign talks = site.data.journal-club | sort: "start-date-time" | reverse %}

{% for semester in site.data.calendar.semesters %}

### {{semester.name}}

{% for talk in talks %}
{% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
{% unless start_date_time_in_seconds < now and talk.semester == semester.tag %}{% continue %}{% endunless%}

{% include journal-club_item.html talk=talk is_previous=true %}

{% endfor %}

{% endfor %}
