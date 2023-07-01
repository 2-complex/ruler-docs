Ruler aggressively caches build results instead of discarding them.  It does this by copying files into `.ruler/cache/`  Each file in `.ruler/cache/` has filename equal to the hash of its contents.  You can check this by running `ruler hash` on a file in that directory. The hash will match the filename:

```sh
$ ruler hash .ruler/cache/NeGiY-9MRikJ6sIVnvxA1K14rL4EfLvREUClMXx2Lt8=
NeGiY-9MRikJ6sIVnvxA1K14rL4EfLvREUClMXx2Lt8=
```

For each rule in a build, Ruler compares the current hash of the target file to what the hash should be for the current sources.  If the file has the wrong hash, Ruler checks the cache for a file with the right hash.  If that file exists, then instead of rebuilding, Ruler moves the file into place.  To see this in action, let's make an example project.

In the `poetry` directory, we have `line1.txt` and `line2.txt` like so:

<h3>line1.txt</h3>

```
Roses are red
```

<h3>line2.txt</h3>

```
Violets are blue
```

<h3>build.rules</h3>

```
poem.txt
:
line1.txt
line2.txt
:
cat
line1.txt
line2.txt
>> poem.txt
:
```

Run `ruler build`, and Ruler will see that `poem.txt` does not exist and is therefore not up-to-date.  It therefore invokes the cat command to build `poem.txt`

```sh
poetry $ ruler build
build.rules
     Built: poem.txt
```

Look in the cache directory:

```sh
poetry $ ls .ruler/cache
poetry $
```

It's empty.  To save space, Ruler does not duplicate files into the cache as they build.  Instead it caches the old version of a file when it changes.  To see this, try editing one of the source files:

Edit `line2.txt` to this:

```
Violets are violet
```

Then rebuild:

```sh
poetry $ ruler build
build.rules
     Built: poem.txt
```

Check that the new poem built:

```
poetry $ cat poem.txt
Roses are red
Violets are violet
```

Now, look in the cache.  The previous version of `poem.txt` is there, renamed to its own hash:

```
poetry $ ls .ruler/cache/
_hbaVT8ppwStTHhiS8k1S45N9uTejttbD42fkJBQGRE=
poetry $ cat .ruler/cache/_hbaVT8ppwStTHhiS8k1S45N9uTejttbD42fkJBQGRE=
Roses are red
Violets are blue
```

Elsewhere in `.ruler/`, Ruler records the hash of `poem.txt` when it built the first time.  If we revert the source file and rebuild, Ruler will not rerun the build command for `poem.txt`.  Instead it will recover `poem.txt` from the cache.

Edit `line2.txt` to this:

```
Violets are blue
```

Then rebuild:

```
poetry $ ruler build
build.rules
 Recovered: poem.txt
```

