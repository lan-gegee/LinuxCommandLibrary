# TAGLINE

动态虚拟终端管理器

# TLDR

**启动 dvtm**

```dvtm```

**将修饰键设为** Ctrl+a

```dvtm -m ^a```

**切换默认鼠标支持**

```dvtm -M```

**设置回滚历史**缓冲区大小

```dvtm -h [5000]```

**使用状态 FIFO** 显示状态栏

```dvtm -s [/tmp/dvtm-status]```

**用 abduco 保持会话**

```abduco -A [mysession] dvtm```

# SYNOPSIS

**dvtm** [_options_]

# DESCRIPTION

**dvtm**（dynamic virtual terminal manager）将 dwm 风格的窗口管理带入终端。它在单个终端模拟器内平铺多个终端窗口。

该工具提供动态布局、标签和键盘驱动的窗口管理。它轻量且遵循 suckless 的极简主义哲学。

# CONFIGURATION

**config.h**
> 源码级配置文件，必须编辑并重新编译才能更改键绑定、颜色、布局和行为。

# PARAMETERS

**-v**
> 打印版本并退出。

**-M**
> 切换默认鼠标支持。

**-m** _mod_
> 修饰键（默认：Ctrl+g）。

**-d** _delay_
> ncurses 的转义序列延迟（毫秒）。

**-h** _lines_
> 回滚历史缓冲区大小。

**-t** _title_
> 设置终端标题。

**-s** _status-fifo_
> 从中读取状态栏内容的命名管道。

**-c** _cmd_
> 通过管道送入状态 FIFO 的命令。

# DEFAULT KEYS

默认修饰键（MOD）为 **Ctrl+g**。

**Mod+c**：创建窗口
**Mod+x**：关闭窗口
**Mod+j/k**：聚焦下一个/上一个窗口
**Mod+h/l**：调整主区域大小
**Mod+Enter**：放大窗口
**Mod+Space**：切换布局
**Mod+[1-9]**：按编号跳转到窗口
**Mod+e**：进入复制模式
**Mod+p**：粘贴
**Mod+q**：退出

# LAYOUTS

**tile**：主-堆栈布局
**grid**：网格布局
**bstack**：底部堆栈布局
**fullscreen**：单窗口最大化

# CAVEATS

与 tmux/screen 相比功能有限。没有内置的会话持久化；请配合 **abduco**（推荐）或 **dtach** 使用。配置需要编辑 config.h 并重新编译。默认修饰键 Ctrl+g 若与应用程序冲突，可能需要重新绑定。

# HISTORY

**dvtm** 由 **Marc Andre Tanner** 创建，是一个遵循 **dwm** 原则的终端复用器。它诞生于 **2007 年**前后的 suckless 社区，为终端环境提供动态平铺功能，而没有 screen 或 tmux 那样的复杂性。

# INSTALL

```apt: sudo apt install dvtm```

```dnf: sudo dnf install dvtm```

```pacman: sudo pacman -S dvtm```

```apk: sudo apk add dvtm```

```nix: nix profile install nixpkgs#dvtm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [dtach](/man/dtach)(1), [abduco](/man/abduco)(1)
