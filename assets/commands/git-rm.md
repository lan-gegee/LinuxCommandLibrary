# TAGLINE

从工作树和索引中删除文件

# TLDR

**取消跟踪文件**

```git rm [file.txt]```

**删除目录**

```git rm -r [directory/]```

**仅从索引中移除**

```git rm --cached [file.txt]```

**强制删除**

```git rm -f [file.txt]```

**试运行**

```git rm -n [file.txt]```

# SYNOPSIS

**git rm** [_options_] _files_

# PARAMETERS

_FILES_
> 要删除的文件。

**--cached**
> 仅从索引中移除，保留文件本身。

**-r**
> 递归删除。

**-f**, **--force**
> 强制删除。

**-n**, **--dry-run**
> 显示将要删除的内容。

**--ignore-unmatch**
> 即使没有匹配项也以成功状态退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git rm** 从工作树和索引中删除文件，并将该删除暂存以待下次提交。`--cached` 选项只让文件脱离版本跟踪而保留在磁盘上，适用于本应写进 `.gitignore` 的文件。

不带 `--cached` 时，文件会同时从工作树和索引中被删除。

# CAVEATS

不带 --cached 时会从磁盘删除文件。删除操作需要提交。用 --cached 可在不删除文件的情况下取消跟踪。

# HISTORY

git rm 是 **Git** 中用于从版本控制中删除文件的核心命令，与 git add 互为补充。

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

[git-add](/man/git-add)(1), [git-mv](/man/git-mv)(1), [rm](/man/rm)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-rm)```

<!-- verified: 2026-07-17 -->
