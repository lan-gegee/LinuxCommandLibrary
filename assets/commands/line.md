# TAGLINE

从标准输入读取一行并写入标准输出

# TLDR

**读取**单行输入

```line```

# SYNOPSIS

**line**

# DESCRIPTION

**line** 从标准输入读取一行并写入标准输出。它是一个简单的工具，用于在 shell 脚本中精确读取一行。

# CAVEATS

在许多系统上已被弃用。为了脚本的可移植性，建议改用 `read` shell 内建命令或 `head -n 1`。

# INSTALL

```dnf: sudo dnf install mesa-demos```

```pacman: sudo pacman -S mesa-demos```

```apk: sudo apk add mesa-demos```

```nix: nix profile install nixpkgs#mesa-demos```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[read](/man/read)(1), [head](/man/head)(1)
