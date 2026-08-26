# TAGLINE

在网页浏览器中打开仓库

# TLDR

在浏览器中**打开当前仓库**，定位到当前提交/分支

```git browse```

**打开特定远程的仓库**

```git browse [upstream]```

**打开远程上的特定文件**

```git browse [upstream] [path/to/file]```

**跳转到文件中的特定行**

```git browse [upstream] [path/to/file] [42]```

**跳转到文件中的一个行范围**

```git browse [upstream] [path/to/file] [1] [42]```

# SYNOPSIS

**git** **browse** [_remote-name_] [_filename_] [_line1_] [_line2_]

# PARAMETERS

_REMOTE-NAME_
> 要浏览的远程；默认为当前分支跟踪的远程，或 **origin**。

_FILENAME_
> 要在远程上打开的文件路径（相对于仓库根目录）。

_LINE1_
> 要高亮的起始行号（需要 _filename_）。

_LINE2_
> 结束行号，用于高亮一个范围（需要 _line1_）。

# DESCRIPTION

**git browse** 是一个 git-extras 命令，它会检测当前仓库的远程 URL 并在默认网页浏览器中打开。它能识别 GitHub、GitLab 和 Bitbucket 的远程地址，并为每种平台构造正确的网页 URL 格式，包括在当前提交或分支下指向特定文件和行（或行范围）的深链接。

SSH 远程（**git@host:user/repo.git**）会被自动转换为 HTTPS。不指定文件名时，它只会打开当前提交/分支下的仓库主页。

# CAVEATS

仅识别 GitHub、GitLab 和 Bitbucket 的远程 URL 格式。需要系统中有可用的浏览器打开工具（**open**、**xdg-open** 或 **start**）。

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

[gh-browse](/man/gh-browse)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-browse)```

<!-- verified: 2026-07-17 -->
