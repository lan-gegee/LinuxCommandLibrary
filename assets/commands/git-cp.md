# TAGLINE

复制文件并保留 git 历史

# TLDR

**复制文件并保留其历史**

```git cp [source_file] [destination_file]```

**将文件复制到其他目录并保留其历史**

```git cp [path/to/source] [path/to/destination]```

# SYNOPSIS

**git-cp** _current_filename_ _destination_filename_

# DESCRIPTION

**git cp** 是 git-extras 提供的命令，可在复制文件的同时保留其 Git 历史。这使得复制出来的文件也能进行合并冲突处理。

与先做普通文件系统复制再 git add 的方式（会产生一个没有历史的新文件）不同，git cp 利用 Git 通过内容相似度检测文件复制的能力。用 git log --follow --find-copies 查看复制文件的历史时，Git 可以追溯到原文件的提交。

在基于模板创建新文件，或将一个文件的功能拆分到多个文件、同时希望保留归属和历史时，这尤为有用。

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

[git-mv](/man/git-mv)(1), [git-extras](/man/git-extras)(1)
