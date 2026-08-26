# TAGLINE

列出索引和工作区中的文件

# TLDR

**列出已跟踪的文件**

```git ls-files```

**列出未跟踪的文件**

```git ls-files --others```

**列出被忽略的文件**

```git ls-files --ignored --exclude-standard```

**列出已修改的文件**

```git ls-files --modified```

**列出已删除的文件**

```git ls-files --deleted```

# SYNOPSIS

**git ls-files** [_options_] [_files_]

# PARAMETERS

**--cached**, **-c**
> 显示已暂存的文件（默认）。

**--modified**, **-m**
> 显示已修改的文件。

**--deleted**, **-d**
> 显示已删除的文件。

**--others**, **-o**
> 显示未跟踪的文件。

**--ignored**
> 显示被忽略的文件。

**--exclude-standard**
> 使用标准排除规则。

**--stage**, **-s**
> 显示暂存信息。

**-x** _pattern_, **--exclude** _pattern_
> 跳过匹配模式的文件。

**-z**
> 用 NUL 而非换行符终止条目，便于安全地在脚本中使用。

**--full-name**
> 显示相对于仓库根目录而非当前目录的路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git ls-files** 列出索引和工作区中的文件。它可以显示已跟踪、未跟踪、被忽略、已修改和已删除的文件，因此在脚本编写和自动化中很有价值。

该命令提供了对 Git 文件跟踪状态的底层访问。各种标志控制要显示哪些类别的文件。它常用于脚本中以枚举满足特定条件的文件，例如查找所有未跟踪的文件，或列出 `.gitignore` 忽略的所有内容。

# CAVEATS

显示的是索引状态，而非提交。输出格式随选项而异。适合脚本使用。

# HISTORY

git ls-files 是 **Git** 用于检查索引的底层（plumbing）核心命令，既可直接使用，也被其他 git 命令调用。

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

[git-status](/man/git-status)(1), [git-ls-tree](/man/git-ls-tree)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-ls-files)```

<!-- verified: 2026-07-17 -->
