# Dockerfile for local Jekyll preview of Arc website
FROM ruby:3.2-slim

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    libffi-dev \
    zlib1g-dev \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /srv/jekyll

# Copy Gemfile and install gems first for better caching
COPY Gemfile ./
RUN bundle config set --local path 'vendor/bundle' && \
    bundle install

# Expose Jekyll default port
EXPOSE 4000

# Serve the site, binding to all interfaces so it can be opened in a browser
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--port", "4000", "--livereload", "--force_polling"]
