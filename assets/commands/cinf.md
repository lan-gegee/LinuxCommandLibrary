# TAGLINE

从命令行检查 Linux 命名空间和 cgroups

# TLDR

**列出所有命名空间**（需要 root）

```sudo cinf```

**按 id 检查命名空间**

```sudo cinf --namespace [4026532193]```

**显示某个 PID 的命名空间**

```sudo cinf --pid [27681]```

**检查进程的 cgroup 层级**

```sudo cinf --cgroup [27681:3]```

**调试模式**

```sudo DEBUG=true cinf```

# SYNOPSIS

**cinf** [**--namespace** *id*] [**--pid** *pid*] [**--cgroup** *pid:hierarchy*]

# DESCRIPTION

**cinf**（container info）是一个用于查看 Linux 命名空间和 cgroups 的命令行工具。它适用于底层容器调试：列出命名空间 ID 及其进程数、用户和命令行；深入查看某个命名空间；列出某个 PID 的命名空间；以及检查进程的 cgroup 控制文件。

通常以 root（**sudo**）运行，以便看到所有命名空间。可从 GitHub 发布的 tarball 安装，或使用 Go 构建。

# PARAMETERS

*(no args)*

> 列出所有命名空间及其类型、进程数、用户和示例命令。

**--namespace** *id*

> 显示某个命名空间的详细信息。

**--pid** *pid*

> 列出某个进程的命名空间。

**--cgroup** *pid:hierarchy*

> 检查进程的某个 cgroup 层级（存在交互式/类 top 模式用于监控控制文件；参见 walkthrough 文档）。

**DEBUG=true**

> 用于输出详细调试消息的环境变量。

# CAVEATS

仅限 Linux。权限不足时许多命名空间不可见。内核 cgroup v1 与 v2 的布局差异会影响 **--cgroup** 路径，请与你的主机核对。上游仓库中附有配套的 walkthrough 文档。

# INSTALL

```aur: yay -S cinf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsns](/man/lsns)(1), [nsenter](/man/nsenter)(1), [unshare](/man/unshare)(1), [systemd-cgls](/man/systemd-cgls)(1)

# RESOURCES

```[Source code](https://github.com/mhausenblas/cinf)```

<!-- verified: 2026-07-19 -->
