---
layout: article
title: Funding Opportunities
aside:
  toc: true
---

As a hub for the intersection of Physics and AI in the Boston area and beyond, we are happy to share funding opportunities at this intersection as we become aware of them. 
{:.info}

Note: These are opportunities external to IAIFI. For IAIFI-related job opportunities, see our [IAIFI Jobs page](/job-board.html).

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign funding = site.data.funding | sort | reverse %}
{% for opportunity in funding %}
  {% capture date %}{{opportunity.expire | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
**{{opportunity.title}}** <br>
*{{opportunity.funder}}* <br>
{%if opportunity.deadline %} Deadline: {{opportunity.deadline}} | {% endif %} [Learn more]({{opportunity.link}}) <br>
<div style = "position:relative; top:-1em;" >
<details>
<summary>Details</summary>
<em>{{opportunity.details}}</em>
</details>
</div>
{% endif %}
{% endfor %}

