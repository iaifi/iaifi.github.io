---
layout: article
title: "Pre-Event CoC"
show_title: false
---

{% assign now = 'now' | date: '%s' | plus: 0 %}
{% assign event-time = 'now' | date: '%s' | plus: 900 %}

{% assign talks = site.data.colloquia | sort: "start-date-time" %}

{% for talk in talks %}
  {% assign start_date_time_in_seconds = talk.start-date-time | date: '%s' | plus: 0 %}
  {% unless start_date_time_in_seconds < event-time %}{% continue %}{% endunless %}

  {% include colloquium_item.html talk=talk %}

{% endfor %}

## IAIFI Code of Conduct

Regardless of their position or seniority, members of the IAIFI and participants in IAIFI activities are expected to:

* Act in an ethical and collaborative manner at all times and abide by the [MIT Physics Community Values](https://physics.mit.edu/about-physics/community-values/)
* Work with the utmost scientific integrity and respect the confidentiality of information and work presented at internal IAIFI meetings
* Treat each other with dignity and respect, support and encourage each other's growth, and step in as needed to maintain an environment free of discrimination, harassment, and bullying

Furthermore, members of the IAIFI and participants in IAIFI activities may not engage in retaliation against anyone for objecting to a behavior that may violate this code, reporting a violation of this code, or participating in the resolution of such a complaint.


