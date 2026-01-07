---
layout: article
header: false
footer: false
title: "IAIFI Announcements: Spring 2026"
show_title: false
--- 


{% include_relative iaifi-reminder_header.html %}

## Announcing IAIFI Spring 2026 Public Colloquium Series

We are pleased to announce the lineup for our Spring 2026 IAIFI Colloquium series, featuring researchers at the intersection of Physics and AI from a variety of sectors. 

Each colloquium will be broadcast over Zoom (details below), and live on [our YouTube channel](https://www.youtube.com/channel/UCueoFcGm_15kSB-wDd4CBZA), where you can view recordings of past colloquia as well. We will send additional details about each colloquium as it approaches, and you can view updates on [the IAIFI Public Events page](https://iaifi.org/events.html).

If you are local to the Boston area and would like to attend IAIFI events in person, please [complete the interest form](https://app.smartsheet.com/b/form/3cff913c564141249c4292ad8c435774) to be added as a Friend of IAIFI.

We hope you can join us for this round of IAIFI colloquia!

{% assign talks = site.data.colloquia | sort: "start-date-time" %}
{% for talk in talks %}
  {% unless talk.semester == "spring-2026" %}{% continue %}{% endunless %}
* **{{talk.start-date-time | date: "%B %-d"}}: [{{talk.speaker-name}}]({{talk.speaker-website}}) ({{talk.speaker-title}}, {{talk.speaker-affiliation}})**
    * [Add to your calendar]({{talk.calendar-link}})
{% endfor %}
    
[Join on Zoom](https://mit.zoom.us/j/91200832411){:.button.button--outline-primary.button--pill.button--sm}    [More Information](https://iaifi.org/events.html){:.button.button--outline-primary.button--pill.button--sm} 

While you wait, catch up on our previous colloquia on YouTube:

[Fall 2025](https://youtube.com/playlist?list=PLBY0ED2StbGaFMHOCrNUFmQyobejsegHT&si=CviAB4YEV08qUr9O){:.button.button--outline-primary.button--pill.button--sm} 
[Spring 2025](https://youtube.com/playlist?list=PLBY0ED2StbGb7VsUi73x6Dp4vkHT0LQ1k&si=D1FYHklvjXCBGLH0){:.button.button--outline-primary.button--pill.button--sm} 

## In Other News...

### IAIFI Summer School 2026: Applications Open, Due February 9, 2026!

We are pleased to announce that registration is now open for the 2026 IAIFI Summer School, featuring lectures, hands-on tutorials, lightning talks, a hackathon, and networking events.

[Apply to the 2026 IAIFI Summer School](https://iaifi.org/phd-summer-school){:.button.button--outline-primary.button--pill.button--lg}

* **When:** August 3–7, 2026 
* **Where:** Boston, MA (exact location TBA)
* **What:** Four days of lectures and tutorials on the following topics: Generative Modeling/Diffusion, Symbolic Regression, Computer Vision, and Simulation-Based Inference; a full-day hackathon, with time built into the week to begin working on projects; and networking events, including a career panel
* **Registration Deadline: Monday, February 9, 2026.** Space may be limited, so a brief application is required. You will be notified of your registration status by February 16, 2026. 
* **Costs:** There will be no fee to attend the IAIFI Summer School. Dorms will be available for attendees to book and IAIFI will reimburse up to 5 nights (contingent upon attendance) after the event. Attendees are expected to cover the costs of travel.

### Save the Date: IAIFI Summer Workshop 2026

We hope you can also save the date for IAIFI Summer Workshop, which will be held August 10-14, 2026 in Boston, MA. More details will be provided early in 2026.

[IAIFI Summer Workshop Updates](https://iaifi.org/summer-workshop){:.button.button--outline-primary.button--pill.button--lg}

{% include_relative iaifi-reminder_footer.html %}

