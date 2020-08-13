###  The Institute for Artificial Intelligence and Fundamental Interactions Website

The IAIFI webpage source is hosted in GitHub and built using GitHub Pages. It is possible to use the [editor on GitHub](https://github.com/iaifi/iaifi.github.io/edit/master/README.md) to maintain and preview the content for your website in Markdown files; however, for most things it's easier to just build and run Jekyll locally.

Whenever a commit is made to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages that make up the IAIFI site, from the content in the Markdown files. Specifically, adding a file XXX.md will lead to the creation of XXX.html. The main webpage content can be found (and edited) in the following files:

- index.md creates the IAIFI homepage;
- about.md creates the *About* page;
- people.md creates the *People* page;
- research.md creates the *Research* page.

#### IAIFI News

Any Markdown file added to the *_posts* directory with the naming format *YYYY-MM-DD-NAME.md* will automatically trigger creation of a *News* entry assigned the date from the file name. These automatically appear in the *News* page. See existing posts for examples to get the header info and formatting correct. In the header, the *title* value will appear as the article's title on the *News* page. Text before the
 *excerpt_separator* string (see \_config.yml) is used as the article's preview lead. 

#### Markdown

Since Jekyll converts the simple Markdown files into the html that makes up the site, most IAIFI website updates only require editing Markdown files in your favorite editor. For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

#### Cheatsheet

Here are some useful commands for easy copy/pasting:

* Cloning this git repo over ssh:  `git clone git@github.com:iaifi/iaifi.github.io.git`
* Running Jekyll locally:  `bundle exec jekyll serve`
* Seeing Jekyll page locally:  <http://localhost:4000>
* Jekyll TeXt theme documentation:  <https://tianqi.name/jekyll-TeXt-theme/docs/en/quick-start>


