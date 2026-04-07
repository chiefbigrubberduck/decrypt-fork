# Decrypt
This program takes over the screen, prints flickering random characters and slowly makes the piped content (or input file) visible. This is a fork of jtwaelson's "decrypt"


## Examples

Do this for example on Linux:
```tree ~/Downloads | ./decrypt.py```

or
```jp2a my_favourite_cat.jpg --term-width | ./decrypt.py```

On Mac:
```ls ~/Downloads -R | ./decrypt.py```


## Remarks

Warning: keeps the entire input in memory and uses an O(n^2) algorithm. It is not efficient cpu/ram wise. Easy rewrite is possible but this is just for fun.
