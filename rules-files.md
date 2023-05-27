## Rules Files

Dependencies are encoded in a .rules file. A .rules file contains newline-separated blocks called **rules**. Each rule has three sections: targets, sources and command. Targets and sources are newline-separated lists of file paths. Command is a command-line invocation that presumably takes the sources as input and updates the targets. Each section ends with `:` alone on a line. For example, a .rules might contain this single rule:

```txt
build/game
:
src/game.h
src/game.cpp
:
c++
src/game.cpp
--std=c++17
-o build/game
:
```

That rule declares that the executable `build/game` depends on two source files `src/game.h` and `src/game.cpp` and builds by this line:

```sh
c++ src/game.cpp --std=c++17 -o build/game
```

Ruler uses unconventional syntax for the command. One invocation can span multiple lines without backslashes. To get a multi-line invocation, separate by `;` alone on a line.

By using ruler's build subcommand with the option `--rules` you can specify a path to a rules file like so:

```
ruler build --rules=game.rules
```

With no rules file specified, ruler will look in the current working directory for `build.rules`

Ruler build with the `.rules` file above will check whether `game` is up to do date.  If it is not up to date, ruler looks for a way to recover it from a cache.  If there is no way to recover the file from a cache, it runs the command.
