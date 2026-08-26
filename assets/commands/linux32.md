# TAGLINE

将体系结构执行域设为 32 位并运行指定程序

# TLDR

此命令是 setarch 的**别名**

```tldr setarch```

# SYNOPSIS

**linux32** [_options_] [_program_ [_arguments_]]

# DESCRIPTION

**linux32** 将体系结构执行域设为 32 位并运行指定程序。它等价于 `setarch linux32`，用于在 64 位系统上通过修改 personality 标志来运行 32 位程序。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setarch](/man/setarch)(8), [linux64](/man/linux64)(8)
