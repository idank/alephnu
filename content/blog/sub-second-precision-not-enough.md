Title: sub-second precision is not enough
Date: 2011-06-04 11:37:00
Category: Python
Tags: gsoc, mercurial

Turns out relying on st_mtime having sub-second precision is not reliable enough, as this small test demonstrates:

    :::bash
    $ touch a b ; stat a b | grep Modify
    Modify: 2011-07-28 15:36:19.505160175 +0300
    Modify: 2011-07-28 15:36:19.505160175 +0300

Opening one more process seems to delay enough to show a difference:

    :::bash
    $ touch a ; touch b ; stat a b | grep Modify
    Modify: 2011-07-28 15:37:50.082659665 +0300
    Modify: 2011-07-28 15:37:50.085158931 +0300

(test was done on a Debian Squeeze, ext4 fs).

Not to mention that Python's underlying type for floats is only good for around sixteen digits. Taking out the ten digits before the decimal point, that leaves about six for sub-seconds.

This test:

    :::python
    import os

    diffs = 0

    for i in range(10000):
        f = open('x', 'w+')
        f.close()

        one = os.stat('x').st_mtime

        f = open('x', 'w+')
        f.close()

        two = os.stat('x').st_mtime

        if one != two:
            diffs += 1

    print diffs, 'diffs out of 10000 iterations'

is giving me around ~30 per run, which is obviously not good enough.
