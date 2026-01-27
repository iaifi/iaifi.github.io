---
title: IAIFI AI+Physics Blog
---

<div style="display: flex; gap: 2rem;">

  <!-- Main Content -->
  <main style="flex: 1;">

{% assign sorted_posts = site.blog_posts | sort: 'date' | reverse %}
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

<!-- Sidebar -->
  <aside style="flex: 0 0 250px; position: sticky; top: 20px; height: fit-content;">
    <h3>By Month</h3>
    <ul style="list-style: none; padding: 0; margin-bottom: 2rem;">
      {% assign grouped_posts = sorted_posts | group_by_exp: 'post', 'post.date | date: "%B %Y"' %}
      {% for group in grouped_posts %}
        <li style="margin-bottom: 1rem;">
          <strong>{{ group.name }}</strong>
          <ul style="list-style: none; padding-left: 1rem; margin-top: 0.25rem; font-size: 0.7rem;">
            {% for post in group.items %}
              <li>– <a href="#post-{{ post.slug }}">{{ post.title }}</a></li>
            {% endfor %}
          </ul>
        </li>
      {% endfor %}
    </ul>

    <h3>By Tag</h3>
    <ul style="list-style: none; padding: 0;">
      {% assign all_tags = "" | split: "," %}
      {% for post in sorted_posts %}
        {% for tag in post.tags %}
          {% unless all_tags contains tag %}
            {% assign all_tags = all_tags | push: tag %}
          {% endunless %}
        {% endfor %}
      {% endfor %}
      
      {% assign sorted_tags = all_tags | sort %}
      {% for tag in sorted_tags %}
        <li style="margin-bottom: 0.5rem;">
          <strong>{{ tag }}</strong>
          <ul style="list-style: none; padding-left: 1rem; margin-top: 0.25rem; font-size: 0.7rem;">
            {% for post in sorted_posts %}
              {% if post.tags contains tag %}
                <li>– <a href="#post-{{ post.slug }}">{{ post.title }}</a></li>
              {% endif %}
            {% endfor %}
          </ul>
        </li>
      {% endfor %}
    </ul>
  </aside>
</div>
