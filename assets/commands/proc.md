# TAGLINE

提供进程和内核信息的虚拟文件系统

# TLDR

**查看进程信息**

```cat /proc/[pid]/status```

**查看 CPU 信息**

```cat /proc/cpuinfo```

**查看内存信息**

```cat /proc/meminfo```

**查看内核参数**

```cat /proc/sys/kernel/hostname```

# SYNOPSIS

**/proc** 文件系统文档

# COMMON FILES

**/proc/cpuinfo**
> CPU 信息。

**/proc/meminfo**
> 内存统计。

**/proc/loadavg**
> 系统负载平均值。

**/proc/uptime**
> 系统运行时间。

**/proc/version**
> 内核版本。

**/proc/mounts**
> 已挂载的文件系统。

**/proc/[pid]/**
> 每个进程专属的目录。

# DESCRIPTION

**/proc** 是一个虚拟文件系统，提供进程和内核信息。它并不存在于磁盘上——内容由内核动态生成。

# EXAMPLES

```bash
# CPU details
cat /proc/cpuinfo

# Memory usage
cat /proc/meminfo | grep -E "MemTotal|MemFree"

# Process command line
cat /proc/$$/cmdline

# File descriptors
ls -l /proc/$$/fd

# Environment variables
cat /proc/$$/environ | tr '\0' '\n'

# Network statistics
cat /proc/net/dev
```

# PER-PROCESS FILES

```
/proc/[pid]/cmdline   - Command line
/proc/[pid]/cwd       - Current directory
/proc/[pid]/environ   - Environment
/proc/[pid]/exe       - Executable link
/proc/[pid]/fd/       - File descriptors
/proc/[pid]/maps      - Memory mappings
/proc/[pid]/status    - Process status
```

# CAVEATS

Linux 专用。某些文件需要 root 权限。结构随内核版本而异。

# HISTORY

/proc 文件系统最早出现在 **Unix System V** 中，后在 **Linux** 中被大幅扩展用于内核自省。

# SEE ALSO

[ps](/man/ps)(1), [top](/man/top)(1), [proc](/man/proc)(5)
