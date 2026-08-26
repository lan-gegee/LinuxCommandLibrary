# TAGLINE

以代码方式运行流水线的可编程 CI/CD 引擎

# TLDR

在当前目录**初始化**新的 Dagger 模块

```dagger init --sdk=[go|python|typescript]```

**调用**当前模块中定义的函数

```dagger call [function_name] --[arg]=[value]```

**开发**模块（编辑 dagger.json 后重新生成 SDK 绑定）

```dagger develop```

**安装**另一个模块作为依赖

```dagger install [github.com/owner/repo@version]```

在模块上下文中**打开**交互式 Shell

```dagger```

**运行**外部命令并挂载 Dagger 引擎

```dagger run -- [go test ./...]```

用 GraphQL **直接查询** Dagger API

```dagger query < [query.graphql]```

# SYNOPSIS

**dagger** [_global-options_] _command_ [_command-options_] [_arguments_]

# PARAMETERS

**call**
> 调用当前模块中的函数；参数以 **--flag=value** 形式传递，结果以流的形式返回。

**init**
> 在当前目录搭建新模块。需要 **--sdk** 来选择语言。

**develop**
> 编辑 **dagger.json** 或添加依赖后重新生成代码绑定。

**install**
> 添加一个模块引用（本地路径或远程 Git URL）作为依赖。

**run**
> 以临时 Dagger 引擎会话执行任意命令，并通过 **DAGGER_SESSION_PORT** 暴露引擎。

**query**
> 向 Dagger 引擎发送原始 GraphQL 查询（从文件或 stdin 读取）。

**login** / **logout**
> 针对 Dagger Cloud 进行身份验证，以获取流水线追踪和缓存功能。

**-m**, **--mod** _REF_
> 使用远程模块而非本地模块（如 **github.com/dagger/dagger/ci**）。

**--progress** _MODE_
> 进度 UI：**auto**、**plain** 或 **tty**。

**--silent**
> 完全隐藏进度输出。

**-v**, **--debug**
> 详细 / 调试日志。

# DESCRIPTION

**dagger** 是一个可移植构建引擎的 CLI，它以代码而非 YAML 的方式执行流水线。每条流水线都通过相应的 Dagger SDK 用 **Go**、**Python**、**TypeScript**、**Java**、**PHP** 或 **Elixir** 表达为函数。函数接受类型化输入（目录、机密、服务、基本类型），描述一张容器化操作图，并返回类型化的输出。

引擎可在本地运行于 Docker、Podman 或任何兼容 OCI 的运行时上，也可以完全相同地运行在任何 CI 中（GitHub Actions、GitLab CI、Jenkins、CircleCI、Azure Pipelines、Buildkite）。由于每个步骤都按内容寻址并缓存，重复调用会复用先前的结果，让本地迭代与 CI 运行一样快。

**dagger call** 是主要入口：它定位模块（由 **dagger.json** 定义）、用提供的标志调用所请求的函数，并以流的方式返回结果。模块可以从本地路径或 Git URL 组合其他模块，从而在项目和组织间实现可复用的构建单元。

# MODULE LAYOUT

典型的模块目录包含：

```
dagger.json     # module manifest (sdk, dependencies)
.dagger/        # generated SDK bindings (do not edit)
main.<ext>      # user-authored functions
```

编辑 **dagger.json** 或任何函数签名后，请运行 **dagger develop** 重新生成绑定。

# CAVEATS

需要一个可用的 OCI 运行时（Docker、Podman、nerdctl）；首次调用时 Dagger 会启动自己的引擎容器。函数参数是强类型且区分大小写的；**--myArg** 与 **--my-arg** 不可互换。固定到某个 Git ref 的模块在上游 SDK 变更其接口后可能在 **dagger develop** 时出问题。缓存放在一个名为 **dagger-engine-*** 的 Docker 卷里，可能变得很大；可用 **docker volume rm** 清理。

# HISTORY

**Dagger** 由 **Solomon Hykes**（Docker 的创造者）、**Sam Alba** 和 **Andrea Luzzardi** 创立，于 **2022 年 3 月**公开发布。最初的 0.x 版本通过 **CUE** 驱动流水线。**2023 年初**，项目转向多语言 **module** 模型并提供原生语言 SDK，同时 **dagger call** 取代了旧的 **dagger do** 入口。**2023 年末**发布的 **0.9** 版本将模块系统作为默认方式。

# INSTALL

```pacman: sudo pacman -S dagger```

```brew: brew install dagger```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [podman](/man/podman)(1), [act](/man/act)(1), [buildah](/man/buildah)(1)
