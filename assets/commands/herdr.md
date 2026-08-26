# TAGLINE

专为 AI 编程智能体打造的终端复用器

# TLDR

在当前项目中**启动** herdr

```herdr```

**脱离**会话（默认前缀键风格）

```[ctrl+b] q```

之后**重新接入**

```herdr```

通过脚本**安装**

```curl -fsSL https://herdr.dev/install.sh | sh```

# SYNOPSIS

**herdr** [*options*] [*command*]

# DESCRIPTION

**herdr** 是一个面向智能体的终端复用器：它是一个单独的 Rust 二进制文件，运行在你现有的终端内，为编程智能体（Claude Code、Codex 等）显示实时窗格，并使会话在脱离后继续运行——包括通过 SSH 连接的场景。它支持键盘和鼠标操作、tmux 风格的前缀键、窗口拆分、插件以及套接字 API，让各个智能体能够创建窗格并相互等待。

文档：https://herdr.dev/docs/

# PARAMETERS

**herdr**

> 接入当前工作区的会话，不存在则创建。

其他子命令和标志（远程接入、插件管理等）因版本而异——请运行 **herdr --help** 并参阅在线快速入门。

常见用法：按前缀键 **ctrl+b** 再按 **q** 脱离；再次运行 **herdr** 即可重新接入。

# CAVEATS

智能体集成取决于你安装了哪些工具。套接字 API 和插件会扩大攻击面——请谨慎对待不受信任的插件。它并非所有 **tmux** 工作流的直接替代品，需要学习 herdr 自己的按键绑定。

# INSTALL

```brew: brew install herdr```

```nix: nix profile install nixpkgs#herdr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [zellij](/man/zellij)(1), [gemini](/man/gemini)(1)

# RESOURCES

```[Source code](https://github.com/ogulcancelik/herdr)```

```[Homepage](https://herdr.dev)```

```[Documentation](https://herdr.dev/docs/)```

<!-- verified: 2026-07-19 -->
