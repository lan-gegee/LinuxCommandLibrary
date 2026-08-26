# TAGLINE

安排文件在下一次提交时加入仓库

# TLDR

**添加指定文件**

```hg add [file]```

**添加所有新文件**

```hg add```

**按模式添加文件**

```hg add '*.py'```

**添加目录中的文件**

```hg add [path/to/directory]```

**试运行预览效果**

```hg add -n [file]```

# SYNOPSIS

**hg** **add** [_options_] [_files_...]

# PARAMETERS

**-n**, **--dry-run**
> 显示将要添加的内容，但不修改实际状态。

**-I**, **--include** _PATTERN_
> 只添加匹配模式的文件（可重复使用）。

**-X**, **--exclude** _PATTERN_
> 跳过匹配模式的文件（可重复使用）。

**-S**, **--subrepos**
> 递归处理子仓库。

# DESCRIPTION

**hg add** 安排文件在下一次提交时加入仓库。不带参数时，它会添加工作目录中的所有新文件。可使用 .hgignore 文件将某些文件排除在版本控制之外。已添加的文件在提交前会在 **hg status** 中显示 'A' 状态。

# INSTALL

```apt: sudo apt install mercurial```

```dnf: sudo dnf install mercurial```

```pacman: sudo pacman -S mercurial```

```apk: sudo apk add mercurial```

```zypper: sudo zypper install mercurial```

```brew: brew install mercurial```

```nix: nix profile install nixpkgs#mercurial```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hg](/man/hg)(1), [hg-commit](/man/hg-commit)(1), [hg-status](/man/hg-status)(1)
