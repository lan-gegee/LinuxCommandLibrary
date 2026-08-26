# TAGLINE

检查 NixOS 配置值，显示已设置了哪些选项及其当前值

# TLDR

列出一个给定选项键的所有**子键**

```nixos-option [option_key]```

列出当前的**启动内核模块**

```nixos-option boot.kernelModules```

列出特定用户的**授权密钥**

```nixos-option users.users.[username].openssh.authorizedKeys.keys```

列出所有**远程构建机**

```nixos-option nix.buildMachines```

列出**另一个 NixOS 配置**下的子键

```NIXOS_CONFIG=[path/to/configuration.nix] nixos-option [option_key]```

递归显示某个用户的**全部值**

```nixos-option -r users.users.[user]```

# SYNOPSIS

**nixos-option** [_options_] _option_path_

# PARAMETERS

**-r, --recursive**
> 递归显示所有嵌套的值

**_option_path_**
> 以点号分隔的配置选项路径

**NIXOS_CONFIG**
> 用于指定其他配置文件的环境变量

# DESCRIPTION

**nixos-option** 检查 NixOS 的配置值，显示设置了哪些选项以及它们的当前值。它使用点号表示法（例如 services.nginx.enable）遍历层次化的 NixOS 模块系统。

该工具会显示配置选项的类型、默认值、描述和当前值。对于容器类选项（如 services.* 或 users.*），它会列出可用的子键。

这对于探索可用的 NixOS 选项、调试配置问题，以及理解由 Nix 配置定义的系统当前状态很有帮助。

# CAVEATS

会对 Nix 配置进行求值，在复杂系统上可能耗时较长。只显示来自 NixOS 模块系统的选项；无法检查任意的 Nix 表达式。某些动态选项可能无法完全发现。

# INSTALL

```nix: nix profile install nixpkgs#nixos-option```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nixos-rebuild](/man/nixos-rebuild)(8), [nix-env](/man/nix-env)(1), [configuration.nix](/man/configuration.nix)(5)
