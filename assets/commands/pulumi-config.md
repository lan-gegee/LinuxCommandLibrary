# TAGLINE

管理 Pulumi 堆栈配置值

# TLDR

**设置配置值**

```pulumi config set [key] [value]```

**设置机密值**

```pulumi config set --secret [key] [value]```

**获取配置值**

```pulumi config get [key]```

**列出全部配置**

```pulumi config```

**删除配置**

```pulumi config rm [key]```

# SYNOPSIS

**pulumi** **config** [_command_] [_options_]

# PARAMETERS

**set** _key_ _value_
> 设置配置值。

**get** _key_
> 获取配置值。

**rm** _key_
> 删除配置。

**refresh**
> 从状态中更新配置。

**--secret**
> 加密该值。

**--plaintext**
> 以明文存储。

**-s**, **--stack** _name_
> 目标堆栈。

**--json**
> 以 JSON 格式输出。

# DESCRIPTION

**pulumi config** 管理堆栈的配置值。配置包括云区域、实例规格和机密（secrets）等参数。机密在状态文件中是加密存储的。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-stack](/man/pulumi-stack)(1)
