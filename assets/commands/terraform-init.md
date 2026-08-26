# TAGLINE

初始化 Terraform 工作目录

# TLDR

**初始化当前目录**

```terraform init```

**初始化并升级** provider 和模块

```terraform init -upgrade```

**从文件加载 backend 配置进行初始化**

```terraform init -backend-config=[path/to/config.hcl]```

**初始化时不配置** backend

```terraform init -backend=false```

**初始化并将状态迁移**到新 backend

```terraform init -migrate-state```

**从模块源初始化**

```terraform init -from-module=[source]```

# SYNOPSIS

**terraform** **init** [_options_]

# PARAMETERS

**-upgrade**
> 将模块和插件升级到允许的最新版本。

**-backend** _true|false_
> 启用或禁用 backend 配置。默认为 **true**。

**-backend-config** _path_
> 通过文件路径或 key=value 键值对提供 backend 配置。可多次指定。

**-reconfigure**
> 重新配置 backend，忽略任何已保存的配置。不进行状态迁移。

**-migrate-state**
> 尝试通过交互式提示将现有状态复制到新 backend。

**-force-copy**
> 跳过迁移提示并自动复制状态。

**-from-module** _source_
> 在初始化前将模块复制到目标目录。

**-get** _true|false_
> 下载子模块。默认为 **true**。

**-plugin-dir** _path_
> 强制插件安装只从指定目录读取插件。

**-lockfile** _mode_
> 设置锁文件模式。使用 **readonly** 可校验校验和而不更新锁文件。

**-input** _true|false_
> 启用或禁用交互式提示。默认为 **true**。

**-lock** _true|false_
> 操作期间锁定状态文件。默认为 **true**。

**-lock-timeout** _duration_
> 重试获取状态锁的时长。默认为 **0s**。

**-no-color**
> 禁用输出中的颜色代码。

**-json**
> 启用机器可读的 JSON 输出。

# DESCRIPTION

**terraform init** 初始化包含 Terraform 配置文件的工作目录。这是编写新配置或从版本控制克隆现有配置后要运行的第一个命令。它可以安全地多次运行，不会删除现有配置或状态。

该命令执行几个初始化步骤：配置用于存储状态的 backend，下载并安装配置中声明的 provider 插件，以及下载配置中引用的子模块。每个步骤都可以用标志单独控制。

# CAVEATS

更换 backend 时，必须在 **-reconfigure**（丢弃旧状态）与 **-migrate-state**（把状态复制到新 backend）之间做出选择。当 backend 已变更而运行 init 时未带任一标志，会产生错误。**-plugin-dir** 选项会禁用默认的插件下载行为，因此该目录必须包含所有需要的 provider。

# HISTORY

**Terraform** 由 **Mitchell Hashimoto** 创建，于 **2014** 年由 **HashiCorp** 发布。init 命令的引入是为了管理日益复杂的 provider 插件和模块依赖。在 **Terraform 0.13**（2020 年）中，provider 插件管理被大幅重构，引入了依赖锁文件，并把公共 Terraform Registry 作为默认插件来源。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-plan](/man/terraform-plan)(1), [terraform-apply](/man/terraform-apply)(1)
