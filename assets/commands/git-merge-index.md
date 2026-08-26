# TAGLINE

为未合并的文件运行合并程序

# TLDR

**对未合并的文件运行合并程序**

```git merge-index [merge-program] -a```

**合并特定文件**

```git merge-index [merge-program] [file]```

# SYNOPSIS

**git** **merge-index** [_options_] _merge-program_ _files_...

# PARAMETERS

**-a**
> 对所有未合并的条目运行。

**-o**
> 出错时不停止。

**-q**
> 安静模式。

# DESCRIPTION

**git merge-index** 为每个需要合并的文件运行指定的合并程序。这个底层（plumbing）命令是 Git 内部合并机制的一部分，在三方合并操作期间被调用，用于处理索引中未合并的文件。

该命令会把文件信息（包括 base、ours 和 theirs 版本及其对象 ID）传给指定的合并程序。大多数用户从不需要直接调用它，因为 `git merge` 会自动处理。它主要供自定义合并工作流以及了解 Git 内部原理使用。

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

[git-merge](/man/git-merge)(1), [git-mergetool](/man/git-mergetool)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-merge-index)```

<!-- verified: 2026-07-17 -->
