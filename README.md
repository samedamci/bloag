# bloag

Database-less RSS and static HTML blog generator from Markdown files.
Created to deploying blog on [samedamci.me](https://samedamci.me/blog).
Very basic and primitive version currently only working with this site.
In future I will create scheme to generate full blog from scratch but... not now.

## Usage
*Works only with samedamci.me blog...*
```
$ bloag -i <post_id> -H blog/index.html -R blog/rss.xml -M input.md
```

## Installation
+ Clone repo.
```
$ git clone https://git.samedamci.me/samedamci/bloag && cd bloag
```
+ Build and install package.
```
$ pip3 install --user .
```
