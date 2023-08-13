## What is a Dependence Graph?

A <b>dependence graph</b> is a diagram of files linked by arrows.  Each arrow indicates a dependence between files, in other words: the file at the head of the arrow (called a <b>target</b>) must update whenever the file at the tail of the arrow (called a <b>source</b>) changes.  Such a diagram comes in handy in many situations.  Here is an example.

Suppose you are writing a scientific journal article.  The finished article is a PDF, but that PDF is made by assembling text and visuals stored in other files.  There are figures made in a drawing program, a chart showing experimental data, and a LaTeX file describing the final product.

The directory for this project contains:

- <b>fig1.eps</b> and <b>fig2.eps</b> Technical illustrations made by an artist
- <b>data.csv</b> A spreadsheet containing raw experimental data
- <b>make_chart.py</b> A script that reads `data.csv` and uses a python library to construct <b>chart.png</b> run by typing:

```sh
python make_chart.py
```

- <b>article.tex</b> A LaTeX document containing the article's text with formatting tags and references to the figures and to the chart all describing the final product
- <b>article.pdf</b> which we generate by typing:

```sh
pdflatex article.tex
```

This is the dependence graph:

<img src = "journal-article.svg">

If just one source file changes, following the arrows through the diagram reveals what must update.  Suppose we add more experimental data to `data.csv`, this should prompt a change to `chart.png`, and that change must incorporate into `article.pdf`.  So, we need to run:

```sh
python make_chart.py
pdflatex article.tex
```

On the other hand, if our artist makes adjustments to `fig1.eps`, then we must incorporate the new `fig1.eps` into the final pdf, but there's no need to rebuild the chart.  We only must to do this:

```sh
pdflatex article.tex
```

Throughout the Ruler documentation, we use diagrams like this one to quickly explain dependence scenarios and how Ruler handles them.
