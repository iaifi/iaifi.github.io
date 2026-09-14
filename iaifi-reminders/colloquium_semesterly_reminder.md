---
layout: article
header: false
footer: false
title: "IAIFI Announcements: Spring 2026"
show_title: false
--- 


{% include_relative iaifi-reminder_header.html %}

## Announcing IAIFI Fall 2026 Public Colloquium Series

We are pleased to announce the lineup for our Fall 2026 IAIFI Colloquium series, featuring researchers at the intersection of Physics and AI from a variety of sectors. 

Each colloquium will be broadcast over Zoom (details below), and live on [our YouTube channel](https://www.youtube.com/channel/UCueoFcGm_15kSB-wDd4CBZA). We will send additional details about each colloquium as it approaches, and you can view updates on [the IAIFI Public Events page](https://iaifi.org/events.html).

*If you are local to the Boston area and would like to attend IAIFI events in person, please [complete the interest form](https://app.smartsheet.com/b/form/3cff913c564141249c4292ad8c435774) to be added as a Friend of IAIFI.*

[Join on Zoom](https://mit.zoom.us/j/91200832411){:.button.button--outline-primary.button--pill.button--sm}    [More Information](https://iaifi.org/events.html){:.button.button--outline-primary.button--pill.button--sm} 

We hope you can join us for this round of IAIFI colloquia!

{% assign talks = site.data.colloquia | sort: "start-date-time" %}
{% for talk in talks %}
  {% unless talk.semester == "fall-2026" %}{% continue %}{% endunless %}
* **{{talk.start-date-time | date: "%B %-d"}}: [{{talk.speaker-name}}]({{talk.speaker-website}}) ({{talk.speaker-title}}, {{talk.speaker-affiliation}})**{% if talk.talk-title %}: {{talk.talk-title}} {% endif %} \| [Add to your calendar]({{talk.calendar-link}})
{% endfor %}

While you wait, catch up on our [previous colloquia on YouTube](https://www.youtube.com/channel/UCueoFcGm_15kSB-wDd4CBZA).

## Reminder: IAIFI Fellowship Applications due October 7, 2026
Applications for the seventh round of IAIFI's Postdoctoral Fellowship for early-career scientists working at the intersection of Physics and AI are due on Wednesday, October 7, 2026.

[Apply on AJO](https://academicjobsonline.org/ajo/jobs/32251){:.button.button--outline-primary.button--pill.button--lg} [Learn more about the IAIFI Fellowship](https://iaifi.org/fellows){:.button.button--outline-primary.button--pill.button--lg}

## IAIFI Management Update

Jesse Thaler, who has served as IAIFI Director since we formed in 2020, has [been named Director of MIT's Laboratory for Nuclear Science](https://news.mit.edu/2026/jesse-thaler-named-director-laboratory-nuclear-science-0707) and is handing over the reigns as IAIFI Director to Mike Williams! Subsequently, Phiala Shanahan is taking on the role of IAIFI Deputy Director, previously held by Mike. Thank you to Jesse for five years of visionary leadership, we look forward to having Mike and Phiala at the helm!

{% include_relative iaifi-reminder_footer.html %}

