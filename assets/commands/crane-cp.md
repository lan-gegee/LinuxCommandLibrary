# TAGLINE

crane copy 的别名

# TLDR

**在镜像仓库之间复制镜像**

```crane cp [source_image] [destination_image]```

**复制时选择平台**

```crane cp --platform linux/amd64 [source_image] [destination_image]```

# SYNOPSIS

**crane** **cp** [_options_] _source_ _destination_

# DESCRIPTION

**crane cp** 是 **crane copy** 的别名。它在镜像仓库之间复制容器镜像，无需先拉取到本地存储，并尽可能在服务端完成复制。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-copy](/man/crane-copy)(1), [crane-push](/man/crane-push)(1), [crane-pull](/man/crane-pull)(1)
