# TAGLINE

管理 Pulumi ESC 环境和机密

# TLDR

**列出所有环境**

```pulumi env ls```

**打开并求值一个环境**

```pulumi env open [org/env]```

**从环境中获取指定值**

```pulumi env get [org/env] [key]```

**在环境中设置一个值**

```pulumi env set [org/env] [key] [value]```

**初始化新环境**

```pulumi env init [org/env]```

**编辑环境定义**

```pulumi env edit [org/env]```

**移除环境**

```pulumi env rm [org/env]```

**在加载环境变量后运行命令**

```pulumi env run [org/env] -- [command]```

# SYNOPSIS

**pulumi** **env** _command_ [_options_]

# SUBCOMMANDS

**ls**
> 列出环境。

**open** _name_
> 打开并对环境求值，显示解析后的值。

**get** _name_ _key_
> 从环境中获取指定的值。

**set** _name_ _key_ _value_
> 在环境中设置一个值。

**init** _name_
> 创建新环境。

**edit** _name_
> 在编辑器中编辑环境定义。

**rm** _name_
> 移除环境。

**run** _name_ **--** _command_
> 在设置好环境变量的情况下运行命令。

**version-tag** _name_
> 管理环境版本标签。

# DESCRIPTION

**pulumi env** 管理 Pulumi ESC（Environments, Secrets, and Configuration，环境、机密与配置）。ESC 提供跨堆栈和应用程序的配置与机密的集中管理。环境可以组合其他环境，并与 AWS Secrets Manager、HashiCorp Vault 等机密提供程序集成。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-config](/man/pulumi-config)(1), [pulumi-stack](/man/pulumi-stack)(1)
