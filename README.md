# bloag

Database-less RSS blog generator from static HTML page.
Created to deploying RSS version of blog on [samedamci.me](https://samedamci.me/blog).
Very basic and primitive version currently only working with this site,
because it reads specific HTML structure to generate posts.
In the future this tool will can also generate website and
work as static site generator.

## Usage
*Works only with samedamci.me blog...*

Remote:
```
$ bloag -i https://samedamci.me/blog/index.html -o blog/rss.xml
```
Local:
```
$ bloag -i blog/index.html -o blog/rss.xml
```
