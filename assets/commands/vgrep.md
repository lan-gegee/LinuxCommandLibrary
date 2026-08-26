# TAGLINE

与编辑器集成的交互式 grep

# TLDR

**搜索模式**

```vgrep "[pattern]"```

**在目录中搜索**

```vgrep "[pattern]" [path]```

**交互式打开结果**

```vgrep -s "[pattern]"```

**显示特定结果**

```vgrep --show [index]```

**不使用 git ignore**

```vgrep --no-git "[pattern]"```

# SYNOPSIS

**vgrep** [_-s_] [_--show index_] [_options_] _pattern_ [_path_]

# PARAMETERS

**-s**
> 交互模式。

**--show** _INDEX_
> 按索引显示结果。

**--no-git**
> 不使用 gitignore。

**-n**
> 行号。

**-i**
> 不区分大小写。

# DESCRIPTION

**vgrep** 是一个 grep 结果分页器，它会为每个匹配项分配索引编号，让你可以按编号在编辑器中快速打开特定结果。它默认遵循 .gitignore 规则，并提供批处理和交互两种模式。

在交互模式（**-s**）下，可以浏览结果并直接打开。**--show** 标志无需重新运行搜索即可打开之前已建立索引的结果，非常适合在代码库中浏览匹配项。

# CAVEATS

Go 语言实现。需要配置编辑器。与 grep 不同。

# HISTORY

**vgrep** 的设计目标是快速搜索代码并按索引在编辑器中打开结果。

# INSTALL

```dnf: sudo dnf install vgrep```

```zypper: sudo zypper install vgrep```

```brew: brew install vgrep```

```nix: nix profile install nixpkgs#vgrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [rg](/man/rg)(1), [ag](/man/ag)(1)
