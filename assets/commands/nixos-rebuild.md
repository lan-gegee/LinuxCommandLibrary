# TAGLINE

通过构建新配置来重新配置 NixOS 系统

# TLDR

**构建并切换**到新配置（设为启动默认项）

```sudo nixos-rebuild switch```

使用**自定义 profile 名称**构建并切换

```sudo nixos-rebuild switch -p [name]```

构建、切换并**安装更新**

```sudo nixos-rebuild switch --upgrade```

**回滚**到上一个 generation

```sudo nixos-rebuild switch --rollback```

构建并设为**启动默认项**但不激活

```sudo nixos-rebuild boot```

构建并**测试**但不创建启动项

```sudo nixos-rebuild test```

构建配置并在**虚拟机**中运行

```sudo nixos-rebuild build-vm```

**列出**可用的 generation

```nixos-rebuild list-generations```

# SYNOPSIS

**nixos-rebuild** [**switch**|**boot**|**test**|**build**|**build-vm**] [**--upgrade**] [**--rollback**] [**-p** _name_]

# COMMANDS

**switch**
> 构建并激活，同时设为启动默认项。

**boot**
> 构建并设为启动默认项，但不激活。

**test**
> 构建并激活，但不创建启动项。

**build**
> 只构建配置，不激活。

**build-vm**
> 构建配置并在虚拟机中打开。

**dry-build**
> 显示将会构建的内容。

**dry-activate**
> 显示激活时会发生哪些变化。

**list-generations**
> 列出可用的系统 generation。

# PARAMETERS

**--upgrade**
> 在构建前更新 nixpkgs channel。

**--rollback**
> 回滚到上一个 generation。

**-p, --profile-name _name_**
> 启动项的名称。

**--flake _uri_**
> 从 flake 引用构建。

**--no-build-nix**
> 切换时不重新构建 Nix。

**--fast**
> 跳过重新构建 Nix 和文档。

**--show-trace**
> 显示详细的错误追踪信息。

# DESCRIPTION

**nixos-rebuild** 通过从 /etc/nixos/configuration.nix 构建新配置来重新配置 NixOS 系统，并可选择将其激活。NixOS 采用声明式配置模型，整个系统都用 Nix 表达式描述。

每次构建都会创建一个新的 generation，可以在启动时选择。这样即使出现问题，也能安全地回滚到之前正常工作的配置。

# CAVEATS

大多数操作需要 root 权限。配置错误会导致构建无法完成。较大的变更可能需要大量的下载和构建时间。switch 命令会重启发生变化的服务。

# HISTORY

**nixos-rebuild** 是基于 Nix 软件包管理器的 Linux 发行版 **NixOS** 的一部分。NixOS 由 Eelco Dolstra 创建，于 2003 年首次发布。它开创了声明式系统配置以及支持回滚的原子升级。

# SEE ALSO

[nix](/man/nix)(1), [nix-env](/man/nix-env)(1), [nix-channel](/man/nix-channel)(1)
