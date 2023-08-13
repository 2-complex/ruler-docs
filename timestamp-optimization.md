Consider a dependence graph with one source `A` and one target `B`.

<img src = "ab.svg">

The target needs to update when the source changes.  A very sensible way to do this is to compare modified dates.  If `A` was modified after `B`, that means `B` is out of date, so it needs to update.  This approach makes sense intuitively, and it's efficient.  All the build needs to do is compare a few numbers; it doesn't have to read the whole file.

Ruler, however, does not work this way.  Ruler takes into account the files' contents.  To determine if `B` needs to update, Ruler reads in `A`, computes a hash, checks its records for what `B` should be based on that hash.  If it does not have a record, or if `B` does not match the record, then it updates `B`.

That is very inefficient compared to using modified dates, but Ruler has a trick up its sleeve.  In addition to its mappig of source hashes to target hashes, it also stores a mapping of modified date to hash for any file it encounters.  When determining the hash of `A`, for example, it first looks at the modified date of `A` to see if it matches what it has on file, and if it does, Ruler skips computing the hash, it just assumes the hash is the same as it was.

This means that the first time you build a large project, Ruler will have to read in each file to compute its hash, but on incremental builds it does not have to.
