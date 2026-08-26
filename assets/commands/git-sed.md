# TAGLINE

在已跟踪的文件中查找并替换

# TLDR

**在已跟踪文件中查找并替换**

```git sed "[old]" "[new]"```

**带 sed 标志替换**（例如忽略大小写）

```git sed -f [i] "[old]" "[new]"```

**限定某个路径**

```git sed "[old]" "[new]" -- [path/]```

**替换后提交**结果

```git sed -c "[old]" "[new]"```

# SYNOPSIS

**git** **sed** [_-c_] [_-f_ _flags_] _search_ _replacement_ [_flags_] [_--_ _pathspec_]

# PARAMETERS

_SEARCH_
> 要查找的模式。

_REPLACEMENT_
> 要替换进去的文本。

**-f**, **--flags** _flags_
> 要附加的 sed 替换标志（如 `g`、`i`）；也可以作为末尾的位置参数给出。

**-c**, **--commit**
> 之后提交该改动；如果工作树原本不干净则会失败。

**--** _pathspec_
> 将替换范围限定在匹配的文件/路径。

# DESCRIPTION

**git sed** 先运行 `git grep` 找出匹配的文件，再通过管道交给 `sed -i` 把 `search` 替换为 `replacement`，改动范围仅限于 Git 跟踪的文件，因此绝不会触碰未跟踪或被忽略的文件。它属于 git-extras，为全仓库范围的重命名省去了单独编写 `grep | xargs sed` 管道的麻烦。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sed](/man/sed)(1), [git-grep](/man/git-grep)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-sed)```

<!-- verified: 2026-07-17 -->
