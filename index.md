## What is Ruler?

Ruler is a command-line build tool like Make or Ninja.  It uses config files with the extension `.rules`  A `.rules` file describes:

- The dependence relationship between files
- For each target file, a command to update

When invoked like this:

```sh
ruler build
```

... Ruler computes which files need to update (and in what order), and runs the commands for those files only.

Software developers use tools like this to manage complex C/C++ projects.  Ruler can help manage any project with a dependence graph of files.  Example:

[What is a Dependence Graph](dependence-graph.md)


### Anatomy of a .rules file

A .rules file contains newline-separated blocks called <b>rules</b>.  Each rule consists of three sections: <b>targets</b>, <b>sources</b> and <b>command</b>.  <b>Targets</b> and <b>sources</b> are newline-separated lists of file paths.  <b>Command</b> is a command-line invocation meant to update the targets using sources as input.  Each section is terminated by a single “:” alone on a line.  For example, a rule might look like this:

```txt
hello.exe
:
hello.cpp
:
c++
--std=c++17
hello.cpp
-o hello.exe
:
```

With the rule above, if hello.cpp is out of date, hello.exe rebuilds by this command:

```sh
c++ --std=c++17 hello.cpp -o hello.exe
```

A .rules file might consist of several rules, thereby encoding the whole dependence graph.  A more in-depth discussion of the rules file syntax can be found here:

[Rules Files](rules-files.md)
