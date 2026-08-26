# TAGLINE

通过 rsync 从远程仓库的工作目录复制文件

# TLDR

**从远程复制指定文件**到当前目录

```git rscp [remote] [file]```

**复制远程的目录**

```git rscp [remote] [directory]```

# SYNOPSIS

**git** **rscp** _remote_ _files_...

# DESCRIPTION

**git rscp** 是 git-extras 的 `git scp` 的反向操作：它使用 rsync 将给定的文件或目录从远程的工作目录复制到当前工作目录。它与 `git-scp` 是同一个脚本，只是以不同的名字调用，这会让它切换到"拉取"模式，而不是 scp 默认的"推送并暂存"模式。

目标路径由所指定 remote 配置的 URL 推导而来，因此该 remote 必须已存在于 `git remote` 中。

# CAVEATS

属于 git-extras 软件包；需要安装 `rsync`，SSH 远程还需要 `ssh`。与 `git scp` 不同，这样复制来的文件不会被自动暂存。

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

[git-scp](/man/git-scp)(1), [rsync](/man/rsync)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-scp)```

<!-- verified: 2026-07-17 -->
