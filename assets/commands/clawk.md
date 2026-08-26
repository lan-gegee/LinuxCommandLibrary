# TAGLINE

面向 AI 编程代理的、用后即弃且限制网络的 Linux 虚拟机

# TLDR

为当前项目**启动**沙箱并挂载 Claude

```clawk```

在同一沙箱中**附加**一个 shell 或另一个代理

```clawk run shell
clawk run codex```

**停止**虚拟机（仓库与代理状态会保留）

```clawk down```

之后重新**接入**（若已停止则自动启动）

```clawk attach```

**销毁**这个一次性虚拟机（宿主机侧的对话会保留）

```clawk destroy```

**允许**出站主机或**转发**客户机端口

```clawk network allow [sandbox] [api.example.com]
clawk forward add [sandbox] [3000]```

# SYNOPSIS

**clawk** [_command_] [_options_] [_args_]

# DESCRIPTION

**clawk** 在一次性的 Linux microVM 中运行编程代理（Claude Code、Codex、OpenCode 或普通 shell），而不是直接在宿主机上运行。项目目录被挂载到客户机中；出站网络访问采用允许列表机制；主机密钥和文件系统的其余部分都留在虚拟机之外。

在 macOS（Apple 芯片，macOS 14+）上它使用 Virtualization.framework；通过 Firecracker 的 Linux 支持尚处于实验阶段。首次启动时基于 OCI 镜像构建 rootfs；后续启动则是快速的写时复制克隆。空闲的虚拟机可以释放内存并挂起。

可选的 **clawk.mod** 项目配置可设置 CPU、内存、镜像、网络许可、端口转发、环境变量和钩子。工单模式（**clawk work**）可以创建多仓库工作树，并通过 **clawk pr** 打开相互协调的 PR。

# PARAMETERS

**run** _agent_
> 启动或复用沙箱，并附加 **claude**、**codex**、**opencode** 或 **shell**

**attach** / **down** / **up** / **destroy**
> 生命周期管理：重新接入、停止、启动或移除虚拟机

**network** **allow**|**denials** ...
> 管理每个沙箱的出站允许列表，并查看被阻止的目标地址

**forward** **add** ...
> 在 localhost 上发布一个客户机端口

**list** / **status**
> 列出沙箱或显示状态（脚本可用 **--json**）

**--safe**
> 附加时不使用代理的权限绕过选项

# CAVEATS

1.0 之前的软件；应预期破坏性变更。主要支持 macOS Apple 芯片。任何被挂载或列入允许列表的内容都会暴露给代理（包括通过转发的 ssh-agent 执行 git push）。虚拟机监视器逃逸不在防护范围内。

# SEE ALSO

[docker](/man/docker)(1), [lima](/man/lima)(1)

# RESOURCES

```[Source code](https://github.com/clawkwork/clawk)```

```[Documentation](https://github.com/clawkwork/clawk/tree/main/docs)```

<!-- verified: 2026-07-14 -->
