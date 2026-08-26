# TAGLINE

通过 scp 将文件复制到远程 Git 仓库

# TLDR

**将单个文件复制到远程**

```git scp [remote] [path/to/file]```

**将多个文件复制到远程**

```git scp [remote] [file1] [file2]```

**将文件复制到远程的指定分支**

```git scp [remote] [path/to/file] --branch [branch_name]```

# SYNOPSIS

**git** **scp** _remote_ _files_...

# DESCRIPTION

**git scp** 使用 scp 将文件复制到 Git 远程。它属于 **git-extras**，会利用 Git 配置中该远程的 URL 确定主机和路径，然后通过 scp 传输文件。要从远程复制文件，请改用 **git rscp**。

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

[git-rscp](/man/git-rscp)(1), [scp](/man/scp)(1), [git-extras](/man/git-extras)(1)
