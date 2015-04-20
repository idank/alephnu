Title: upstart script section exits prematurely
Date: 2012-10-13 11:37:00
Tags: bash

I wrote my first Upstart script today, and like anyone wanting
to get the job done quickly I haven't read the entire [cookbook](http://upstart.ubuntu.com/cookbook).

So after spending a couple of minutes trying to figure out
why my two line script is only executing the first command, I returned to the
cookbook and searched for `sh -e` and lo and behold:

> Remember that Upstart runs every script section using /bin/sh -e. This means
> that if any simple command fails, the shell will exit.

As a default that probably makes sense for most scripts but it certainly
surprised me. It should at least be mentioned where they introduce the
[script section](http://upstart.ubuntu.com/cookbook/#script) in the cookbook.

So if your script contains commands that might fail and that's fine
by you then you can `|| true` them so the shell won't exit.
