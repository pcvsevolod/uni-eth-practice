for i in $(ls ./python/ui/*.ui); do
    pyuic5 -o "$filename.py" $i
done
