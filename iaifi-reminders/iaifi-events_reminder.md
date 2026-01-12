---
layout: article
header: false
footer: false
title: "IAIFI Colloquium Reminder"
show_title: false
--- 

{% assign target_date = "2026-02-13" %}
{% assign formatted_target = target_date | date: "%A, %B %e, %Y" %}

Dear IAIFI, 

A reminder that we will be hosting the following event(s) on {{formatted_target}}: 

<!-- Getting all events and sorting them by time -->
{% assign event_list = '' | split: '' %}
{% for event_type in site.data.calendar.event_types %}
{% assign event_list = event_list | concat: site.data[event_type] %}
{% endfor %}
{% assign event_list = event_list| sort: "start-date-time" %}

{% for event in event_list %}
  {% include_relative iaifi-all_event_item.html talk=event target_date=target_date %}
{% endfor %}

We hope to see you at these events!

