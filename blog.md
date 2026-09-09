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

<!-- Cross-platform section -->
<div class="section-header" style="margin-top: var(--xl);">
    <span class="section-tag">Platforms</span>
    <h2>Arc is expanding.</h2>
    <p>Available on Android and Mac now. iOS and Windows coming soon.</p>
</div>
<div class="platform-links" style="justify-content: center; margin-bottom: var(--xl);">
    <a href="{{ '/android/' | relative_url }}">Arc for Android</a>
    <a href="{{ '/ios/' | relative_url }}">Arc for iOS</a>
    <a href="{{ '/macos/' | relative_url }}">Arc for Mac</a>
    <a href="{{ '/windows/' | relative_url }}">Arc for Windows</a>
</div>

<!-- Feature links -->
<div class="section-header">
    <span class="section-tag">Features</span>
    <h2>Explore what Arc can do.</h2>
</div>
<div class="platform-links" style="justify-content: center; margin-bottom: var(--xl);">
    <a href="{{ '/ai-summary-reader/' | relative_url }}">AI Summary &amp; Reader</a>
    <a href="{{ '/ai-writer/' | relative_url }}">AI Writer</a>
    <a href="{{ '/ai-workflow-automation/' | relative_url }}">Workflow Automation</a>
</div>