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

Each colloquium will be broadcast over Zoom (details below), and live on [our YouTube channel](https://www.youtube.com/channel/UCueoFcGm_15kSB-wDd4CBZA). We will send additional details about each colloquium as it approaches, and you can view updates on [the IAIFI Public Events page](https://iaifi.org/events.html).

*If you are local to the Boston area and would like to attend IAIFI events in person, please [complete the interest form](https://app.smartsheet.com/b/form/3cff913c564141249c4292ad8c435774) to be added as a Friend of IAIFI.*

[Join on Zoom](https://mit.zoom.us/j/91200832411){:.button.button--outline-primary.button--pill.button--sm}    [More Information](https://iaifi.org/events.html){:.button.button--outline-primary.button--pill.button--sm} 

We hope you can join us for this round of IAIFI colloquia!

{% assign talks = site.data.colloquia | sort: "start-date-time" %}
{% for talk in talks %}
  {% unless talk.semester == "spring-2026" %}{% continue %}{% endunless %}
* **{{talk.start-date-time | date: "%B %-d"}}: [{{talk.speaker-name}}]({{talk.speaker-website}}) ({{talk.speaker-title}}, {{talk.speaker-affiliation}})**{% if talk.talk-title %}: {{talk.talk-title}} {% endif %} \| [Add to your calendar]({{talk.calendar-link}})
{% endfor %}

While you wait, catch up on our previous colloquia on YouTube:

[Fall 2025](https://youtube.com/playlist?list=PLBY0ED2StbGaFMHOCrNUFmQyobejsegHT&si=CviAB4YEV08qUr9O){:.button.button--outline-primary.button--pill.button--sm}
[Spring 2025](https://youtube.com/playlist?list=PLBY0ED2StbGb7VsUi73x6Dp4vkHT0LQ1k&si=D1FYHklvjXCBGLH0){:.button.button--outline-primary.button--pill.button--sm}
[Fall 2024](https://youtube.com/playlist?list=PLBY0ED2StbGYRJ6pDz92KnxGpVS40m16k&si=A7VKuuDT3kPkwG_R){:.button.button--outline-primary.button--pill.button--sm}
[Spring 2024](https://youtube.com/playlist?list=PLBY0ED2StbGYMooZlcZXlEORbSISo1fWQ&si=TIfyC2paRtLlYLRl){:.button.button--outline-primary.button--pill.button--sm}
[Fall 2023](https://youtube.com/playlist?list=PLBY0ED2StbGa_CwDvA1l747j0nh6Yc42E&si=pu9oZ6uTUu-I41eM){:.button.button--outline-primary.button--pill.button--sm}
[Spring 2023](https://youtube.com/playlist?list=PLBY0ED2StbGZKP9i6M-3hiZSpxkCsW2jX&si=NAKwB2O29yxSIXKi){:.button.button--outline-primary.button--pill.button--sm}
[Fall 2022](https://youtube.com/playlist?list=PLBY0ED2StbGbnP4OH5_ggH1QvoO3nyOw7&si=WrUYsw4g0PPL4HI8){:.button.button--outline-primary.button--pill.button--sm}
[Spring 2022](https://youtube.com/playlist?list=PLBY0ED2StbGbd6ZhDB6Yhg2tB_jnXrxuJ&si=LjdJ6iLsGjj2UhpR){:.button.button--outline-primary.button--pill.button--sm}
[Fall 2021](https://youtube.com/playlist?list=PLBY0ED2StbGZtEAbnyZz9p3pK31qHLXmq&si=XShiq9Jv4QlNdoGX){:.button.button--outline-primary.button--pill.button--sm}
[Spring 2021](https://youtube.com/playlist?list=PLBY0ED2StbGZihzDLwNtPZtsdUvDRVyfG&si=f0DXvxhcta7Isa8L){:.button.button--outline-primary.button--pill.button--sm}

{% include_relative iaifi-reminder_footer.html %}

