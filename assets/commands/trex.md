# TAGLINE

正则表达式可视化与测试终端应用

# TLDR

启动交互式正则表达式演练场

```trex```

加载文件用于正则测试

```trex -f [file]```

# SYNOPSIS

**trex** [_options_]

# DESCRIPTION

**trex** 是一个基于终端的正则表达式编写、可视化和测试工具。它呈现一个实时正则演练场，你可以并排输入模式和测试字符串，匹配结果和捕获组会动态高亮显示。它还包含正则帮助菜单，并支持文件加载。

# HISTORY

**trex** 由 **Samyak Bardiya**（samyakbardiya）创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#trex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grex](/man/grex)(1), [rexi](/man/rexi)(1), [ripgrep](/man/ripgrep)(1)
