#! /bin/bash

if [ $# -ne 1 ];
    then echo "Requires 1 Argument (name of file in iaifi-news folder without .md)"
    exit
fi

echo ""
echo "Preparing to Juice...  $1"

echo ""
echo "Rebuilding Site..."
echo ""
bundle exec jekyll build


echo ""
echo "Inlining Styles..."
mkdir -p _site/iaifi-news/assets/css/
cp _site/assets/css/main.css _site/iaifi-news/assets/css/main.css
juice --preserve-important true --remove-style-tags false --web-resources-images false _site/iaifi-news/$1.html _site/iaifi-news/$1-juiced.html


echo ""
echo "Copying ..."
pbcopy < _site/iaifi-news/$1-juiced.html

echo ""
echo "HTML for $1 copied to clipboard!"
echo ""
