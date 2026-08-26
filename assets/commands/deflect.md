# TAGLINE

面向 Linux 基础设施的无代理、基于 SSH 的 DevOps 指挥中心

# TLDR

**从 PyPI 安装 Deflect One**

```pip install deflect-one```

**以生产模式启动仪表盘**

```deflect```

**启动演示模式**（无需 SSH 连接）

```deflect --demo```

**从源码检出目录直接运行**（手动安装依赖）

```pip install textual paramiko cryptography && python deflect.py```

**在运行中的 TUI 里打开 AI 聊天**，用自然语言执行命令

```[Ctrl+A]```

**在选中的主机上弹出交互式 SSH shell**

```[F2]```

# SYNOPSIS

**deflect** [_options_]

# PARAMETERS

**--demo**
> 以演示模式运行，不访问任何 SSH。适合评估或培训场景。

**-h**, **--help**
> 显示用法信息并退出。

# KEYBOARD SHORTCUTS

**Ctrl+D**
> Docker 管理面板。

**Ctrl+W**
> 防火墙（UFW / iptables）概览。

**Ctrl+F**
> SFTP 文件管理器。

**Ctrl+A**
> AI 聊天——用普通英语描述意图，由它翻译成 CLI / SSH / Bash 命令。

**Ctrl+L**
> 日志聚合视图。

**Ctrl+P**
> 进程监视器。

**F1**
> 帮助菜单。

**F2**
> 在选中的主机上打开交互式 SSH shell。

# DESCRIPTION

**Deflect One**（命令为 **deflect**）是一个单文件 Python TUI，能把 SSH 访问变成一个完整的 DevOps 平台。它将**可观测性**（CPU/内存/磁盘、进程表、日志聚合）、**安全性**（主动攻击检测、防火墙控制）和**运维能力**（Docker 管理、软件包安装、SFTP、部署）整合到一个界面中，且无需在被管理的主机上安装任何代理，只需 SSH 凭据即可。

可选的 LLM 后端为 **Ctrl+A** 聊天提供支持：操作者可以输入_"restart nginx on web-prod-02 and tail its error log"_ 之类的语句，Deflect One 会生成并执行对应的命令，并将输出直接显示出来。该工具基于 **Textual** 框架构建，使用 **paramiko** 处理 SSH、使用 **cryptography** 处理密钥。

# CONFIGURATION

主机、凭据以及可选的 AI 服务商密钥存储在首次运行时创建的本地配置文件中；所有 SSH 流量都由运行 Deflect One 的工作站直接发起，因此不会经过任何厂商的云端。

# CAVEATS

由于 Deflect One 会代替你执行任意远程命令（包括 AI 生成的命令），对 **Ctrl+A** 流程要保持与给代理授予 shell 访问权同等的警惕：确认前逐条审查命令，尤其是在生产主机上。本项目采用 MIT 许可证并**附带署名要求**；再分发前请先阅读 LICENSE 文件。

# HISTORY

**Deflect One** 由 **Volodymyr Frytskyy (WhitemanV)** 编写，作为重量级商业 DevOps 套件的轻量替代方案，让基础设施管理保持无代理且自包含。

# SEE ALSO

[ssh](/man/ssh)(1), [ansible](/man/ansible)(1), [htop](/man/htop)(1), [tmux](/man/tmux)(1), [lazydocker](/man/lazydocker)(1)
