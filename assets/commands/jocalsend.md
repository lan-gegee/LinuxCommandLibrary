# TAGLINE

使用 LocalSend 协议的 TUI 文件共享工具

# TLDR

**启动 jocalsend**以发现设备并共享文件

```jocalsend```

**发送指定文件**

```jocalsend -f [path/to/file]```

**发送文本**

```jocalsend -t "[message]"```

# SYNOPSIS

**jocalsend** [**-f** _file_] [**-t** _text_] [_options_]

# DESCRIPTION

**jocalsend** 是 **LocalSend** 协议的终端实现，提供 TUI 界面，用于在局域网内的设备间收发文件和文本。它与官方 LocalSend 应用以及任何其他 LocalSend 兼容客户端互通。

该工具会自动发现本地子网内的邻近设备，并提供键盘驱动的界面来选择接收方和传输文件。无需互联网连接或账号——所有传输都直接在本地网络中进行。

# CAVEATS

仅在本地网络中可用。发送方和接收方都必须运行 LocalSend 兼容客户端。主要在 Linux 上测试；macOS 支持虽在预期之内但测试较少。

# HISTORY

**jocalsend** 由 **nebkor** 开发，使用基于 **Ratatui** TUI 库的 **Rust** 编写。它面向希望在终端环境中使用 LocalSend 功能的用户。

# INSTALL

```nix: nix profile install nixpkgs#jocalsend```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scp](/man/scp)(1), [rsync](/man/rsync)(1)
