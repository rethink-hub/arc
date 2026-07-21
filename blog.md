---
layout: default
title: "Arc Blog — AI Tips, Guides & Android Productivity"
description: "Guides on AI productivity, Android multitasking, screen assistants, and how to get more done with AI on your phone. Practical tips from an indie developer."
keywords: "Arc AI blog, Android productivity, AI screen assistant tips"
og_image: /assets/images/og-blog.png
---

<div class="blog-index">
    <header class="blog-index-header">
        <h1>Arc Blog</h1>
        <p>AI productivity guides, Android tips, and how to get more done with AI on your phone.</p>
    </header>

    <div class="blog-list">
        {% assign posts = site.posts | sort: 'date' | reverse %}
        {% for post in posts %}
        <a href="{{ post.url | relative_url }}" class="blog-card-link">
            <article class="blog-card">
                <h2>{{ post.title }}</h2>
                <p class="blog-excerpt">{{ post.description | default: post.excerpt }}</p>
                <div class="blog-meta">
                    <time>{{ post.date | date: "%b %d, %Y" }}</time>
                </div>
            </article>
        </a>
        {% endfor %}
    </div>
</div>