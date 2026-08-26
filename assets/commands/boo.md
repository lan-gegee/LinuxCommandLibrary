# TAGLINE

基于 libghostty 的 screen 风格终端复用器

# TLDR

**创建新会话**（默认以当前目录命名）

```boo new [session_name]```

**创建以分离模式运行命令的会话**

```boo new [session_name] -d -- [command]```

**列出**所有会话

```boo ls```

**重新连接**到某个会话

```boo attach [session_name]```

**打开全屏会话管理器**

```boo ui```

向分离状态的会话**发送文本**并提交

```boo send [session_name] --text '[make]' --enter```

**等待某个会话的输出稳定后**读取其屏幕内容

```boo wait [session_name] --idle && boo peek [session_name]```

**终止**一个会话

```boo kill [session_name]```

# SYNOPSIS

**boo** \<command\> [options] [arguments]

# COMMANDS

**new [NAME]**

> 创建新会话。默认以当前目录名命名。使用 **-d** 时会话以分离模式启动，可在 **--** 之后传入要运行的命令。

**attach NAME**

> 重新连接到会话，恢复其屏幕内容、样式、光标和回滚缓冲区。别名：**at**、**a**。连接时会从其他已连接的客户端手中接管该会话。

**ls**

> 列出会话。**--json** 输出机器可读的结果。

**ui**

> 全屏会话管理器，提供切换、创建、调整大小和终止会话的键绑定。

**send NAME**

> 不连接会话而直接发送输入。**--text TEXT** 发送字面文本，**--enter** 提交文本，**--key KEY1,KEY2** 发送控制按键，如 Enter、C-c 或 Up。

**peek NAME**

> 打印会话渲染后的屏幕状态。**--scrollback** 包含历史记录，**--json** 额外输出尺寸、光标和标题。

**wait NAME**

> 阻塞直到满足条件：**--text TEXT** 等待文本出现在屏幕上，**--idle** 等待输出静默满 2 秒，**--timeout DUR** 设置最长等待时间（如 500ms、2s、1m、4h、1d）。

**rename OLD NEW**

> 重命名会话。

**kill NAME**

> 结束一个会话。**--all** 结束所有会话。

**help [command]**

> 显示概览、单个命令的详情，或用 **--all** 显示所有帮助页。

# KEY BINDINGS

前缀键为 **Ctrl-a**，遵循 GNU screen 的默认设置。

**C-a d**

> 从当前会话分离；会话继续在后台运行。

**C-a l**

> 重绘屏幕。

**C-a a**

> 向会话中的程序发送字面量 Ctrl-a。

# DESCRIPTION

**boo** 是一款秉承 GNU screen 精神的终端复用器：每个会话一个窗口、Ctrl-a 前缀键、会话在断开连接后依然存活。它的独特之处在于所有会话输出都通过 **libghostty-vt**——Ghostty 终端的终端模拟核心——进行解析，因此重新连接时可以完整忠实地重建全屏状态（内容、SGR 样式、光标位置、滚动区域、终端模式和窗口标题），而不是近似还原。

客户端/守护进程架构让会话保持存活：客户端管理 TTY，而每个会话的守护进程拥有挂接 PTY 的子进程，并将其输出馈送到持久的 ghostty-vt 终端流中。即使在分离状态下也能应答终端查询，从而防止 TUI 程序在后台会话中挂起。

除 **attach** 外的所有命令都无需终端即可运行，因此 boo 可以编写脚本，供自动化流程和 AI 智能体使用：**send** 向会话输入内容，**wait** 阻塞直到输出稳定或出现指定文本，**peek** 读取渲染后的屏幕（可选 JSON 格式）。

退出码：0 成功，1 错误，2 用法错误，3 会话未找到，4 等待超时。

# CAVEATS

同一时间只能有一个客户端连接到会话；连接时会抢占会话，没有类似 screen 多显示模式的功能。每个会话只有一个窗口——不支持分屏或标签页，其设计模型是"一个任务一个会话"，通过 **boo ui** 来调度。**Ctrl-a** 前缀尚不可配置，且会话始终以 TERM=xterm-256color 运行。项目尚年轻，不能完全替代 screen。

# HISTORY

boo 于 2026 年由 Coder 发布，以 Zig 编写，构建在 libghostty-vt 之上——这是从 Ghostty 终端模拟器中抽出的 MIT 许可终端模拟库。它复兴了 GNU screen 的简单持久会话模式，同时加入了精确的现代终端模拟以及面向脚本化和智能体驱动工作流的自动化原语。

# SEE ALSO

[screen](/man/screen)(1), [tmux](/man/tmux)(1), [zellij](/man/zellij)(1), [abduco](/man/abduco)(1), [dtach](/man/dtach)(1), [ghostty](/man/ghostty)(1)

# RESOURCES

```[Source code](https://github.com/coder/boo)```

<!-- verified: 2026-06-12 -->
