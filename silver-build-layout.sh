#!/usr/bin/env bash

DIR="$1"
PROJECT="%%MODULENAME%%"

if [ -z "$DIR" ] ; then
    echo "$(basename $0) DIR"
    echo "execute his OUTSIDE a repository / checkout"
    exit 2
fi

if [ ! -e "$DIR/bin/python" ] ; then
    silver init "$DIR"
fi

cd "$DIR"
MAIN_REPRO="git@github.com:hudora/%%PROJECTNAME%%.git"
# for R/O access it is something like
#MAIN_REPRO="git://github.com/ianb/zamboni.git"

if [ ! -e src ] ; then
    mkdir src
fi

if [ ! -e src/$PROJECT-src/.git ] ; then
    git clone $MAIN_REPRO src/$PROJECT-src
fi

if [ ! -L app.ini ] ; then
    rm app.ini
    ln -s src/$PROJECT-src/silver-app.ini app.ini
fi

if [ ! -e lib/python/silvercustomize.py ] ; then
    echo "import os, sys
OUR_ROOT = os.path.dirname(os.path.realpath(__file__))
sys.path = [os.path.realpath(os.path.join(OUR_ROOT, '../../src/$PROJECT-src'))] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
" > lib/python/silvercustomize.py
fi

if [ ! -e lib/python/$PROJECT.pth ] ; then
    echo "../../src/$PROJECT-src" > lib/python/$PROJECT.pth
fi

if [ ! -L bin/manage.py ] ; then
    if [ -e src/$PROJECT-src/manage.py ] ; then
        (cd bin ; ln -s ../src/$PROJECT-src/manage.py manage.py)
        chmod +x bin/manage.py
    fi
fi

if [ ! -L static/media ] ; then
    cd static
    ln -s ../src/$PROJECT-src/media media
    cd ..
fi

./bin/pip install -I -r src/$PROJECT-src/requirements.txt
