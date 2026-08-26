# TAGLINE

终端中的精美 git 提交图

# TLDR

**显示当前仓库的提交图**

```serie```

**限制显示的提交数量**

```serie -n [100]```

**使用拓扑排序的提交顺序**

```serie -o topo```

**使用棱角边线风格和双倍宽度单元格**

```serie -s angular --graph-width double```

# SYNOPSIS

**serie** [_options_]

# PARAMETERS

**-n**, **--max-count** _NUMBER_
> 渲染的最大提交数量。

**-p**, **--protocol** _TYPE_
> 图像协议：auto、iterm、kitty 或 kitty-unicode。默认：auto。

**-o**, **--order** _TYPE_
> 提交排序方式：chrono 或 topo。默认：chrono。

**-g**, **--graph-width** _TYPE_
> 单元格宽度：auto、double 或 single。

**-s**, **--graph-style** _TYPE_
> 边线风格：rounded 或 angular。

**-i**, **--initial-selection** _TYPE_
> 启动时选中的提交：latest 或 head。

**-h**, **--help**
> 显示帮助文本并退出。

**-V**, **--version**
> 输出版本信息并退出。

# CONFIGURATION

**$SERIE_CONFIG_FILE**
> TOML 配置文件路径。未设置时回退到 **$XDG_CONFIG_HOME/serie/config.toml**。

# DESCRIPTION

**serie** 使用终端图像协议（iTerm2 内联图像或 Kitty 图形协议）直接在终端中渲染精美的 git 提交图。它为 **git log --graph --all** 提供了可视化替代方案，支持自定义图形样式、提交排序和交互式浏览。在 TUI 内按 **?** 可查看快捷键速查表。

# CAVEATS

需要支持 iTerm2 内联图像协议或 Kitty 图形协议的终端。不支持 Sixel 图形，并且在会剥离图像转义序列的终端复用器（tmux、screen、Zellij）中无法可靠渲染。

# HISTORY

**serie** 由 **Kyosuke Fujimoto**（lusingander）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S serie```

```apk: sudo apk add serie```

```brew: brew install serie```

```nix: nix profile install nixpkgs#serie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tig](/man/tig)(1), [lazygit](/man/lazygit)(1), [gitui](/man/gitui)(1)
