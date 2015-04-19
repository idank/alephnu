Title: refresh browser when html or css changes
Date: 2011-12-17 11:32:00
tags: bash, html, vim

If you work regularly with web pages you know how tedious it is to go back and forth between your editor and browser and hitting refresh to see the changes.


This shell script finds the browser window of a given HTML file and refreshes it:

    #!/bin/sh

    windowtitle=$(sed -ne "s/<title>\(.*\)<\/title>/\1/p" "$1")

    if [ $? != 0 ]; then
        echo "couldn't find <title> in file" $1 1>&2
        exit 1
    fi

    # get rid of leading/trailing whitespace
    windowtitle=$(echo -n $windowtitle)

    if [ -z "$windowtitle" ]; then
        echo "couldn't find <title> in file" $1 1>&2
        exit 1
    fi

    # oldid=$(xdotool getwindowfocus)
    id=$(xdotool search -title "$windowtitle")

    if [ $? != 0 ]; then
        echo 'window not found' 1>&2
        exit 1
    fi

    xdotool windowactivate $id
    xdotool key F5 $id
    # xdotool windowactivate $oldid


The first half of the script is basically just getting the &lt;title&gt; of the file so we can find the correct window to refresh. The rest is giving it focus and hitting F5.

The two commented lines are for those who have multiple monitors with the browser and editor visible at the same time. Then it makes sense to give focus back to the original window. Uncomment them if you'd like that.

Both of these snippets require **xdotool**, which can be found in any distro package manager (in Ubuntu/Debian `sudo apt-get install xdotool`).

This can be integrated into vim like this:

    autocmd FileType html noremap <buffer><silent> K :update <Bar>
        \ execute 'silent !~/refresh.sh "%"'<CR><Esc>

Putting this in your .vimrc and hitting <kbd>K</kbd> will save the current file and run the script, assuming it's at `~/refresh.sh`.
