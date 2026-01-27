---
title: IAIFI AI+Physics Blog
---

<style>
.math-callout {
  border-left: 4px solid #0b7285;
  background: rgba(11,114,133,.06);
  padding: .9rem 1rem;
  margin: 1rem 0 1.25rem;
  border-radius: 6px;
}
.math-callout .title { font-weight: 600; margin-bottom: .25rem; }
.math-callout .eq { text-align: center; margin: .5rem 0; }
.math-callout .caption { color: #555; font-size: .95em; margin-top: .25rem; }

h2 {
  font-size: 1.8rem;
  margin-top: 2rem;
}

h3 {
  font-size: 1.3rem;
  margin-top: 1.5rem;
}

h4 {
  font-size: 1.1rem;
  margin-top: 1rem;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

.highlight-box {
  background: rgba(32, 178, 170, 0.1);
  padding: 1rem;
  margin: 1rem 0;
  font-weight: bold;
}

</style>

<div style="display: flex; gap: 2rem;">

  <!-- Main Content -->
  <main style="flex: 1;">

{% assign sorted_posts = site.hidden_blog_review | sort: 'date' | reverse %}
{% for post in sorted_posts %}
  <div class="blog-post" id="post-{{ post.slug }}">
    <h2>{{ post.title }}</h2>
  <div style="flex: 1;"><em>By {{ post.author }} </em></div>
 <div style="display: flex; justify-content: space-between; gap: 20px;"> 
  <div style="font-size: x-small; color: gray; white-space: nowrap;">{{ post.tags | join: " | " }}</div> <div style="font-size: x-small; color: gray; white-space: nowrap;">👤 IAIFI | 📅 {{ post.date | date: "%B %d, %Y" }}</div>
</div>
    
    {{ post.content }}
<br>
<br>
  </div>
  
{% endfor %}
  </main>


