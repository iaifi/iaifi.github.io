#! /bin/bash

# Copying from Loom Jekyll theme

BLUE='\033[0;36m'
NC='\033[0m'
echo -e "\n${BLUE}building site...${NC}\n"
bundle exec jekyll build
echo -e "\n${BLUE}inlining styles...${NC}"
mkdir -p _site/digest/assets/css/
cp _site/assets/css/main.css _site/digest/assets/css/main.css
juice --preserve-important true --remove-style-tags false --web-resources-images false _site/digest/2024-04-01.html _site/digest/2024-04-01-juiced.html
pbcopy < _site/digest/2024-04-01-juiced.html
echo -e "\n${BLUE}html copied to clipboard 🌿${NC}\n"
