# TAGLINE

Go 的旧版依赖管理工具

# TLDR

**为项目初始化依赖管理**

```dep init```

**添加依赖**

```dep ensure -add [github.com/pkg/errors]```

**更新全部依赖**

```dep ensure -update```

**更新指定依赖**

```dep ensure -update [github.com/pkg/errors]```

**查看依赖状态**

```dep status```

**可视化依赖树**

```dep status -dot | dot -Tpng -o deps.png```

# SYNOPSIS

**dep** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：init、ensure、status、prune、check。

**init**
> 用 dep 初始化新项目。

**ensure**
> 确保依赖得到满足。

**-add** _PACKAGE_
> 添加一个依赖。

**-update** [_PACKAGE_]
> 更新依赖。

**status**
> 显示依赖状态。

**prune**
> 移除未使用的依赖。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dep** 是 Go modules 成为标准之前 Go 的官方依赖管理工具。它通过 Gopkg.toml 和 Gopkg.lock 文件管理项目依赖，确保构建可复现。

该工具负责解析传递依赖、处理版本约束，并将依赖 vendor 到 vendor 目录。ensure 命令是添加、更新和同步依赖的主要入口。

dep 采用语义化导入版本控制（semantic import versioning），支持多种版本约束语法，包括 semver 区间、分支和修订版本。

# CONFIGURATION

**Gopkg.toml**
> 项目依赖约束和元数据配置。

**Gopkg.lock**
> 生成的锁定文件，记录确切的依赖版本和哈希值。

# CAVEATS

在 Go 1.11 及以上版本中已被 Go modules（go mod）取代。新项目应使用 Go modules。从 dep 到 modules 有官方迁移路径。仅支持位于 GOPATH 内的项目。

# HISTORY

dep 由 Go 社区开发，于 **2016 年**发布，是官方的依赖管理试验方案。它在 Go 1.11（**2018 年**）引入 Go modules 之前一直充当过渡方案，此后 dep 进入维护模式。

# INSTALL

```aur: yay -S dep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1)
