#!/bin/sh
py=python
py3=python3
if $py --version | grep -q 'Python 3.'; then
    :
elif $py3 --version | grep -q 'Python 3.'; then
    py=$py3
else
    echo 'Install python3!'
    exit
fi

py_init='./one.py'
echo '#!'`which $py` > $py_init
cat boh/config.py >> $py_init
chmod +x $py_init
$py_init
echo 'Da end'
