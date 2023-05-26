## What is Ruler?

Ruler is a command-line build tool like Make or Ninja.  Software developerms often use tools like these for complex C/C++ project, but Ruler can also help manage any project that has a dependence graph of files.  An example is discussed here:

[What is a Dependence Graph](dependence-graph.md)

Ruler uses config files with the extension `.rules`  A `.rules` describes:

- The relationship of dependence between files
- For each target file, a command to update

When invoked like this:

```sh
ruler build
```

... Ruler determines which files need to update (and in what order), and runs the commands for those files only.


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

A .rules file might consist of several rules, thereby encoding the whole dependence graph.
