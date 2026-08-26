# TAGLINE

找出使用过期共享库的进程

# TLDR

**检查正在使用已删除库的进程**

```sudo checkrestart```

**显示详细输出及被删文件明细**

```sudo checkrestart -v```

**仅报告属于某个软件包的进程**

```sudo checkrestart -p```

**显示适合监控工具的精简输出**

```sudo checkrestart -t```

**以机器可读的制表符分隔格式输出**

```sudo checkrestart -m```

**将特定软件包排除在结果之外**

```sudo checkrestart -i [package_name]```

# SYNOPSIS

**checkrestart** [_options_]

# PARAMETERS

**-v**, **--verbose**
> 详细输出，启用 -f 并显示排除原因。

**-f**, **--show-files**
> 列出已删除的文件以及正在使用它们的程序。

**-d**, **--debug**
> 在输出中包含调试细节，启用 -v。

**-t**, **--terse**
> 精简的单行输出，适合 Nagios 等监控工具。

**-m**, **--machine**
> 机器可读输出；每行以制表符分隔。

**-p**, **--package**
> 仅报告属于某个软件包的进程。

**-a**, **--all**
> 不读取 exclude.conf 和 local-exclude.conf。

**-n**, **--no-lsof**
> 即使 lsof(8) 可用也不使用。

**-i** _REGEXP_, **--exclude-package** _REGEXP_
> 忽略与匹配软件包名称关联的服务。

**-x** [_TYPE:_]_REGEXP_, **--exclude** [_TYPE:_]_REGEXP_
> 排除匹配模式的条目（类型：package、unit、program、pid、file）。

**-e** _PID_
> 排除具有此 PID 的进程。

**-b** _FILE_, **--blocklistfile** _FILE_
> 忽略匹配 FILE 中模式的已删除文件。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**checkrestart** 找出升级后仍在使用旧版（已删除）库的进程。当系统库更新后，运行中的进程仍继续使用内存中加载的旧版本库。该工具找出这些进程，以便重启它们以使用新库。

软件包更新之后（尤其是安全补丁），关键服务在重启前可能仍在运行有漏洞的代码。checkrestart 扫描 **/proc/*/maps** 中对已删除库文件的引用，并报告受影响的进程及其建议的重启命令。

该工具与系统 init 系统集成，给出合适的服务重启命令（**systemctl restart**、**service restart**）。对于非服务进程，则报告进程名和 PID。

# CAVEATS

需要 root 权限才能扫描所有进程。有些进程难以安全重启（X server、会话管理器）。该工具无法检测到所有需要重启的情况。内核更新需要完整重启系统，而非仅重启进程。

# HISTORY

**checkrestart** 是 **debian-goodies** 软件包的一部分，后者是一组面向 Debian 系统的实用工具集合。它的诞生是为了帮助系统管理员识别哪些服务在库更新后需要重启，这在注重安全的环境中是一个常见问题。类似功能也存在于其他工具中，如 Red Hat 生态系统的 **needs-restarting**。

# SEE ALSO

[needrestart](/man/needrestart)(1), [lsof](/man/lsof)(8), [apt](/man/apt)(8)
