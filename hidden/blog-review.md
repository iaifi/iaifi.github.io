---
title: IAIFI AI+Physics Blog
---

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


