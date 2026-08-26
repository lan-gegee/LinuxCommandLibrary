# TAGLINE

用 Rust 编写的兼容 POSIX 的交互式 Shell

# TLDR

**通过 Cargo 安装**

```cargo install nsh```

**启动**交互式会话

```nsh```

作为登录 shell **运行**（如果已安装在 PATH 中）

```nsh -l```

# SYNOPSIS

**nsh** [*options*] [*script*]

# DESCRIPTION

**nsh** 是一个专注于交互式生产力的命令行 shell，同时保持面向 POSIX 并带有部分 Bash 扩展。其特性包括制表符补全、语法高亮、Bash 补全支持（通过在内部调用真正的 Bash 实现）以及内置的零配置默认值。它使用 Rust 编写。

该项目自述为 alpha 阶段：许多 Bash 特性仍然缺失，日常使用可能遇到不完善之处。文档位于仓库的 **docs/** 目录中。

# PARAMETERS

你构建版本支持的选项（脚本执行、交互模式、版本）请参见 **nsh --help**。主要安装方式是 **cargo install nsh**。

# CAVEATS

Alpha 软件；未经测试请勿替换生产环境的登录 shell。Bash 补全桥接需要已安装 **bash**。对于复杂的交互式设置，功能完备性落后于 Bash/zsh。

# INSTALL

```brew: brew install nsh```

```nix: nix profile install nixpkgs#nsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1), [oil](/man/oil)(1)

# RESOURCES

```[Source code](https://github.com/nuta/nsh)```

```[Documentation](https://github.com/nuta/nsh/tree/master/docs)```

<!-- verified: 2026-07-19 -->
