Consider a dependence graph with one source `A` and one target `B`.  The target needs to update when the source changes.  A very sensible way to do this is to compare modified dates.  If `A` was modified after `B`, that means `B` is out of date, so it needs to update.  Not only does this approach make sense intuitively, it's also very efficient.  All the build needs to do is compare a few numbers; it doesn't have to read the whole file.

Ruler, however, does not work this way.  Ruler takes into account the files' contents.  So, to determine if `B` needs to update, Ruler reads in `A` and looks to see if it has a record of what `B` should be based on that hash.  If it does not have a record, or if it does have a record, and `B` does not match, then it updates `B`.

That is very inefficient compared to using modified dates, but Ruler has a trick up its sleeve.  It also stores in persistent memory a mapping of modified date to hash for any file it encounters in the project.  So, when it is determining the hash of `A`, for example, it first looks at the modified date of `A` to see if it matches what it has on file, and if it does, Ruler doesn't bother computing the hash, it just assumes the hash is the same.

This means that the first time you build a large project, Ruler will have to read in each file to compute its hash, but on incremental builds it does not have to.
