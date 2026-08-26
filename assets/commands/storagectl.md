# TAGLINE

枚举并挂载 systemd 存储提供程序提供的存储卷

# TLDR

**列出所有可用的存储卷**

```storagectl volumes```

**列出存储提供程序**

```storagectl providers```

**列出存储卷模板**

```storagectl templates```

**列出匹配通配符的存储卷**

```storagectl volumes '*foo*'```

**使用 storage 挂载助手挂载目录存储卷**（需要 root 权限）

```mount -t storage fs:myvol /mnt/myvol```

# SYNOPSIS

**storagectl** [OPTIONS...] {COMMAND} [NAME...]

# DESCRIPTION

**storagectl** 是一个用于检查存储提供程序及其暴露的存储卷的命令行工具。它是 systemd 项目的一部分。

存储提供程序实现 `io.systemd.StorageProvider` Varlink 接口，并在 `/run/systemd/io.systemd.StorageProvider/`（系统级）或用户等效路径下注册一个 AF_UNIX 套接字。

systemd 自带两个提供程序：

- `systemd-storage-block@.service` — 暴露系统的块设备。
- `systemd-storage-fs@.service` — 暴露来自底层文件系统的常规文件和目录（支持通过模板即时创建）。

storagectl 还可以充当挂载助手（`mount -t storage ...` 或 `mount -t storage.FSTYPE ...`），以获取存储卷并将其挂载到任意位置。源以 `PROVIDER:VOLUME` 形式指定。

# COMMANDS

**volumes** [_GLOB_]
> 列出存储卷（默认命令）。可选的通配符用于过滤卷名。

**templates** [_GLOB_]
> 列出支持的存储卷模板（适用于支持动态创建的提供程序）。

**providers**
> 列出已知的存储提供程序及其套接字是否可达。

# OPTIONS

**--system**
> 操作系统级提供程序（默认）。

**--user**
> 操作每用户提供程序。

**--json**=_MODE_
> 以 JSON 输出（"short"、"pretty" 或 "off"）。

**--no-pager**, **--no-legend**, **--no-ask-password**
> 控制输出和身份验证行为。

# CAVEATS

该工具相对较新（在 systemd 261 中加入）。存储提供程序是一个实验性/低层级接口，主要面向高级用例和其他 systemd 组件（例如 machinectl）。

# SEE ALSO

[systemctl](/man/systemctl)(1), [mount](/man/mount)(8), [machinectl](/man/machinectl)(1)

# RESOURCES

```[Source code](https://github.com/systemd/systemd)```

```[Documentation](https://www.freedesktop.org/software/systemd/man/latest/storagectl.html)```

<!-- verified: 2026-07-11 -->
