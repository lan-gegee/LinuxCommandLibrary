# TAGLINE

用 Zig 编写的快速键盘驱动 Git 终端界面

# TLDR

在当前 Git 仓库中**打开 ziggity**

```ziggity```

**通过 Homebrew 安装**（macOS / Linux）

```brew install simoarpe/ziggity/ziggity```

**从源码构建**（需要 Zig 0.16）

```zig build -Doptimize=ReleaseSafe```

从 Shell 中**指向共享配置文件**

```export ZIGGITY_CONFIG="$HOME/.config/ziggity/config.ini"```

**显示应用内快捷键**（运行后）

```?```

**退出**

```q```

# SYNOPSIS

**ziggity**

# DESCRIPTION

**ziggity** 是一个面向 Git 的终端用户界面（TUI），以小巧的 Zig 二进制程序提供 lazygit 风格的工作流。它以子进程方式驱动原生 **git**（不使用 libgit2），并使用 libvaxis 构建界面。分屏面板涵盖 Status、Files、Branches、Commits 和 Stash，配有实时 diff 预览和上下文相关的底部栏。

核心操作全部由键盘驱动：暂存或取消暂存整个文件或单个 hunk 与行，通过应用内的 summary/body 编辑器提交，管理分支和标签，带可选消息的 stash，不阻塞界面的 fetch/pull/push，以及通过可视化计划编辑器执行交互式 rebase。其他功能包括真正的 **git log --graph** 查看器、多选范围、自定义补丁构建、合并冲突解决、GPG 签名检查、worktree 和 submodule 导航、可重映射按键以及可自定义主题颜色。

在任何 Git 仓库中运行 **ziggity**。按 **?** 显示按键绑定浮层（自动滚动到当前聚焦的面板），按 **q** 退出。项目为 macOS、Linux（musl）和 Windows 提供预构建的静态二进制文件；Homebrew 从项目的 tap 安装 macOS/Linux 软件包。

# KEYBOARD SHORTCUTS

**1**–**5**：聚焦 Status / Files / Branches / Commits / Stash
**h** **l** / 方向键：在侧边面板之间移动焦点
**j** **k** / 方向键：移动选择
**tab**：聚焦 Diff 面板（及返回）
**space**：暂存文件 · 检出分支 · 应用 stash（视焦点而定）
**c**：提交
**a**：全部暂存/取消暂存（Files）
**d** / **D**：丢弃菜单 / 全部丢弃
**f** / **p** / **P**：fetch / pull / push
**i**：交互式 rebase 计划编辑器
**ctrl+l**：提交图查看器
**ctrl+z**：撤销上一次操作
**?**：按键绑定帮助
**q**：退出

# CONFIGURATION

**ZIGGITY_CONFIG**
> 指向全局生效的 INI 配置文件的环境变量。没有自动加载的 XDG 路径；若要在多个仓库间共享设置，请在 Shell 配置中设置该变量。

**\<repo\>/.ziggity.ini**
> 每个仓库单独的 INI 文件，优先级高于 **ZIGGITY_CONFIG**。完全没有任何配置文件时，设置回退到默认值和每仓库自动检测（尤其是编辑器）。

常见设置包括面板布局（**side_panel_width_percent**、**expand_focused_side_panel**）、提交编辑器参考线（**commit_summary_limit**、**commit_body_guide**）、刷新/fetch 间隔、编辑器预设（**editor_preset**、**editor_command**）、可重映射按键（**key.\<name\>**）、主题颜色（**color.\<name\>** 为终端调色板索引 0–255）以及自定义命令（**command.\<key\>**）。

# CAVEATS

运行时要求 **PATH** 中存在 **git**。破坏性历史操作（硬重置、强制推送、rebase）应谨慎使用。macOS 预构建二进制可能需要一次性清除隔离标记（**xattr -d com.apple.quarantine**）。Windows 构建为交叉编译且属实验性质。与 lazygit 的功能对等在某些方面是有意不完整的（例如撤销后的重做尚未实现）。

# HISTORY

**ziggity** 由 **Simone Arpe** 创建，使用 **Zig** 编写。它追求 lazygit 式的使用感受但并非逐行移植，强调小巧且依赖少的二进制、明确的内存所有权以及原生的 git 子进程。

# SEE ALSO

[git](/man/git)(1), [lazygit](/man/lazygit)(1), [gitui](/man/gitui)(1), [tig](/man/tig)(1)

# RESOURCES

```[Source code](https://github.com/simoarpe/ziggity)```

<!-- verified: 2026-07-20 -->
