# TAGLINE

等待后台进程完成

# TLDR

**等待所有后台任务**完成

```wait```

**按 PID 等待特定任务**

```wait [pid]```

**等待多个 PID**

```wait [pid1] [pid2]```

**按作业号等待某个任务**

```wait %1```

**等待任意一个任务**完成（Bash 4.3+）

```wait -n```

**等待任意任务并将其 PID 存入变量**（Bash 5.1+）

```wait -n -p completed_pid [pid1] [pid2]```

**获取被等待进程的退出状态**

```command & wait $!; echo "Exit status: $?"```

# SYNOPSIS

**wait** [**-fn**] [**-p** _varname_] [_pid_|_jobspec_ ...]

# PARAMETERS

_pid_
> 要等待的进程 ID。

_jobspec_
> 作业说明符（例如 %1、%+、%-）。

**-n**
> 等待指定列表中任意单个任务完成（若未列出则等待所有后台任务），并返回其退出状态。自 Bash 4.3 起可用。

**-f**
> 强制等待每个进程真正终止后才返回，而不是在作业状态变化时（例如被停止时）就返回。需要启用作业控制。

**-p** _varname_
> 将已完成任务的 PID 或作业 ID 赋值给变量 _varname_。与 **-n** 搭配使用最有用，可识别哪个任务完成了。自 Bash 5.1 起可用。

不带参数时，等待所有后台进程。

# DESCRIPTION

**wait** 是一个 shell 内建命令，它会暂停执行，直到指定的后台进程完成为止。它返回被等待进程的退出状态。

给定 PID 时，wait 会阻塞到该进程终止。给定作业说明符（%1、%2 等）时，它等待那个特定的作业。不带参数时，它等待所有子进程。

对于会派生后台进程并需要同步其完成状态或检查其退出状态的脚本而言，这个命令必不可少。

特殊变量 **$!** 保存着最后一个后台进程的 PID，通常与 wait 搭配使用：**command & pid=$!; wait $pid**

# EXAMPLES

```bash
# Run commands in parallel, then wait
command1 &
command2 &
command3 &
wait  # Wait for all three

# Wait and check exit status
long_task &
pid=$!
wait $pid
if [ $? -eq 0 ]; then
    echo "Success"
fi

# Process jobs as they complete (Bash 4.3+)
job1 & job2 & job3 &
while wait -n; do
    echo "A job completed successfully"
done

# Identify which job finished (Bash 5.1+)
cmd1 & pids+=($!)
cmd2 & pids+=($!)
wait -n -p finished "${pids[@]}"
echo "PID $finished exited with status $?"
```

# CAVEATS

wait 只对当前 shell 的子进程有效。无法等待由其他 shell 或其他用户启动的任意进程。

**-n** 选项（等待任意单个任务）是 Bash 扩展，并非所有 POSIX shell 都支持。**-p** 选项要求 Bash 5.1 或更高版本。

如果不带参数且不存在子进程，wait 返回 0。如果指定的 PID 不存在，wait 返回 127。

# INSTALL

```apk: sudo apk add execline```

```brew: brew install execline```

```nix: nix profile install nixpkgs#execline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jobs](/man/jobs)(1), [bg](/man/bg)(1), [fg](/man/fg)(1), [kill](/man/kill)(1), [bash](/man/bash)(1), [disown](/man/disown)(1)
