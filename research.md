---
layout: article
title: Research
---

By combining revolutionary advances in deep learning from AI with the time-tested strategies of deep thinking from physics, IAIFI researchers are gaining a deeper understanding of our universe and of intelligence itself. IAIFI's efforts have helped to establish the interdisciplinary field of AI+Physics, combining AI innovation with inductive biases from physics to advance both fields in a virtuous cycle. IAIFI is facilitating collaborations across the domains of **Foundational AI**, **Theoretical Physics**, **Experimental Physics**, and **Astrophysics** by using cross-cutting themes of *Representation/Manifold Learning*, *Generative Models*, *Uncertainty Quantification/Robust AI*, *Physics-Motivated Optimization*, and *Reinforcement Learning* to develop a common language. 

## [Domain Impact](/domain-research.html)

<style>
.card_header h4 {
  white-space: nowrap; 
}
</style>

<div class="grid-container">
  <div class="grid grid--p-2" style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">
    <div class="cell cell--4" style="flex: 0 0 48%; max-width: 48%; box-sizing: border-box;">
      <center>
      <a href="/domain-research.html#foundational-ai">
        <div class="card" style="height: 100%;">
          <div class="card_image">
          <img class="image" src="images/research-AI.png" style="width: 100%; height: auto;"/>
          </div>
              <div class="card_header">
              <h3><font color="cornflowerblue">FOUNDATIONAL AI</font></h3>
              <div class="card_content" style="font-size: 14px; color: black;">
              Infusing physics principles into AI to create state-of-the-art AI innovations
            </div>
          </div>
        </div>
      </a>
      </center>
    </div>
    
    <div class="cell cell--4" style="flex: 0 0 48%; max-width: 48%; box-sizing: border-box;">
      <center>
      <a href="/domain-research.html#theoretical-physics">
        <div class="card" style="height: 100%;">
          <div class="card_image">
          <img class="image" src="images/research-theory.png" style="width: 100%; height: auto;"/>
          </div>
              <div class="card_header">
              <h3><font color="lightcoral">AI + THEORETICAL PHYSICS</font></h3>
              <div class="card_content" style="font-size: 14px; color: black;">
              Leveraging AI to understand the theoretical underpinning of fundamental physics
            </div>
          </div>
        </div>
      </a>
      </center>
    </div>

    <div class="cell cell--4" style="flex: 0 0 48%; max-width: 48%; box-sizing: border-box;">
      <center>
      <a href="/domain-research.html#experimental-physics">
        <div class="card" style="height: 100%;">
          <div class="card_image">
          <img class="image" src="images/research-experiment.png" style="width: 100%; height: auto;"/>
          </div>
              <div class="card_header">
              <h3><font color="forestgreen">AI + EXPERIMENTAL PHYSICS</font></h3>
              <div class="card_content" style="font-size: 14px; color: black;">
              Enhancing the operations and analysis of flagship NSF experiments through AI
            </div>
          </div>
        </div>
      </a>
      </center>
    </div>
    
    <div class="cell cell--4" style="flex: 0 0 48%; max-width: 48%; box-sizing: border-box;">
      <center>
      <a href="/domain-research.html#astrophysics">
        <div class="card" style="height: 100%;">
          <div class="card_image">
          <img class="image" src="images/research-astro.png" style="width: 100%; height: auto;"/>
          </div>
              <div class="card_header">
              <h3><font color="darkgoldenrod">AI + ASTROPHYSICS</font></h3>
              <div class="card_content" style="font-size: 14px; color: black;">
              Using AI techniques to understand the universe on cosmological scales
            </div>
          </div>
        </div>
      </a>
      </center>
    </div>
    
  </div>
</div>

<!---
## [Cross-Cutting Themes](/cross-cutting-research.html)

<div class="grid-container">
  <div class="grid grid--p-2" style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">
    
<div class="cell cell--4" style="flex: 0 0 31%; max-width: 31%; box-sizing: border-box;">
<center>
<a href="/ai-research.html">
<div class="card" style="height: auto%; min-height: 150px; padding: 10px; text-align: center; background: #f5f5f5; border-radius: 8px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); font-size: 12px;">
    <div class="card_header" text-align: center; max-width: 100%; white-space: normal; padding: 5px;">
        <h4 style="font-size: 14px; line-height: 1.2; margin: 0; style="word-wrap: break-word; overflow-wrap: break-word;">REPRESENTATION/ MANIFOLD LEARNING</h4>
    </div>
    <div class="card_content" style="color: black;">
        Developing algorithms that categorize and label data and improve the features and knowledge extracted. Often deep physics insight can found in the structure of learned representations. Conversely, inductive biases from physics and understanding of a problem’s underlying manifold structure can inform the structure of AI architectures.
    </div>
</div>
</a>
</center>
</div>

</div>
</div>


[Representation/Manifold Learning](/cross-cutting-research.html#representation/manifold-learning){:.button.button--outline-primary.button--pill.button--md}
[Generative Models](/cross-cutting-research.html#generative-models){:.button.button--outline-primary.button--pill.button--md}
[Uncertainty Quantification/Robust AI](/cross-cutting-research.html#uncertainty-quantification/robust-ai){:.button.button--outline-primary.button--pill.button--md}
[Physics-Motivated Optimization](/cross-cutting-research.html#physics-motivated-optimization){:.button.button--outline-primary.button--pill.button--md}
[Reinforcement Learning](/cross-cutting-research.html#reinforcement-learning){:.button.button--outline-primary.button--pill.button--md}
--->

## Highlights

{% assign highlights = site.data.research-highlights | sort: "date-added" | reverse %}
{% for highlight in highlights %}

### {{highlight.title}}
*{{highlight.authors}}*

<details>
<summary>Public Slide</summary>
<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap">
<iframe src="{{highlight.public-embed-link}}" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>
[View and download public slide]({{highlight.public-link}})
</details>    

<details>
<summary>Technical Slide</summary>
<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap">
<iframe src="{{highlight.technical-embed-link}}" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>
[View and download technical slide]({{highlight.technical-link}})
</details>
{% endfor %}

