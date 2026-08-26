# TAGLINE

列出 Linux 命名空间的相关信息

# TLDR

列出所有**命名空间**

```lsns```

以 **JSON 格式**列出命名空间

```lsns -J```

列出**特定进程**的命名空间

```lsns -p 1234```

只列出**特定类型**的命名空间

```lsns -t net```

用**自定义列**列出

```lsns -o NS,TYPE,PID,COMMAND```

仅列出**持久化**的命名空间

```lsns -P```

# SYNOPSIS

**lsns** [_options_] [_namespace_]

# DESCRIPTION

**lsns** 列出 Linux 命名空间的信息。命名空间为各类系统资源提供隔离，该工具显示存在哪些命名空间以及哪些进程在使用它们。

# PARAMETERS

**-t, --type TYPE**
> 按命名空间类型过滤（mnt、net、ipc、user、pid、uts、cgroup、time）

**-p, --task PID**
> 显示特定进程的命名空间

**-o, --output LIST**
> 指定要显示的列

**-l, --list**
> 使用列表输出格式

**-J, --json**
> 以 JSON 格式输出

**-r, --raw**
> 使用原始输出格式

**-n, --noheadings**
> 不打印表头

**-u, --notruncate**
> 不截断列中的文本

**-W, --nowrap**
> 不换行显示多行单元格

**-P, --persistent**
> 只显示持久化的命名空间

**-T, --tree REL**
> 以指定关系显示树状视图

# NAMESPACE TYPES

**mnt**: 挂载点
**net**: 网络资源
**ipc**: System V IPC 对象
**user**: 用户和组 ID
**pid**: 进程 ID
**uts**: 主机名和域名
**cgroup**: Cgroup 根目录
**time**: 启动时钟和单调时钟

# CAVEATS

非 root 用户可能看到不完整的结果，因为某些命名空间信息需要提升权限。默认输出格式可能随版本变化；脚本请使用显式选项。

# HISTORY

**lsns** 属于 **util-linux**，让容器化和进程隔离所依赖的 Linux 命名空间子系统变得可见。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nsenter](/man/nsenter)(1), [unshare](/man/unshare)(1), [namespaces](/man/namespaces)(7)
