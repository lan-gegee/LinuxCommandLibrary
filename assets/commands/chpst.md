# TAGLINE

以改变的进程状态运行程序

# TLDR

**以其他用户身份运行命令**

```chpst -u [user] [command]```

**以特定用户和组运行**

```chpst -u [user:group] [command]```

**限制内存使用**

```chpst -m [50000000] [command]```

**从目录设置环境变量**

```chpst -e [/etc/service/myapp/env] [command]```

**运行前切换目录**

```chpst -/ [/var/lib/app] [command]```

**限制打开文件的数量**

```chpst -o [1000] [command]```

**设置 nice 级别**

```chpst -n [10] [command]```

# SYNOPSIS

**chpst** [_options_] _command_

# DESCRIPTION

**chpst** 根据给定选项改变进程状态并运行程序。它是 **runit** 服务监管套件的一部分，提供了一种标准化的方式来设置服务进程的用户、资源限制和环境。

该工具整合了几种常见的进程修改操作：更改用户/组身份、设置资源限制、从文件加载环境变量以及获取锁。这简化了原本需要多条命令的服务 run 脚本。

环境目录（配合 **-e** 使用）包含以环境变量命名的文件，文件内容即为变量值。这种模式在 runit 和 daemontools 服务管理中很常见。

# PARAMETERS

**-u** _user[:group]_
> 在运行命令前设置 UID 和 GID。

**-e** _directory_
> 从目录中的文件设置环境变量。

**-m** _bytes_
> 限制数据段、栈和锁定内存大小。

**-d** _bytes_
> 限制数据段大小。

**-o** _n_
> 限制打开文件描述符的数量。

**-p** _n_
> 限制进程数量。

**-f** _bytes_
> 限制输出文件大小。

**-c** _bytes_
> 限制核心转储（core dump）大小。

**-n** _inc_
> 调整 nice 级别。

**-/** _dir_
> 更改根目录（chroot）。

**-C** _pwd_
> 在启动程序前将工作目录更改为 pwd。与 -/ 组合时，在 chroot 之后切换目录。

**-b** _argv0_
> 以 argv0 作为程序的第 0 个参数运行 prog。

**-l** _lock_
> 以写方式打开锁文件，获取独占锁；若锁已被其他进程持有则立即失败。

**-L** _lock_
> 以写方式打开锁文件，获取独占锁；若锁被其他进程持有则等待。

**-P**
> 在新的进程组中运行 prog。

**-0**, **-1**, **-2**
> 启动 prog 前关闭标准输入 (0)、标准输出 (1) 或标准错误 (2)。

**-v**
> 向标准错误输出详细信息。

# CAVEATS

更改用户需要 root 权限。资源限制是按进程生效的；子进程会继承限制但各自独立计算。chroot 选项要求目标位置有完整的根文件系统。锁文件必须位于支持锁的文件系统上。chpst 在选项错误时以退出码 100 结束，在改变进程状态失败时以退出码 111 结束。

# HISTORY

**chpst** 由 **Gerrit Pape** 创建，是 **runit** 的一部分。runit 是一种带服务监管的 Unix init 方案，发布于 **21 世纪初**。它的灵感来自 **daemontools** 的类似工具（setuidgid、softlimit、envdir），但将这些功能合并到了单一命令中。该工具因其简洁性而持续流行，并在 runit 之外的各种服务管理场景中被使用。

# INSTALL

```apt: sudo apt install runit```

```apk: sudo apk add runit```

```brew: brew install runit```

```nix: nix profile install nixpkgs#runit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runsv](/man/runsv)(8), [runsvdir](/man/runsvdir)(8), [sv](/man/sv)(8)
