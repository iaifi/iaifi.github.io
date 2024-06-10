---
layout: article
title: Public Colloquia
aside:
  toc: true
---

Please [sign up for our mailing list](http://mailman.mit.edu/mailman/listinfo/iaifi-news) to receive updates on IAIFI events.

You can [watch our Past Colloquia recordings on YouTube](https://www.youtube.com/channel/UCueoFcGm_15kSB-wDd4CBZA).

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign talks = site.data.colloquia %}

## Upcoming Colloquia 

{% for talk in talks %}
  {% assign talk-date = talk.talk-date | date: '%s' | plus: 0 %}
  {% unless talk-date > now %}{% continue %}{% endunless %}

  {% include colloquium_item.html talk=talk %}

{% endfor %}

## Past Colloquia 

{% for semester in site.data.calendar.semesters %}

### {{semester.name}}

{% for talk in talks %}
  {% assign talk-date = talk.talk-date | date: '%s' | plus: 0 %}
  {% unless talk-date < now and talk.type == semester.tag %}{% continue %}{% endunless%}

  {% include colloquium_item.html talk=talk is_previous=true %}

{% endfor %}

{% endfor %}
