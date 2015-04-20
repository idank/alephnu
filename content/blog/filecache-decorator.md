Title: the filecache decorator
Date: 2011-06-04 11:37:00
Tags: gsoc, mercurial, python

The past week or so I've been working on [a new decorator](http://markmail.org/thread/uublw3vjjrmqp5nr) that tracks files under the .hg/ directory for changes.

In short, you use it on a method and it turns it to a property with caching the result, like [propertycache](http://selenic.com/repo/hg/file/6d1d0b9c4ecc/mercurial/util.py#l164). But it also gives you the ability to invalidate the cached property, which triggers a stat(2) call that checks if the file behind the property changed since the last time it was read.

I used it on the dirstate, changelog, manifest, bookmark files, and the tags cache in localrepo so far. What it means in practice is that a call to repo.invalidate() is significantly cheaper where some of the above haven't changed since the last time they were read.

This is crucial so the command server's cached repository stays up-to-date where it changes by a different process than the server itself, i.e. via committing to it directly on the command line.

The main issue with this approach is that we fail if we end up missing changes. For example, a filesystem that doesn't have subsecond precision, will cause our cache to lie in the following situation:

<table>
<tr><td style="padding-right: 10px;">time<td>action</tr>
<tr><td>0<td>file x is modified</tr>
<tr><td>0.1<td>file x is read, inserted to the cache</tr>
<tr><td>0.2<td>file x is modified again, size remains the same</tr>
</table>

We end up with file x from 0 in our cache. Now suppose we invalidate the cache, this triggers a stat('x'), in which st_mtime == 0, which according to our cache is the most recent version of x, hence no need to reread. But it was in fact modified afterwards, but our filesystem doesn't have the necessary precision to help us spot it.

So we have to make sure our cache is reliable, and if we can't, we must fallback to reading the file every time the cache is invalidated.

Luckily Mercurial's approach to writing files helps us here. Essentially most of the important files under .hg/ are either: 1) atomically replaced, 2) appended.

If our filesystem is able to tell us a) if a file is replaced, or b) if it has subsecond precision, we're basically good to go. Because if we have (a) then (1) is covered, and (2) is covered because st_size changes on append. And if we have (b) it's obvious.

The current plan is to use the above test to make sure our cache is reliable, otherwise read the file every time. In the future we can improve this by also noting **when** the file was read.
