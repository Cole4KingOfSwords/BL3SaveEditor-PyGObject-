if test -e "main.py"; then
 python3 main.py
else
 cd python || exit
 python3 main.py
fi