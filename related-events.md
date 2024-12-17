---
layout: article
title: Related Events
aside:
  toc: true
---

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign talks = site.data.external-events %}

## Related Events

### Upcoming External Events

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds > now %}{% continue %}{% endunless %}

  {% if talk.type == "external-event" %}
  {% include related-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

### Upcoming Workshops

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds >= now %}{% continue %}{% endunless %}

  {% if talk.type == "workshop" %}
  {% include related-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

### Past Workshops

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < now %}{% continue %}{% endunless %}

  {% if talk.type == "workshop" %}
  {% include related-event_item.html talk=talk %}
  {% endif %}
{% endfor %}

## Related Organizations

Other organizations that hold public events relevant to the IAIFI community:

  * [SERC Symposium, MIT Schwarzman College of Computing](https://computing.mit.edu/cross-cutting/social-and-ethical-responsibilities-of-computing/serc-symposium/?mc_cid=890e6a3190&mc_eid=918e0bd2e4)
  * [A3D3 Seminars](https://indico.cern.ch/category/14431/)
  * [Physics Meets ML](http://www.physicsmeetsml.org/)
  * [NSF AI Planning Institute for Data-Driven Discovery in Physics Seminar Series](https://www.cmu.edu/ai-physics-institute/events/index.html)
  * [CLARIPHY Topical Meetings](https://clariphy.org/topical.html)
  * [Understanding the Nature of Inference Colloquia](https://inferenceproject.yale.edu/colloquium-series)
  * [Stochastics and Statistics Seminars presented by the MIT Statistics and Data Science Center](https://stat.mit.edu/seminars/)
  * [CMSA New Technologies in Mathematics Seminar Series at Harvard](https://cmsa.fas.harvard.edu/tech-in-math/)
  * [Invitation to MIT conference on Mechanistic Interpretability](https://docs.google.com/forms/d/e/1FAIpQLSflee__rtDzXkHMSd-iCD873QhcCp4Dr0ysw7QlIy4vYzdnzA/viewform)
  * [AstroAI Lunch Talks](https://astroai.cfa.harvard.edu/events/)

