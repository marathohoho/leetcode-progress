temp="Added"$(ls -td -- */ | head -n 1 | cut -d'/' -f1)

git add . && git commit -m $temp && git push



