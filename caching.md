One feature that sets Ruler apart from other tools like it is that it aggressively caches build results instead of discarding them.  It does this by copying files into a directory, which by default is located in `.ruler/cache`.  Each file in `.ruler/cache` has filename equal to to the hash of its contents.  You can check this by running the command `ruler hash` on a file in that directory, and noting that the hash matches the filename:

```sh
$ ruler hash .ruler/cache/NeGiY-9MRikJ6sIVnvxA1K14rL4EfLvREUClMXx2Lt8=
NeGiY-9MRikJ6sIVnvxA1K14rL4EfLvREUClMXx2Lt8=
```

When handling a build rule, Ruler uses the current state of the source files and target files to see if the targets need to update.  It makes the determination based on the hash of 