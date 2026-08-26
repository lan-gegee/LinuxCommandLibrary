# TAGLINE

管理 DVC 配置设置

# TLDR

**设置一个配置值**

```dvc config [core.remote] [myremote]```

**读取一个配置值**

```dvc config [core.remote]```

**设置一个全局配置值**

```dvc config --global [core.autostage] true```

**设置一个项目级（本地）配置值**

```dvc config --local [core.remote] [myremote]```

**列出所有配置项**

```dvc config --list```

**取消一个配置值**

```dvc config --unset [core.remote]```

# SYNOPSIS

**dvc config** [_options_] [_name_] [_value_]

# PARAMETERS

_NAME_
> 配置键。

_VALUE_
> 配置值。

**--global**
> 使用全局配置。

**--system**
> 使用系统配置。

**--local**
> 使用项目级配置（.dvc/config.local，被 Git 忽略）。

**--project**
> 使用项目级配置（.dvc/config，由 Git 跟踪）。

**--list**, **-l**
> 列出所有配置项。

**--unset**
> 移除一个配置项。

**-h**, **--help**
> 显示帮助信息。

# CONFIGURATION

**.dvc/config**
> 仓库级 DVC 配置文件。

**~/.config/dvc/config**
> 全局用户配置文件。

# DESCRIPTION

**dvc config** 在项目、本地、全局和系统级别管理 DVC 配置。配置控制多种行为，包括默认远程存储、缓存和自动化设置。

配置的优先级从高到低依次为：本地（被 Git 忽略）、项目（由 Git 跟踪）、全局（用户）、系统。常见的配置节包括 `core`（remote、autostage）、`cache`（type、dir）和 `remote`（url、credentials）。

将 `core.autostage` 设为 true 可自动将 .dvc 文件的更改暂存到 Git，减少手动操作步骤。默认远程存储通过 `core.remote` 设置。

# CAVEATS

某些选项需要仓库上下文。无效的键可能仍会被接受。修改系统配置需要相应的权限。

# HISTORY

dvc config 遵循 **Git config** 的约定，为 DVC 设置提供熟悉的配置管理方式。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc](/man/dvc)(1), [dvc-init](/man/dvc-init)(1), [git-config](/man/git-config)(1)
