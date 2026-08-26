# TAGLINE

从终端管理 AgentBox 云沙箱与模板

# TLDR

通过 npm 全局**安装** CLI

```npm install -g agentbox-cli```

向 AgentBox 云**进行身份验证**

```agentbox auth login```

**列出**活动与暂停状态的沙箱

```agentbox sandbox list```

按数量上限**列出运行中的沙箱**

```agentbox sandbox list --state running --limit [25]```

按元数据键值对**筛选沙箱**

```agentbox sandbox list --metadata [env=prod,team=ml]```

按 ID **终止指定沙箱**

```agentbox sandbox kill [sandbox_id]```

**终止所有运行中的沙箱**

```agentbox sandbox kill --all```

**搭建并构建**自定义沙箱模板

```agentbox template create [my-template]; agentbox template build```

# SYNOPSIS

**agentbox** _command_ [_subcommand_] [_flags_]

# PARAMETERS

**auth login**
> 让 CLI 向 AgentBox 云完成身份验证，并在本地持久化凭据。

**auth logout**
> 从本地机器上删除已存储的凭据。

**sandbox list**
> 列出已认证账户可见的沙箱。

**sandbox kill** _id_
> 终止给定 _id_ 的沙箱。沙箱内的数据会被丢弃。

**sandbox kill --all**
> 终止该账户当前正在运行的每一个沙箱。

**template create** _name_
> 在当前目录中搭建一个新的自定义沙箱模板骨架。

**template build**
> 把当前目录定义的模板构建为可部署的镜像。

**--state** _states_
> 以逗号分隔的状态（**running**、**paused**）过滤 **sandbox list** 结果。

**--metadata** _key=value,..._
> 按元数据键值对过滤 **sandbox list** 结果。

**--limit** _N_
> 把 **sandbox list** 结果限制为 _N_ 条（默认 **10**）。

# DESCRIPTION

**agentbox** 是 **AgentBox.cloud** 的命令行客户端。AgentBox.cloud 是一项托管服务，在相互隔离的 x86 和 Android 云沙箱中运行 AI 代理。该 CLI 具备与 AgentBox Web 控制台对等的能力：为开发者完成认证、列出并终止运行中的沙箱，以及管理决定沙箱如何供给的自定义模板镜像。

该 CLI 通常与 AgentBox 的 **Python** 和 **JavaScript** SDK 配合使用。SDK 从应用代码中以编程方式创建沙箱；CLI 则是配套的管理工具，可用于审计、清理以及编写可复用的沙箱模板，全程无需离开终端。

**agentbox template create** 会生成一个目录，内含模板清单和一份类似 Dockerfile 的配方。**agentbox template build** 把该目录打包成一个镜像，后续的 SDK 调用可以按名称引用它，从而为代理代码提供一致且可复现的初始环境。

# CAVEATS

需要 **Node.js** 运行时（通过 **npm install -g agentbox-cli** 安装）和一个有效的 **AgentBox.cloud** 账户；它不通过 **apt**、**brew** 或 **pacman** 分发。**agentbox sandbox kill** 是破坏性操作——沙箱内的任何数据都会永久丢失。名称 **agentbox** 与 GitHub 上若干无关的纯本地 Docker 项目（例如 **rcarmo/agentbox**、**fletchgqc/agentbox**）重名，它们并不是同一个工具。

# HISTORY

AgentBox 诞生于 **2024–2025** 年的 AI 代理沙箱服务浪潮之中，同期项目还有 **E2B**、**Modal** 和 **Daytona** 等。这类服务基于轻量级虚拟化，让 AI 生成的代码能够在远离用户机器的地方安全执行。该 CLI 以 **agentbox-cli** 之名发布在 **npm** 上，文档位于 **agentbox.cloud**。

# SEE ALSO

[docker](/man/docker)(1), [npm](/man/npm)(1)
