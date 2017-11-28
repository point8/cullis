# Cullis

> **cul·lis** (kŭl′ĭs)    
> A gutter or groove in a roof

Compose a PowerPoint presentation from a single PDF file or several image files.


## Documentation

* :bug: **For bug reports and feature requests use the [issue tracker](https://git.point-8.de/dev/friday-tasks/issues)**


## Quickstart

You can either convert a single PDF file containing several pages or a bunch of image files.

### PDF file

```
cullis convert /path/to/file.pdf
```

### Image files

```
cullis convert /path/to/image/dir/
```

### Optional arguments

```
$ cullis convert --help
Usage: cullis convert [OPTIONS] SOURCE

Options:
  -v, --verbose   Show debug output
  -o, --out TEXT  Name of output file (w/o file extension)
  --help          Show this message and exit.
```

## Setup

* Install ImageMagick. It's important to not install the newest version, but Version 6, as the newest version doesn't support all necessary bindings yet.

```
brew install imagemagick@6
```

* Set ENV

```
export MAGICK_HOME=/usr/local/opt/imagemagick@6/
```

* Install **cullis** with `pip install -U .`
