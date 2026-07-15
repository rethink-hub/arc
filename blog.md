---
layout: default
title: "Arc Blog — AI Tips, Guides & Android Productivity"
description: "Guides on AI productivity, Android multitasking, screen assistants, and how to get more done with AI on your phone. Practical tips from an indie developer."
---

<div class="blog-index">
    <header class="blog-index-header">
        <h1>Arc Blog</h1>
        <p>AI productivity guides, Android tips, and how to get more done with AI on your phone.</p>
    </header>

    <div class="blog-list">
        {% assign posts = site.posts | sort: 'date' | reverse %}
        {% for post in posts %}
        <article class="blog-card">
            <h2><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h2>
            <p class="blog-excerpt">{{ post.description | default: post.excerpt }}</p>
            <div class="blog-meta">
                <time>{{ post.date | date: "%b %d, %Y" }}</time>
            </div>
        </article>
        {% endfor %}
    </div>
</div>