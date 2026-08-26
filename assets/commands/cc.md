# TAGLINE

系统 C 编译器

# TLDR

此命令是 **gcc** 的别名。

# SYNOPSIS

**cc** [_options_] _files_...

# DESCRIPTION

**cc** 传统上是系统 C 编译器命令。在大多数 Linux 系统上，它是指向 **gcc**（GNU 编译器套件）的符号链接或别名。

在构建脚本中使用 **cc** 可以获得跨系统可移植性，因为不同系统的默认编译器可能不同。

# INSTALL

```dnf: sudo dnf install gcc```

```pacman: sudo pacman -S gcc```

```apk: sudo apk add gcc```

```zypper: sudo zypper install gcc```

```brew: brew install gcc```

```nix: nix profile install nixpkgs#gcc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [clang](/man/clang)(1), [make](/man/make)(1)

# RESOURCES

```[Documentation](https://gcc.gnu.org/onlinedocs/)```

<!-- verified: 2026-06-22 -->
