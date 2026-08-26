# TAGLINE

显示 Alire 软件包管理器命令的帮助信息。

# TLDR

**显示**特定 alr 命令的**帮助**

```alr help [command]```

**列出所有可用的** alr 命令

```alr help```

**显示全局选项**和一般帮助信息

```alr --help```

# SYNOPSIS

**alr** **help** [_command_]

# PARAMETERS

**command**
> 要获取帮助的 alr 子命令名称。

# DESCRIPTION

**alr help** 显示 Alire（Ada/SPARK 软件包管理器）命令的详细帮助信息。不带参数运行时，它会列出所有可用命令；提供命令名称时，则显示该特定命令的详细用法信息。

Alire 是面向 Ada/SPARK 的源码软件包管理器，类似于 Rust 的 cargo 或 OCaml 的 opam。**alr** 命令行工具负责管理依赖、构建项目，并从 Alire 目录引入库。

# INSTALL

```apt: sudo apt install alire```

```aur: yay -S alire```

```nix: nix profile install nixpkgs#alire```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[alr](/man/alr)(1), [alr-version](/man/alr-version)(1)

# RESOURCES

```[Source code](https://github.com/alire-project/alire)```

```[Homepage](https://alire.ada.dev/)```

```[Documentation](https://alire.ada.dev/docs/)```

<!-- verified: 2026-06-11 -->
