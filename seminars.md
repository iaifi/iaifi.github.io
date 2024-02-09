---
layout: article
title: Internal Discussion Seminars
aside:
  toc: true
---

## Upcoming Seminars
{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.seminars %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
  {% if talk.type == "spring-2024" %}

* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
  {% endif %}
  {% endif %}
{% endfor %}


## Past Seminars
[Access recordings of past seminars (for IAIFI members only)](https://docs.google.com/document/d/1ZGLuC_-eqMwyeeJNbwR5YhEg_S18E8akbDE9m39oYsY/edit?usp=sharing)

### Spring 2024 Seminars

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.seminars %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "spring-2024" %}

* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * <a href="{{talk.slides-link}}">Talk Slides</a> (For IAIFI members only)
  {% endif %}
  {% endif %}
{% endfor %}

### Fall 2023 Seminars

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.seminars %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "fall-2023" %}

* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * <a href="{{talk.slides-link}}">Talk Slides</a> (For IAIFI members only)
  {% endif %}
  {% endif %}
{% endfor %}

### Spring 2023 Seminars

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.seminars %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "spring-2023" %}

* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * <a href="{{talk.slides-link}}">Talk Slides</a> (For IAIFI members only)
  {% endif %}
  {% endif %}
{% endfor %}

### Fall 2022 Seminars

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.seminars %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "fall-2022" %}

* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * <a href="{{talk.slides-link}}">Talk Slides</a> (For IAIFI members only)
  {% endif %}
  {% endif %}
{% endfor %}
    
### Spring 2022 Seminars

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.seminars %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "spring-2022" %}

* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * <a href="{{talk.slides-link}}">Talk Slides</a> (For IAIFI members only)
  {% endif %}
  {% endif %}
{% endfor %}

### Fall 2021 Seminars

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.seminars %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "fall-2021" %}

* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * <a href="{{talk.slides-link}}">Talk Slides</a> (For IAIFI members only)
  {% endif %}
  {% endif %}
{% endfor %}


### Spring 2021 Seminars

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.seminars %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "spring-2021" %}

* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}**
    * *{{talk.talk-title}}*
    * <a href="{{talk.slides-link}}">Talk Slides</a> (For IAIFI members only)
  {% endif %}
  {% endif %}
{% endfor %}

