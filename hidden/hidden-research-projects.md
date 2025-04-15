---
layout: article
title: Research Projects (Hidden Page)
---

## Senior Investigator or Fellow Name

{% for project in site.data.research-projects %}

### {{project.title}}

**Project Lead:** {{project.project-lead}}

**Project Abstract:** {{project.project-abstract}}

**IAIFI members involved:** {{project.other-iaifi-leads}}; {{project.other-iaifi-members}}

**Non-IAIFI Collaborators:** {{project.other-collaborators}}

**Industry Partners:** {{project.industry-collaborators}}

**Inductive Bias Element:** {{project.inductive-bias}}

**Novel AI Approach:** {{project.novel-ai}}

**Next Steps for Project:** {{project.next-steps}}

**Papers:**

{{project.project-papers}}

**Talks Given:** 

{{project.talks-given}}

**Code:** {{project.project-code}}

<br> 

<p style="text-align: center;"><strong>{{project.title}}</strong></p>
<p style="text-align: center;">{{project.project-lead}}; {{project.other-iaifi-leads}}; {{project.other-iaifi-members}}; {{project.other-collaborators}}</p>

<br>

<div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 10px; width: 100%; height: 500px;">
  <!-- Top Left -->
  <div style="white-space: pre-line; border: 1px solid #ccc; padding: 10px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <strong>Project Goals</strong>
    {{ project.goals }}
  </div>

  <!-- Top Right: image + text -->
  <div style="border: 1px solid #ccc; padding: 10px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
    <img src="{{project.project-figure}}" alt="Example image" style="max-width: 100%; height: auto; margin-bottom: 10px;">
    <div>{{project.figure-caption}}</div>
  </div>

  <!-- Bottom Left -->
  <div style="white-space: pre-line; border: 1px solid #ccc; padding: 10px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <strong>Barriers and Methods to Overcome</strong>{{project.barriers}}
  </div>

  <!-- Bottom Right -->
  <div style="white-space: pre-line; border: 1px solid #ccc; padding: 10px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <strong>Research Achievements</strong>{{project.project-achievements}}
  </div>
</div>


{% endfor %}
