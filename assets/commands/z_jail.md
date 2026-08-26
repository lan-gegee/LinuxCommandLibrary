# TAGLINE

用于执行原生代码的多层 Linux 沙箱

# TLDR

在隔离的根文件系统内并强制执行 seccomp 的情况下**运行程序**

```sudo z_jail --root=[path/to/rootfs] --seccomp-enforce -- [program] [args...]```

执行前**校验二进制完整性**

```sudo z_jail --root=[path/to/rootfs] --seccomp-enforce --self-hash=[blake2b_hex] -- [program]```

抑制审计 JSON 输出

```sudo z_jail --root=[path/to/rootfs] --quiet -- [program]```

从源码**构建**约 130 KiB 的 PIE 二进制

```make```

# SYNOPSIS

**z_jail** **--root=**_dir_ [_options_] **--** _program_ [_args_]

# PARAMETERS

**--root=**_dir_
> 包含目标二进制及其依赖的沙箱根目录（必需）。

**--seccomp-enforce**
> 启用 seccomp-BPF 白名单（**whitelist-v1**，15 个系统调用）。

**--self-hash=**_hex_
> 除非 **z_jail** 二进制与给定的 BLAKE2b-256 哈希一致，否则拒绝运行。

**--quiet**
> 抑制 JSON 审计输出。

**--verbose**
> 启用调试日志。

**--version**
> 打印构建 ID 并退出。

**--help**
> 显示用法并退出。

# DESCRIPTION

**z_jail** 是一个轻量级的 C99 沙箱，用于在 Linux 上执行不受信任的原生二进制程序。它组合了七层防御，除标准 C 工具链外没有任何运行时依赖：Truthimatics 判定引擎、mount/PID/net/IPC/UTS 命名空间、**pivot_root**、带锁定 securebits 的能力丢弃、**PR_SET_NO_NEW_PRIVS**、seccomp-BPF 系统调用白名单，以及带 BLAKE2b 内容指纹的 JSON 审计日志。

父进程克隆隔离的命名空间，应用资源限制，切换到 **--root**，安装 seccomp 过滤器，然后 **execve** 目标程序。子进程退出后，会写入一条描述判定结果、耗时、沙箱设置和可执行文件哈希的审计记录。

**z_jail** 面向 CI 流水线、CTF jail 和轻量级代码评测等场景，定位介于 **bwrap** 这类极简工具与 **nsjail** 或 **gVisor** 这类较重的沙箱之间。

# CAVEATS

**z_jail** 需要 **CAP_SYS_ADMIN**（通常是 root）来创建命名空间和执行 **pivot_root**。默认 seccomp 白名单只允许 15 个系统调用——许多程序需要自定义策略，否则会被杀死。动态链接的二进制需要将库放入 **--root** 内；静态二进制只需可执行文件本身。内核漏洞利用和硬件侧信道不在声明的威胁模型范围内。

# HISTORY

**Z-Jail** 由 **Division-36** 开发，于 **2026 年**发布 **v1** 版本，面向 Linux 内核 **5.4+**，仅需一条 **make** 命令构建，无外部库依赖。

# SEE ALSO

[bwrap](/man/bwrap)(1), [firejail](/man/firejail)(1), [chroot](/man/chroot)(8)

# RESOURCES

```[Source code](https://github.com/Division-36/Z-Jail)```

```[Documentation](https://github.com/Division-36/Z-Jail/tree/main/docs)```

<!-- verified: 2026-07-11 -->
