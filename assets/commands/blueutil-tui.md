# TAGLINE

通过 blueutil 管理 macOS 蓝牙设备的 TUI

# TLDR

**启动**蓝牙管理器 TUI

```blueutil-tui```

# SYNOPSIS

**blueutil-tui**

# DESCRIPTION

**blueutil-tui** 是一个用于管理 macOS 蓝牙设备的终端用户界面。它构建在 **blueutil** 之上，提供交互式界面，让用户可以查看已配对的设备、连接/断开设备以及发现新设备。

该 TUI 显示已配对蓝牙设备的列表及其连接状态，并支持通过键盘快捷键进行设备搜索和刷新。

# CAVEATS

仅适用于 **macOS**，因为它依赖命令行工具 **blueutil**，后者必须通过 **brew install blueutil** 单独安装。可使用 **pipx install blueutil-tui** 或 **uv tool install blueutil-tui** 安装。

# HISTORY

**blueutil-tui** 是社区开发的基于 Python 的 TUI 封装，围绕 **blueutil** 命令行工具构建。它使用 **Textual** 框架进行终端渲染。

# SEE ALSO

[bluetuith](/man/bluetuith)(1)
