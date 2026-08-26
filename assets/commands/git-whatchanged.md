# TAGLINE

显示提交日志及文件级差异信息

# TLDR

**显示带差异信息的提交日志**

```git whatchanged```

**针对特定文件显示**

```git whatchanged [file]```

**显示统计信息**

```git whatchanged --stat```

**限制输出数量**

```git whatchanged -n [10]```

**显示指定日期之后的记录**

```git whatchanged --since="[2 weeks ago]"```

# SYNOPSIS

**git** **whatchanged** [_options_] [_paths_...]

# PARAMETERS

**-n** _num_
> 限制提交的数量。

**--stat**
> 显示 diffstat（差异统计）。

**--since** _date_
> 显示指定日期之后的提交。

**--until** _date_
> 显示指定日期之前的提交。

**-p**
> 显示补丁。

# DESCRIPTION

**git whatchanged** 显示每次提交所引入的差异的日志。它本质上等同于 `git log --raw --no-merges`，便于查看每次提交影响了哪些文件。

# CAVEATS

此命令已被弃用，并计划在未来某个 Git 版本中移除。请改用 `git log --raw`。当按路径限制输出时，需在路径前添加 `--` 以避免与分支名产生歧义，例如 `git whatchanged -- [file]`。

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

[git-log](/man/git-log)(1), [git-diff](/man/git-diff)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/git-whatchanged)```

<!-- verified: 2026-07-17 -->
