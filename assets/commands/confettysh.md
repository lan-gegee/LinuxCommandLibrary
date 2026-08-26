# TAGLINE

通过 SSH 送上彩带和烟花

# TLDR

**连接到 confettysh SSH 服务器观看彩带动画**

```ssh [host] -t confetti```

**连接观看烟花动画**

```ssh [host] -t fireworks```

**连接到本地 confettysh 服务器**

```ssh -p [2222] localhost```

# SYNOPSIS

**confettysh**

# DESCRIPTION

**confettysh** 是一台在终端中显示彩带和烟花动画的 SSH 服务器。它由 Charmbracelet 基于 Wish 框架构建，为 Maas Lalani 的 confeTTY 项目提供 SSH 接口。

该服务器接受 SSH 连接，并在连接的终端中直接渲染基于粒子的动画。用户可以通过把动画类型作为 SSH 命令传入来选择彩带或烟花。按下任意键会触发额外的粒子效果。

confettysh 主要用于演示如何使用 Go 语言和 Bubble Tea 框架构建基于 SSH 的 TUI 应用，同时也可作为有趣的庆祝工具。

# CAVEATS

confettysh 是一台 SSH 服务器，不是独立的 CLI 工具。它需要有一个正在运行的服务器实例可供连接。动画质量取决于终端模拟器的 Unicode 支持和渲染速度。

# HISTORY

**confettysh** 由 **Charmbracelet** 创建，是其使用 Bubble Tea TUI 框架和 Wish SSH 库构建的终端工具套件的一部分。它将 Maas Lalani 编写的 confeTTY 动画引擎封装为一台用 Go 编写的 SSH 服务器。

# SEE ALSO

[ssh](/man/ssh)(1), [sl](/man/sl)(1), [cowsay](/man/cowsay)(1), [lolcat](/man/lolcat)(1)
