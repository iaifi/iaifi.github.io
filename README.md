###  The Institute for Artificial Intelligence and Fundamental Interactions Website

The IAIFI webpage source is hosted in GitHub and built using GitHub Pages. It is possible to use the [editor on GitHub](https://github.com/iaifi/iaifi.github.io/edit/master/README.md) to maintain and preview the content for your website in Markdown files; however, for most things it's easier to just build and run Jekyll locally.

Whenever a commit is made to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages that make up the IAIFI site, from the content in the Markdown files. Specifically, adding a file XXX.md will lead to the creation of XXX.html. The main webpage content can be found (and edited) in the following files:

- index.md creates the IAIFI homepage;
- about.md creates the *About* Overview page;
- activities.md creates the *About* Synergies page;
- iaifi-news.md creates the *About* News page;
- people.md creates the *People* page;
- research.md creates the *Research* page;
- fellows.md creates the *Fellows* page.

#### IAIFI News

Currently, we are placing these under \_includes/news, since then it is trivial to inline include their Markdown content in other Markdown files. This is not optimal, but since we don't really know yet what we're going to do with the news, we decided to do this because it's simple. 

#### Markdown

Since Jekyll converts the simple Markdown files into the html that makes up the site, most IAIFI website updates only require editing Markdown files in your favorite editor. For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

#### Cheatsheet

Here are some useful commands for easy copy/pasting:

* Cloning this git repo over ssh:  `git clone git@github.com:iaifi/iaifi.github.io.git`
* Running Jekyll locally:  `bundle exec jekyll serve`
* Seeing Jekyll page locally:  <http://localhost:4000>
* Jekyll TeXt theme documentation:  <https://tianqi.name/jekyll-TeXt-theme/docs/en/quick-start>
