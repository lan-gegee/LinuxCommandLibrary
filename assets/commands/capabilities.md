# TAGLINE

Linux 进程特权能力（capabilities）系统

# TLDR

**查看**可执行文件的能力

```getcap [/path/to/binary]```

**递归查看目录中**文件的能力

```getcap -r [/path/to/directory]```

**为可执行文件设置能力**

```sudo setcap cap_net_bind_service=+ep [/path/to/binary]```

**移除可执行文件上的所有能力**

```sudo setcap -r [/path/to/binary]```

**查看当前进程能力**

```grep Cap /proc/self/status```

**解码能力的十六进制值**

```capsh --decode=[hex_value]```

**打印当前 Shell 的能力**

```capsh --print```

# SYNOPSIS

**getcap** [_options_] _file_...

**setcap** _capabilities_ _file_

**capsh** [_options_]

# PARAMETERS

**getcap -r** _directory_
> 递归搜索具有能力标志的文件。

**getcap -v**
> 详细输出，显示所有被搜索的文件（包括没有能力的）。

**setcap** _cap=flags_ _file_
> 设置能力（flags：e=effective、p=permitted、i=inheritable）。用 + 添加，用 - 移除。

**setcap -r** _file_
> 移除文件上的所有能力。

**setcap -q**
> 安静模式，抑制警告。

**capsh --print**
> 打印当前能力和 securebits。

**capsh --decode** _hex_
> 将能力位掩码解码为人类可读的名称。

**capsh --drop** _cap_
> 从边界集（bounding set）中丢弃一项能力。

**capsh --caps**=_cap-set_
> 设置进程当前生效的能力。

**capsh --keep**=_0|1_
> 设置 keep-capabilities 标志（0=关，1=开）。

# COMMON CAPABILITIES

**cap_net_bind_service**：绑定 1024 以下端口
**cap_net_raw**：使用原始套接字（如 ping）
**cap_net_admin**：网络管理（接口、防火墙、路由）
**cap_sys_admin**：广泛的系统管理（mount、sethostname 等）
**cap_sys_ptrace**：用 ptrace 跟踪任意进程
**cap_dac_override**：绕过文件的读、写、执行权限检查
**cap_setuid/cap_setgid**：更改进程的 UID/GID
**cap_chown**:任意更改文件所有者
**cap_kill**：向任意进程发送信号
**cap_fowner**：绕过要求文件所有者的操作权限检查

# DESCRIPTION

**Linux capabilities** 将传统上由 root 持有的特权划分为若干独立单元，可分别授予可执行文件。从内核 2.2 起，不必让整个程序以 root 运行，而是通过特定能力只授予所需的权限。

例如，需要绑定 80 端口的 Web 服务器可以只获得 **cap_net_bind_service**，而不必拥有完整的 root 权限。这遵循最小权限原则，限制安全漏洞可能造成的破坏。

每个线程的能力存在于三个集合中：**permitted**（可用能力的上限）、**effective**（当前在权限检查中生效）和 **inheritable**（跨 execve 保留）。文件能力存储在扩展属性中，控制二进制执行时获得哪些能力。

**libcap** 库提供管理能力的用户空间工具和 API，包括 **getcap**、**setcap** 和 **capsh**。

# CAVEATS

能力是 Linux 特有的，无法移植到其他 Unix 系统。并非所有文件系统都支持能力扩展属性（如 NFS、FAT）。某些应用程序显式检查 UID 0 而非能力。能力继承规则复杂且容易配置错误。Docker 和容器通过运行时配置单独管理能力。**cap_sys_admin** 被有意设计得职责宽泛，会授予大范围特权。

# HISTORY

POSIX 能力在 **1990 年代**的 POSIX.1e 标准草案中被提出，但该标准最终未定稿。Linux 从内核 **2.2**（1999 年）开始实现能力，并在 **2.6.24**（2008 年）中加入文件能力这一重大改进。随着容器化和注重安全的系统管理的发展，该特性变得日益重要。

# SEE ALSO

[getcap](/man/getcap)(8), [setcap](/man/setcap)(8), [capsh](/man/capsh)(1)
