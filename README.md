# MkDocs Git Info Plugin

A (very) basic MkDocs plugin that pulls out Git information for each of the markdown files that are passed into a Jinja template so you can show meta-info such as last-update timestamps, contributors, commits etc.

All variables are passed to the Jinja template inside of the context object called `git-info`. This object includes:

```
last_updated_unix
last_updated_short
last_updated_long
last_updated_iso
number_commits
number_authors
```

## Usage:

Inside your Jinja template, reference the above variables:

```
{% if git_info %}
<span>Last update: {{ git_info['last_updated_long'] }}</span>
{% endif %}
```

Which becomes:

```
<span>Last update: 2020-01-20 15:00:06</span>
```

And renders as:

```
Last update: 2020-01-20 15:00:06
```

## Installation

`pip install mkdocs-git-info-plugin`
 
```
plugins:
  - search
  - git-info
```

> Make sure to re-enable search, as it is enabled by default but will be lost when specific plugins are set.

## Drawbacks

MkDocs render times go up quite a bit as the plugin currently performs 3 separate `git` commands for every single markdown file (to get dates, authors, and number of commits). Basically scales linearilly in number of pages and number of `git` commands required per page. This would ideally be rolled into a single `git log` call, which is then parsed reliably by Python.