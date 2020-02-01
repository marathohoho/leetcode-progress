temp="added"+$(ls -td -- */ | head -n 1)
git add . && git commit -m $temp && git push
