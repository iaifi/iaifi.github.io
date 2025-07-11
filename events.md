---
layout: article
title: Public Colloquia
aside:
  toc: true
---

Please [sign up for our mailing list](http://mailman.mit.edu/mailman/listinfo/iaifi-news) to receive updates on IAIFI events.

You can [watch our Past Colloquia recordings on YouTube](https://www.youtube.com/channel/UCueoFcGm_15kSB-wDd4CBZA).

Have suggestions for future speakers to invite? [Fill out the form here](https://app.smartsheet.com/b/form/01976a488bd173719f4b840aaf284212)!

{% assign now = 'now' | date: '%s' | plus: 0 %}

## Upcoming Colloquia 
{% assign talks = site.data.colloquia | sort: "start-date-time" %}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds > now %}{% continue %}{% endunless %}

  {% include colloquium_item.html talk=talk %}

{% endfor %}

## Past Colloquia 
{% assign talks = site.data.colloquia | sort: "start-date-time" | reverse %}

{% for semester in site.data.calendar.semesters %}

### {{semester.name}}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now and talk.semester == semester.tag %}{% continue %}{% endunless%}

  {% include colloquium_item.html talk=talk is_previous=true %}

{% endfor %}

{% endfor %}
