---
layout: article
header: false
footer: false
title: "IAIFI Fall 2025 Wrap-Up"
show_title: false
--- 
<div align="center"  markdown="1">
   [Display this email in your browser](https://iaifi.org/digest/{{digest_date}}){:.button.button--xs}
</div>
<p align="center">
<img src="https://iaifi.org/images/iaifi-pressimage-horizontalcrop-smaller.jpg" align="center" style="max-width:5990px;width:100%" hspace="10" vspace="10"> 
</p>

# IAIFI Fall 2025 Wrap-Up

[IAIFI Opportunities](#iaifi-opportunities){:.button.button--outline-primary.button--pill.button--sm} [Colloquia](#iaifi-colloquium-series){:.button.button--outline-primary.button--pill.button--sm} [Research Highlights](#iaifi-research-highlights){:.button.button--outline-primary.button--pill.button--sm} [Research Papers](#iaifi-research-on-arxiv){:.button.button--outline-primary.button--pill.button--sm} [Event Highlights and News](#in-case-you-missed-it){:.button.button--outline-primary.button--pill.button--sm} [Join IAIFI](#join-iaifi){:.button.button--outline-primary.button--pill.button--sm}

## News from IAIFI Management

Thank you to everyone who attended our events this Fall and otherwise engaged with IAIFI on our research and activities at the intersection of AI and Physics! We have summarized some highlights and information from IAIFI for Fall 2025. Please feel free to reach out to us with questions or comments about any of the below. Best wishes for a safe and pleasant holiday season!

## IAIFI Opportunities

<img src="https://iaifi.org/images/phd-summer-school-logo-2026.png" align="center" style="float: right;max-width:5990px;width:50%" hspace="10" vspace="10"> 

### IAIFI Summer School

Apply for our [2026 IAIFI Summer School](https://iaifi.org/phd-summer-school.html#summer-school-2026), featuring lectures and events that illustrate interdisciplinary research at the intersection AI and Physics and encourage global networking. Hands-on code-based tutorials that build on foundational lecture materials help students put theory into practice, and a hackathon project provides an opportunity for students to collaborate and apply what they’ve learned. The mission of the IAIFI Summer School is to leverage the expertise of IAIFI researchers, affiliates, and partners toward promoting education and workforce development.

**Application details:**
- The [application deadline](https://app.smartsheet.com/b/form/019a9d12ef3e7cb4b5a3855a4c092845) is **February 9, 2026**. Applicants will be notified of their status by February 16, 2026.
- There is no registration fee for the Summer School. Costs of dorm accommodations will be reimbursed by IAIFI, contingent upon attendance. Students for the Summer School are expected to cover the cost of travel.
- Lunch each day, as well as coffee and snacks at breaks, will be provided during the Summer School, along with at least one dinner during the Summer School.
- Virtual attendance can be accomodated.


**Summer School Details:**
- When: August 3–August 7, 2026
- Where: Boston/Cambridge, MA (exact location TBA)
- What: View the agenda [on the Summer School webpage](https://iaifi.org/phd-summer-school.html#lecturers). Lecturer details will be added as they are confirmed by the organizing committee.
- See [FAQs](https://iaifi.org/phd-summer-school.html#faq) on the Summer School webpage

<img src="https://iaifi.org/images/summer-workshop-logo_2026.png" align="left" style="float: left;max-width:5990px;width:30%" hspace="10" vspace="10"> 
**Also save the date for the IAIFI Summer Workshop 2026, which will be held August 10–14, 2026 in Boston/Cambridge (exact location TBA)! Registration will open in January 2026.**

<br>

## IAIFI Colloquium Series

Thank you to our speakers for this term: [Francisco Villaescusa-Navarro](https://franciscovillaescusa.github.io/), [Berthy Feng](https://www.berthyfeng.com/), [Peter Lu](https://petery.lu/), [Andy Keller](https://akandykeller.github.io/), [Melanie Weber](https://melanie-weber.com/), and [T. Konstantin Rusch](https://camail.org/)! 


The IAIFI Colloquium series will continue in Spring 2026 with the following speakers.
- February 13: [Roger Melko (University of Waterloo)](https://rgmelko.github.io/)
- February 27: [Lisa Everett (University of Wisconsin-Madison)](https://home.physics.wisc.edu/leverett/)
- March 13: [Roberto Trotta (SISSA)](https://robertotrotta.com/)
- April 10: [Tommaso Dorigo (INFN)](https://userswww.pd.infn.it/~dorigo/)
- April 24: [James Requeima (Google DeepMind)](https://jamesr.info/)
- May 8: [Yury Polyanskiy (MIT)](https://people.lids.mit.edu/yp/homepage/)

 If you missed any of this semester's colloquia, you can watch recordings of all [Fall 2025 colloquia](https://youtube.com/playlist?list=PLBY0ED2StbGaFMHOCrNUFmQyobejsegHT&si=yfomkBIPFhGDPyvv) on our YouTube channel, as well as [recordings from previous semesters](https://youtube.com/@iaifiinstituteforaifundame3333?feature=shared).

## IAIFI Research Highlights

IAIFI regularly posts research highlights on our website, showcasing the innovative work of IAIFI investigators. View our Summer 2025 and Fall 2025 research highlights below!

- [AutoSciDACT: Automated Scientific Discovery through Contrastive Embedding and Hypothesis Testing](https://iaifi.org/research.html#autoscidact-automated-scientific-discovery-through-contrastive-embedding-and-hypothesis-testing)
- [Evidence for an Instability-induced Binary Merger in the Double-peaked, Helium-rich Type IIn Supernova 2023zkd](https://iaifi.org/research.html#evidence-for-an-instability-induced-binary-merger-in-the-double-peaked-helium-rich-type-iin-supernova-2023zkd)
- [Enhancing events in neutrino telescopes through deep-learning-driven superresolution](https://iaifi.org/research.html#enhancing-events-in-neutrino-telescopes-through-deep-learning-driven-superresolution)
- [Remove Symmetries to Control Model Expressivity and Improve Optimization](https://iaifi.org/research.html#remove-symmetries-to-control-model-expressivity-and-improve-optimization)
- [LEAPS: A discrete neural sampler via locally equivariant networks](https://iaifi.org/research.html#leaps-a-discrete-neural-sampler-via-locally-equivariant-networks)

[View all Research Highlights](https://iaifi.org/research.html#highlights){:.button.button--outline-primary.button--pill.button--sm}

## IAIFI Research on arXiv

Read the latest [IAIFI papers](https://iaifi.org/papers.html) on arXiv! Here, the papers are grouped by the four IAIFI research domains. 

### Foundational AI
{% assign start_date = '2025-06-01' | date: '%s' %}
{% assign end_date = '2025-12-31' | date: '%s' %}
{% assign products = site.data.products | sort | reverse %}
{% for product in products %}
{% assign paper = product %}
{% if paper.type == "paper" %}
{% if paper.iaifi-thrust == "F" %}
{% assign paper_date = paper.arxiv-date | date: '%s' %}
{% if paper_date >= start_date and paper_date <= end_date %}
{% assign arxiv_url = "https://arxiv.org/abs/" | append: paper.arxiv %}
- [{{paper.title}}]({%if paper.doi != blank %}{{paper.doi}}){%else %}{{arxiv_url}})<br>
{% endif %}
{% endif %}
{% endif %}
{% endif %}
{% endfor %}

### Theoretical Physics
{% for product in products %}
{% assign paper = product %}
{% if paper.type == "paper" %}
{% if paper.iaifi-thrust == "T" %}
{% assign paper_date = paper.arxiv-date | date: '%s' %}
{% if paper_date >= start_date and paper_date <= end_date %}
{% assign arxiv_url = "https://arxiv.org/abs/" | append: paper.arxiv %}
- [{{paper.title}}]({%if paper.doi != blank %}{{paper.doi}}){%else %}{{arxiv_url}})<br>
{% endif %}
{% endif %}
{% endif %}
{% endif %}
{% endfor %}

### Experimental Physics
{% for product in products %}
{% assign paper = product %}
{% if paper.type == "paper" %}
{% if paper.iaifi-thrust == "E" %}
{% assign paper_date = paper.arxiv-date | date: '%s' %}
{% if paper_date >= start_date and paper_date <= end_date %}
{% assign arxiv_url = "https://arxiv.org/abs/" | append: paper.arxiv %}
- [{{paper.title}}]({%if paper.doi != blank %}{{paper.doi}}){%else %}{{arxiv_url}})<br>
{% endif %}
{% endif %}
{% endif %}
{% endif %}
{% endfor %}

### Astrophysics
{% for product in products %}
{% assign paper = product %}
{% if paper.type == "paper" %}
{% if paper.iaifi-thrust == "A" %}
{% assign paper_date = paper.arxiv-date | date: '%s' %}
{% if paper_date >= start_date and paper_date <= end_date %}
{% assign arxiv_url = "https://arxiv.org/abs/" | append: paper.arxiv %}
- [{{paper.title}}]({%if paper.doi != blank %}{{paper.doi}}){%else %}{{arxiv_url}})<br>
{% endif %}
{% endif %}
{% endif %}
{% endif %}
{% endfor %}

## In Case You Missed It

[Learn More about IAIFI Public Engagement Activities](https://iaifi.org/outreach.html){:.button.button--outline-primary.button--pill.button--sm}

### Splash Fall 2025
**November 22, 2025**

<img src="https://iaifi.org/images/small-photo-splash2025-joydeep.jpg" align="center" style="float: right; max-width:5990px;width:35%" hspace="10" vspace="0"> 

IAIFI was pleased to participate in [MIT's Splash program](https://esp.mit.edu/learn/Splash/index.html) this year! IAIFI members Christian Ferko (Northeastern), Christina Reissel (MIT), Jamie Sullivan (MIT), and Joydeep Naskar (Northeastern)shared an overview of their work with a group of around 100 high school students and answered questions related to AI and Physics!

<br><br>

### Cambridge Science Carnival 2025
**September 21, 2025**

<img src="https://iaifi.org/images/small-photo-2025-cambridgesciencecarnival.jpg" align="center" style="float: right; max-width:5990px;width:35%" hspace="10" vspace="0"> 

We hosted a booth at the [Cambridge Science Carnival](https://cambridgesciencefestival.org) for the fourth year in a row! This included several AI+Physics activities for all ages, and IAIFI members were able to chat with more than 500 community members across the afternoon. 
<br><br>

### Summer School and Workshop
**August 2025**

In August 2025, we held our fourth annual Summer School and Workshop at Harvard. The Summer School included lectures, hands-on tutorials, lightning talks, networking events, etc. The Summer Workshop featured plenary talks, poster sessions, and networking events. We were also excited to partner with the Boston Museum of Science for our Summer Workshop dinner, when we also hosted a [planetarium show about AI and the search for dark matter](https://www.mos.org/events/beyond-telescope/unveiling-invisible-milky-way-ai), led by IAIFI Senior Investigator Lina Necib.

[Watch the 2025 Workshop Talks on YouTube](https://youtube.com/playlist?list=PLBY0ED2StbGYicBdodtC3QqVVnwhr758-&si=kEw4EHgQHkfCFIbg){:.button.button--outline-primary.button--pill.button--sm}  [Apply for the 2026 Summer School](https://iaifi.org/phd-summer-school.html#apply){:.button.button--outline-primary.button--pill.button--sm}

<style>
  .image-row {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin: 10px 0;
  }
  .image-row img {
    width: 45%;
    max-width: 5990px;
    height: auto;
    flex-shrink: 0; 
    object-fit: contain; 
  }
</style>

<div class="image-row">
  <img src="https://iaifi.org/images/2025-summer-school-group-photo.jpeg" alt="Group photo">
  <img src="https://iaifi.org/images/small-photo-2025-summer-school-lecture.jpg" alt="Lecture">
</div>

<div class="image-row">
  <img src="https://iaifi.org/images/small-photo-2025-summer-workshop-dinner.jpg" alt="Dinner">
  <img src="https://iaifi.org/images/Workshop-2025_Sokratis.jpg" alt="Workshop">
</div>

### AI+Physics Science Communication

We had the opportunity to collaborate on two public engagement projects to communicate AI+Physics to the general public: 

* **Discovery Engines Podcast:** IAIFI Director Jesse Thaler chatted with host Nabil Laoudji about how AI is reshaping physics discovery and how physicists are reshaping AI. 

[Watch the episode on YouTube](https://youtu.be/FQJPvVhriYo){:.button.button--outline-primary.button--pill.button--sm}

* **ScienceClic Educational Video:** IAIFI Investigators collaborated with popular science YouTube channel ScienceClic on a video covering "The Physics of AI," which explores the connections between AI and Physics as related to the 2024 Nobel Prize in Physics, and the link between neural networks and quantum fields. 

[Watch the video on YouTube](https://youtu.be/dRkehLL19Wo?si=0J-6Sw5PhUq5n5ei){:.button.button--outline-primary.button--pill.button--sm}

### IAIFI News

- **IAIFI Junior Investigator Christian Ferko receives Museum of Science digital communication fellowship.** As a [2026 Museum of Science, Boston Digital Science Communication Fellow](https://www.linkedin.com/feed/update/urn:li:activity:7404902033381560321), Christian will participate in specialized training in strategic storytelling, digital content creation, civic trust, and evidence-based communication.  *December 11, 2025*
    
- **IAIFI Investigators honored by Schmidt Sciences as 2025 Early Career Fellows.** IAIFI Fellow/Harvard Society of Fellows' Michael Albergo and IAIFI Senior Investigator/MIT Professor Tess Smidt were selected for the [AI2050 Early Career Fellowship](https://ai2050.schmidtsciences.org/fellows/), which is an enabling fellowship to encourage postdoctoral and pre-tenure researchers from around the world to pursue bold and ambitious work on hard problems in AI. *November 17, 2025*
  
- **IAIFI Senior Investigators collaborate with other interdisciplinary researchers on community white paper exploring "The Future of AI and the Mathematical and Physical Sciences."** The [white paper](https://arxiv.org/abs/2509.02661), which developed out of an NSF-funded Workshop held in March 2025, presents how the MPS domains (Astronomy, Chemistry, Materials Research, Mathematical Sciences, and Physics) can best capitalize on, and contribute to, the future of AI. *September 4, 2025*
  
- **IAIFI Summer School sponsor FirstPrinciples summarizes the impact of the School**. Read [Bridging Minds and Disciplines: The IAIFI Summer School and the Future of Collaborative Science](https://www.firstprinciples.org/article/bridging-minds-and-disciplines-the-iaifi-summer-school-and-the-future-of-collaborative-science?utm_source=linkedin&utm_medium=hub_post&utm_campaign=iaifi_summer_school). *August 15, 2025*
  
- **IAIFI Researchers and Collaborators Discover New Type of Supernova**. [Read about the discovery](https://www.cfa.harvard.edu/news/ai-helps-astronomers-discover-new-type-supernova), led by IAIFI Fellow Alex Gagliano along with IAIFI Senior Investigator Ashley Villar and their collaborators. *August 13, 2025*
  
- **IAIFI Deputy Director Mike Williams participates on panel at AI+Science Summit**. The panel, "[Powering Innovation at the Intersection of AI & Science: NSF’s AI Institutes](https://youtu.be/RlzN7UhuHL0?si=3C6cqb4SbP_IfX1B)" was hosted by the Special Competitive Studies Project at their AI+Science Summit. *July 23, 2025*
  
- **IAIFI Fellow Jessie Micallef receives Impact Award from MicroBooNE expirement**. Jessie received the award for contributions to the experiment. *July 20, 2025*
    
- **Marisa LaFleur promoted from IAIFI Project Manager to IAIFI Managing Director**. As IAIFI Managing Director, Marisa will continue to oversee the implementation of IAIFI activities and to expand her responsibilities related to IAIFI’s long-term strategy and funding. *July 9, 2025*

[View all IAIFI News](https://iaifi.org/#iaifi-news){:.button.button--outline-primary.button--pill.button--sm}

## Join IAIFI

*Visit [IAIFI's website](https://iaifi.org/) for more ways to engage with the community.*

### Senior Researchers in the Boston Area
Senior Researchers include faculty members and senior research scientists with PI status. If you are interested in becoming an IAIFI Affiliate, complete the [IAIFI Affiliate application form](https://app.smartsheet.com/b/form/b73212d8895c4436a947b2dfdd999da3). Affiliate applications must include a [Senior Investigator](https://iaifi.org/people.html#senior-investigators) sponsor.

[Details for Senior Researchers](https://iaifi.org/join.html#facultysenior-researchers){:.button.button--outline-primary.button--pill.button--sm}

### Junior Researchers in the Boston Area
Junior Researchers include undergraduate students, graduate students, postdocs, and research scientists without PI status. If you are interested in getting more involved in IAIFI as a junior researcher, complete the [Junior Researcher Interest Form](https://iaifi.org/junior-interest.html). 

[Details for Junior Researchers](https://iaifi.org/junior-researchers.html){:.button.button--outline-primary.button--pill.button--sm}

<p align="center">
<img src="https://iaifi.org/images/2025-Fall-members.jpeg" align="center" style="max-width:5990px;width:50%" hspace="10" vspace="10"> 
</p>

*IAIFI members participate in a variety of events throughout the semester, including colloquia, journal clubs, and networking events.*

{% include_relative iaifi-reminder_footer.html %}
