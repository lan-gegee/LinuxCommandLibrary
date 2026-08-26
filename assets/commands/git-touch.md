# TAGLINE

创建文件并暂存以待提交

# TLDR

**创建并暂存文件**

```git touch [file.txt]```

**创建多个文件**

```git touch [file1.txt] [file2.txt]```

# SYNOPSIS

**git touch** _files_

# PARAMETERS

_FILES_
> 要创建并暂存的文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git touch** 创建文件并将其暂存以待提交。它把 Unix 的 `touch` 命令与 `git add` 结合在一起，创建出的空文件会被立即纳入跟踪。

该命令适合创建将要提交的占位文件。它省去了"先创建文件再添加跟踪"的单独步骤。

# CAVEATS

属于 git-extras 软件包。创建的是空文件。文件仍需提交。

# HISTORY

git touch 是 **git-extras** 的一部分，为方便起见将文件创建与暂存合二为一。

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

[touch](/man/touch)(1), [git-add](/man/git-add)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-touch)```

<!-- verified: 2026-07-17 -->
