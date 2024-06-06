---
layout: article
title: Public Colloquia
aside:
  toc: true
---

Please [sign up for our mailing list](http://mailman.mit.edu/mailman/listinfo/iaifi-news) to receive updates on IAIFI events.

You can [watch our Past Colloquia recordings on YouTube](https://www.youtube.com/channel/UCueoFcGm_15kSB-wDd4CBZA).

## Upcoming Colloquia 

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.colloquia %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
  {% if talk.type == "spring-2024" %}
  {% if talk.talk-abstract %}
<img class="image" src="{{talk.speaker-photo-location}}" align="right" style="max-width:226px;width:20%" hspace="10" vspace="10"/>
  {% else %}
  <img class="image" src="{{talk.speaker-photo-location}}" align="right" style="max-width:226px;width:8%" hspace="10" vspace="10"/>
  {% endif %}

  {% if talk.talk-abstract %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
  {% else %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
  {% endif %}
  {% endif %}
  {% endif %}
{% endfor %}

## Past Colloquia 

### Spring 2024

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.colloquia %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "spring-2024" %}

<img class="image" src="{{talk.speaker-photo-location}}" align="right" style="max-width:226px;width:20%" hspace="10" vspace="10"/>

{% if talk.slides-link %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> &#124; <a href="{{talk.slides-link}}">Talk Slides</a> {% else %} <a href="{{talk.slides-link}}">Talk Slides</a> {% endif %}
{% else %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> {% else %} Slides and recording not available. {% endif %}
{% endif %}
  {% endif %}
  {% endif %}
{% endfor %}

### Fall 2023

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.colloquia %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "fall-2023" %}

<img class="image" src="{{talk.speaker-photo-location}}" align="right" style="max-width:226px;width:20%" hspace="10" vspace="10"/>

{% if talk.slides-link %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> &#124; <a href="{{talk.slides-link}}">Talk Slides</a> {% else %} <a href="{{talk.slides-link}}">Talk Slides</a> {% endif %}
{% else %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> {% else %} Slides and recording not available. {% endif %}
{% endif %}
  {% endif %}
  {% endif %}
{% endfor %}

### Spring 2023

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.colloquia %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "spring-2023" %}

<img class="image" src="{{talk.speaker-photo-location}}" align="right" style="max-width:226px;width:20%" hspace="10" vspace="10"/>

{% if talk.slides-link %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> &#124; <a href="{{talk.slides-link}}">Talk Slides</a> {% else %} <a href="{{talk.slides-link}}">Talk Slides</a> {% endif %}
{% else %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> {% else %} Slides and recording not available. {% endif %}
{% endif %}
  {% endif %}
  {% endif %}
{% endfor %}

### Fall 2022

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.colloquia %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "fall-2022" %}

<img class="image" src="{{talk.speaker-photo-location}}" align="right" style="max-width:226px;width:20%" hspace="10" vspace="10"/>

{% if talk.slides-link %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> &#124; <a href="{{talk.slides-link}}">Talk Slides</a> {% else %} <a href="{{talk.slides-link}}">Talk Slides</a> {% endif %}
{% else %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> {% else %} Slides and recording not available. {% endif %}
{% endif %}
  {% endif %}
  {% endif %}
{% endfor %}

&nbsp;
### Spring 2022

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.colloquia %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "spring-2022" %}

<img class="image" src="{{talk.speaker-photo-location}}" align="right" style="max-width:226px;width:20%" hspace="10" vspace="10"/>

{% if talk.slides-link %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> &#124; <a href="{{talk.slides-link}}">Talk Slides</a> {% else %} <a href="{{talk.slides-link}}">Talk Slides</a> {% endif %}
{% else %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> {% else %} Slides and recording not available. {% endif %}
{% endif %}
  {% endif %}
  {% endif %}
{% endfor %}


### Fall 2021

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.colloquia %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "fall-2021" %}

<img class="image" src="{{talk.speaker-photo-location}}" align="right" style="max-width:226px;width:20%" hspace="10" vspace="10"/>

{% if talk.slides-link %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> &#124; <a href="{{talk.slides-link}}">Talk Slides</a> {% else %} <a href="{{talk.slides-link}}">Talk Slides</a> {% endif %}
{% else %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> {% else %} Slides and recording not available. {% endif %}
{% endif %}
  {% endif %}
  {% endif %}
{% endfor %}

### Spring 2021

In Spring 2021, our colloquium series featured IAIFI senior investigators, aiming to introduce you to some of the exciting research being carried out at our institute. 

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.colloquia %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "spring-2021" %}

<img class="image" src="{{talk.speaker-photo-location}}" align="right" style="max-width:226px;width:20%" hspace="10" vspace="10"/>

{% if talk.slides-link %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> &#124; <a href="{{talk.slides-link}}">Talk Slides</a> {% else %} <a href="{{talk.slides-link}}">Talk Slides</a> {% endif %}
{% else %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * {% if talk.youtube-link %} <a href="{{talk.youtube-link}}">YouTube Recording</a> {% else %} Slides and recording not available. {% endif %}
{% endif %}
  {% endif %}
  {% endif %}
{% endfor %}
