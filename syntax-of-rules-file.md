The syntax for a `.rules` file is rigid and uncomplicated.  Here is an example `.rules` file:

```txt
math.o
:
math.h
math.cpp
:
c++ -c
math.cpp
-o math.o
:

physics.o
:
math.h
physics.h
physics.cpp
:
c++ -c
physics.cpp
-o physics.o
:

game
:
math.h
math.o
physics.h
physics.o
game.cpp
:
c++
game.cpp
-o game
:

```

Each <b>rule</b> is a block of non-empty lines with three sections <b>targets</b>, <b>sources</b> and <b>command</b>.  Each section ends with a single ":" on a line, and each rule is separated from the next by an empty line.  An empty line anywhere else is an error, and produces an error message for example:

```txt
math.o
:
math.h
math.cpp
:
c++ -c
math.cpp

-o math.o
:
```

```sh
Unexpected empty line 8
```

Similarly, an extra line shows up as an error:

```txt
math.o
:
math.h
math.cpp
:
c++ -c
math.cpp
-o math.o
:


physics.o
:
math.h
physics.h
physics.cpp
:
c++ -c
physics.cpp
-o physics.o
:
```

```sh
Unexpected emtpy line 11
```

There are no escape-characters in the paths, and Ruler interprets a forward slash ("/") as a path separator.  This means that paths with a newline character or a "/" in the name of a file or directory do not work.

The command is parsed as separate invocations separated by a single.  This makes it possible to put   If more than whitespace-separated arguments

