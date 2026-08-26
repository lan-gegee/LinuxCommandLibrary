# TAGLINE

根据提交历史恢复文件时间戳

# TLDR

**恢复文件时间戳**

```git utimes```

# SYNOPSIS

**git utimes**

# DESCRIPTION

**git utimes** 把每个被跟踪文件的 mtime 设置为最后一次修改它的提交的时间戳。Git 刻意不在索引中存储时间戳——每次检出都会以操作发生时的时间写入文件——而该命令可以扭转这一点，供依赖文件日期的工具使用（Make、find、站点地图生成器、归档工具等）。

该命令遍历工作树中所有被跟踪的路径，并用对应的提交时间运行 **touch -t**，因此后续 **make** 风格的"自修改以来"比较会与提交历史相符，而不是与仓库克隆的时刻相符。

# CAVEATS

属于 **git-extras**。只影响被跟踪的文件；被忽略和未跟踪的路径保持其现有 mtime。**会使任何以 mtime 作为指纹的增量构建缓存失效**——请在每次重建后重新运行，而不是每个工作日只跑一次。子模块内容不受影响。

# HISTORY

git utimes 是 **git-extras** 的一部分，解决的是 git 不保留文件修改时间这一常见问题。

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

[touch](/man/touch)(1), [git-log](/man/git-log)(1)
