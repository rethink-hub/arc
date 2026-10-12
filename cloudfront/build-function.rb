# Usage: ruby cloudfront/build-function.rb > /tmp/rewrite.js
# Inlines _data/redirects.yml into cloudfront/rewrite.js.
require "yaml"
require "json"
root = File.expand_path("..", __dir__)
map = YAML.load_file(File.join(root, "_data/redirects.yml")) || {}
map.each do |from, to|
  abort "redirect keys and targets must be site paths: #{from} -> #{to}" unless from.start_with?("/") && to.start_with?("/")
end
src = File.read(File.join(root, "cloudfront/rewrite.js")).sub("__REDIRECTS__", JSON.generate(map))
abort "function exceeds CloudFront's 10KB limit" if src.bytesize > 10_240
puts src
