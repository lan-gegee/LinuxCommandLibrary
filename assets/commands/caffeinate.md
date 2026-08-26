# TAGLINE

创建 macOS 电源管理声明（assertion），防止系统休眠

# TLDR

**无限期阻止空闲休眠**（按 Ctrl-C 停止）

```caffeinate```

**防止显示器休眠**

```caffeinate -d```

**在一段时间内阻止空闲休眠**（单位为秒）

```caffeinate -t [3600]```

**在命令运行期间阻止休眠**

```caffeinate -i [make]```

**组合标志** — 让显示器和磁盘保持唤醒 1 小时

```caffeinate -dim -t [3600]```

**持有声明直到某个进程**（按 PID）退出

```caffeinate -w [pid]```

**阻止系统休眠**（更强，仅在使用交流电源时有效）

```caffeinate -s```

# SYNOPSIS

**caffeinate** [**-disum**] [**-t** _timeout_] [**-w** _pid_] [_utility_ [_arguments_]]

# PARAMETERS

**-d**
> 防止显示器休眠。

**-i**
> 防止系统因空闲而休眠。（未指定任何声明标志时为默认行为）

**-m**
> 防止磁盘因空闲而休眠。

**-s**
> 防止系统休眠。仅在笔记本电脑接入交流电源时有效。

**-u**
> 声明用户处于活动状态。该声明会在 5 秒后自动释放（若被取消则更早）——适用于短暂刷新活动状态而不无限期保持的场景。

**-t** _timeout_
> 在 _timeout_ 秒后释放声明。不带此标志时，声明会一直保持，直到 caffeinate 被终止或所包裹的工具退出。

**-w** _pid_
> 持有声明，直到给定 PID 的进程退出。

_utility_ [_arguments_]
> 如果给定了工具，caffeinate 会运行它并持有声明直到其退出。`caffeinate -i make` 是惯用模式。

# DESCRIPTION

**caffeinate** 创建一个或多个 **IOKit 电源管理声明（assertion）**来抑制不同类型的休眠。它是让 macOS 在任务执行期间不进入显示休眠、空闲休眠、磁盘休眠或系统休眠的受支持方式。

带工具调用时，caffeinate 会派生并运行该工具，同时持有声明直到工具退出。不带工具时，它会一直运行，直到收到信号（如 Ctrl-C）或 `-t` 超时。多个标志可以组合使用；每个标志各自添加一条声明。

# CAVEATS

仅限 macOS（自 OS X 10.8 Mountain Lion 起随系统提供于 `/usr/bin/caffeinate`）。使用电池时 `-s` 可能被忽略——笔记本电脑上 `-i` 是可靠的选择。`-u` 只带来短暂的活动提示；需要更长久的保证请用 `-d -i`。创建声明不能覆盖合上笔记本盖子（clamshell）的休眠行为——那种情况请使用 `pmset`。

Linux 上的等价工具是 `systemd-inhibit` 或 `caffeine`（GNOME 小程序）。X11 下可用 `xset s off -dpms` 控制屏幕保护程序和 DPMS。

# HISTORY

**caffeinate** 由 Apple 在 **Mac OS X 10.8（Mountain Lion，2012 年）**中引入，作为替代“向系统注入鼠标事件以保持 Mac 唤醒”这类临时脚本的官方 CLI 方案。它封装了 IOKit 的 `IOPMAssertion` API。

# INSTALL

```aur: yay -S caffeinate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[caffeine](/man/caffeine)(1), [xset](/man/xset)(1), [systemd-inhibit](/man/systemd-inhibit)(1)
