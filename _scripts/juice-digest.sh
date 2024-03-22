#! /bin/bash

# Copying from Loom Jekyll theme

BLUE='\033[0;36m'
NC='\033[0m'
echo -e "\n${BLUE}building site...${NC}\n"
bundle exec jekyll build
echo -e "\n${BLUE}inlining styles...${NC}"
juice --preserve-important true --remove-style-tags false --web-resources-images false _site/hidden-digest-testing.html _site/hidden-digest-testing-juiced.html
pbcopy < _site/hidden-digest-testing-juiced.html
echo -e "\n${BLUE}html copied to clipboard 🌿${NC}\n"
