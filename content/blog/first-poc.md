Title: first poc of the command server
Date: 2011-06-04 11:37:00
Tags: gsoc, mercurial

Yesterday I sent out an [early version](http://article.gmane.org/gmane.comp.version-control.mercurial.devel/42131) of the command server to the mailing list ([patch queue][]), which included:

- new option --cmdserver to `hg serve`.
- a small Python wrapper, hglib, around the server that can connect to a repository and run commands. Also included is a sample of how real hg commands might look like in the lib, see status().
- a shell that uses hglib and runs commands against a given repository.
- last 2 patches are an attempt to integrate the command server to the test suite.

In the next few days I'll be working on:

- Support for interactive commands.
- Making more tests pass the testsuite using the command server.
- Finalizing the command wire protocol and writing it down in a wiki page.
- Feedback from other devs on the PoC.

[patch queue]: https://bitbucket.org/idank/hg-cmdserver
