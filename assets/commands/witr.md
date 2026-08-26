# TAGLINE

解释进程、端口或容器为何在运行

# TLDR

按名称**解释**某个进程

```witr [name]```

**解释**监听某端口的是什么

```witr --port [port]```

按 PID **解释**某个进程

```witr --pid [pid]```

仅显示祖先链

```witr [name] --short```

以树状显示祖先链

```witr --pid [pid] --tree```

按名称或镜像**查找容器**

```witr --container [name]```

**打开交互式 TUI** 仪表盘

```witr -i```

# SYNOPSIS

**witr** [*options*] [*name*...]

# DESCRIPTION

**witr**（"why is this running?"，为什么它在运行？）回答运行中进程背后的因果问题：它从何而来、如何被启动，以及是哪条由监督者、shell、服务或容器组成的链条让它保持存活。与单独使用 **ps**、**lsof** 或 **systemctl** 不同，它把这些层面关联成一份人类可读的解释（或树状 / JSON 视图）。

目标可以是进程名（默认子串匹配）、PID、端口、打开的文件或容器。容器查找涵盖 Docker、Podman、nerdctl、Kubernetes/crictl、Incus、LXC/LXD 和 FreeBSD jail。不带目标或带 **-i** 时，**witr** 会打开交互式 TUI。

# PARAMETERS

**-p**, **--pid** *pid*

> 查找一个或多个进程 ID（可重复）。

**-o**, **--port** *port*

> 查找绑定到端口的进程（可重复）。

**-f**, **--file** *path*

> 查找持有某个打开文件的进程（可重复）。

**-c**, **--container** *name*

> 按名称、镜像、命令或 compose 标签查找容器（可重复）。

**-x**, **--exact**

> 精确匹配进程名（禁用子串搜索）。

**-s**, **--short**

> 只打印祖先链。

**-t**, **--tree**

> 以树状打印祖先链（包括目标的子进程）。

**-i**, **--interactive**

> 交互式 TUI 模式。

**--json**

> 输出机器可读的 JSON。

**--env**

> 包含进程的环境变量。

**--verbose**

> 扩展的进程信息（挂载、网络，容器的 compose 元数据）。

**--no-color**

> 禁用彩色输出。

**--warnings**

> 仅显示警告。

**-h**, **--help**

> 显示帮助。

**-v**, **--version**

> 显示版本。

# CAVEATS

某些细节（尤其是容器和远程运行时）需要相应的权限和已安装的客户端工具。子串名称匹配可能返回多个结果；请用 **--pid** 或 **--exact** 重新运行。输出质量取决于本地进程树和监督者所暴露的信息。

# INSTALL

```brew: brew install witr```

```nix: nix profile install nixpkgs#witr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ps](/man/ps)(1), [lsof](/man/lsof)(1), [ss](/man/ss)(8), [systemctl](/man/systemctl)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/pranshuparmar/witr)```

<!-- verified: 2026-07-19 -->
