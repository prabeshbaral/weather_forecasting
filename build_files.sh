mkdir -p staticfiles_build
export STATIC_ROOT=mystaticfiles
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput