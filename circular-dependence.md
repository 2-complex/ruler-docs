It is possible to describe a cyclic dependence graph with valid `.rules` syntax.  In this case, Ruler immediately errors on any build or clean.  Here are some examples:

A `build.rules` with a rule making a file depend on itself as a target:

```
a
:
a
:
touch a
:
```

This `.rules` file produces this error:

```
$ ruler build
build.rules
Dependence search failed: Self-dependent target: a
```

A `build.rules` with two rules depending on each other:

```
a
:
b
:
touch a
:

b
:
a
:
touch b
:
```

Produces this error:

```
Dependence search failed: Circular dependence:
a
b
```

When performing a build or clean, Ruler searches the rules file for depdencies.  If the build command specifies a target, Ruler limits its search to dependencies of that target.  This means that even if there is a circular dependence in the `.rules` file somewhere, the build might still succeed:


```
a
:
b
:
touch a
:

b
:
a
:
touch b
:

c
:
:
echo "content" >> c
:
```

```
 $ ruler build c
build.rules
     Built: c
```
