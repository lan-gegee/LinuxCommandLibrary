# TAGLINE

管理 Pixi 项目设置和支持的平台

# TLDR

**添加平台**

```pixi project platform add [platform]```

**列出已配置的平台**

```pixi project platform list```

**添加频道**

```pixi project channel add [channel]```

**提升项目版本号**

```pixi project version bump [major|minor|patch]```

**设置项目描述**

```pixi project description set "[description]"```

**将环境导出为 conda-env YAML**

```pixi project export conda-environment [path/to/env.yml]```

# SYNOPSIS

**pixi** **project** _subcommand_ [_options_]

# PARAMETERS

**channel** _cmd_
> 管理项目频道（add、list、remove）。

**platform** _cmd_
> 管理支持的平台（add、list、remove）。

**description** _cmd_
> 获取或设置项目描述。

**environment** _cmd_
> 管理 pixi 环境（add、list、remove）。

**export** _cmd_
> 将项目导出为其他格式（conda-environment、conda-explicit-spec）。

**name** _cmd_
> 获取或设置项目名称。

**version** _cmd_
> 管理项目版本（get、set、bump、major、minor、patch）。

# DESCRIPTION

**pixi project** 管理存储在 **pixi.toml**（或 **pyproject.toml** 的 `[tool.pixi]` 部分）中的 Pixi 项目配置。其子命令用于配置频道、支持的平台、环境以及项目的名称/描述/版本，还可以将清单导出为 conda 兼容格式。

使用 **pixi init** 可创建新项目；**pixi project** 则操作当前工作目录中已有的清单。

# INSTALL

```pacman: sudo pacman -S pixi```

```brew: brew install pixi```

```nix: nix profile install nixpkgs#pixi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pixi](/man/pixi)(1), [pixi-config](/man/pixi-config)(1)
