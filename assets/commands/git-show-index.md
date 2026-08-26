# TAGLINE

转储包索引文件的内容

# TLDR

**显示包索引内容**

```git show-index < [.idx file]```

# SYNOPSIS

**git** **show-index** < _index_file_

# DESCRIPTION

**git show-index** 从 stdin 读取一个包索引文件并转储其内容。它会显示对应包文件中每个对象的字节偏移量和 SHA-1 哈希值。

这是一个底层（plumbing）命令，用于调试和检查 Git 内部的包文件结构。

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

[git-verify-pack](/man/git-verify-pack)(1)
