## What is Ruler?

Ruler is a command-line tool not unlike Make or Ninja.  It helps deal with any project where some files are soure and some are target, and targets need to update when sources change.  It takes as input a `.rules` file describing:

- The dependence relationship between files
- For each target, a command to update

When invoked, Ruler reads in a .rules file, makes a determination which files need to update, and runs the commands for those files only.


### Anatomy of a .rules file

A .rules file contains newline-separated blocks called <b>rules</b>.  Each rule consists of three sections: <b>targets</b>, <b>sources</b> and <b>command</b>.  <b>Targets</b> and <b>sources</b>b> are newline-separated lists of file paths.  <b>Command</b> is a command-line invocation meant to update the targets using sources as input.  Each section is terminated by a single “:” alone on a line.  For example, a rule might look like this:

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

With the rulefile above, if hello.cpp is out of date, hello.exe rebuilds by this command:

```sh
c++ --std=c++17 hello.cpp -o hello.exe
```

A .rules file might consist of several rules, thereby encoding a whole dependence graph of files.
