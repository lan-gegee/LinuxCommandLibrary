# TAGLINE

将任务调至前台

# TLDR

**在前台恢复**当前任务

```fg```

**恢复**编号为 1 的任务

```fg %[1]```

**恢复**命令以某字符串开头的任务

```fg %[vim]```

**恢复**命令包含某字符串的任务

```fg %?[config]```

**恢复**上一个任务

```fg %-```

# SYNOPSIS

**fg** [_jobspec_]

# PARAMETERS

_jobspec_
> 要恢复的任务。省略时默认为当前任务。

**%N**
> 编号为 N 的任务。

**%string**
> 命令行以 _string_ 开头的任务。

**%?string**
> 命令行包含 _string_ 的任务。

**%%** 或 **%+**
> 当前任务：最近一次被挂起或转入后台的那个。

**%-**
> 上一个任务。

# DESCRIPTION

**fg** 恢复被挂起或后台运行的任务，把它调到前台并让它成为终端的控制进程，从而重新接收你的按键和信号。Shell 会等待该任务结束或停止之后才打印新的提示符。

任务进入后台有两种方式：用 **Ctrl+Z** 挂起正在运行的命令，或者在启动命令时在末尾加上 **&**。**jobs** 会列出这些任务及其编号和状态；**fg** 把其中某个任务调回前台，而 **bg** 则让它在后台继续运行。不带参数时，**fg** 恢复当前任务，即 **jobs** 输出中标记为 **+** 的那一个。

**%** 前缀是任务标识（jobspec），不是进程 ID。它由 Shell 根据自己的任务表来解释，因此任务编号只在启动它们的那个 Shell 里有效。

**fg** 的退出状态就是被恢复命令的退出状态；若作业控制被禁用或任务不存在，则返回非零值。

# CAVEATS

**fg** 需要作业控制（job control）支持，交互式 Shell 默认启用该功能，但脚本中没有。在非交互式 Shell 中它会失败并提示 "no job control"；如果 Shell 支持，可用 **set -m** 启用它。

任务结束后其编号会被复用，所以刚才还正确的 **%N** 稍后可能指向另一个任务。凭记忆手动输入时，建议优先使用 **%string**。

转入后台的任务仍在运行，并且可能继续向你的终端写入内容，其输出会和提示符交错在一起。被 **Ctrl+Z** 停止的任务则是真正暂停了（**SIGTSTP**），在被恢复之前不会取得任何进展。

如果后台任务试图从终端读取数据，它会被 **SIGTTIN** 信号停止，显示为 "stopped (tty input)"；用 **fg** 把它调到前台即可让它读取输入。

用 **disown** 从任务表中移除的任务无法再通过 **fg** 访问。

# HISTORY

作业控制起源于伯克利的 **C shell**，时间大约在 **1980 年**，后来被 **ksh**、**bash** 及其他 Bourne Shell 衍生版本采纳。**POSIX** 将 **fg** 标准化为可选的 User Portability Utilities 作业控制特性的一部分。它必然是 Shell 内建命令，因为只有 Shell 自己知道它的任务表。

# SEE ALSO

[bg](/man/bg)(1), [jobs](/man/jobs)(1), [disown](/man/disown)(1), [wait](/man/wait)(1), [kill](/man/kill)(1), [nohup](/man/nohup)(1), [bash](/man/bash)(1)

# RESOURCES

```[Documentation](https://www.gnu.org/software/bash/manual/bash.html#Job-Control-Builtins)```

<!-- verified: 2026-07-16 -->
