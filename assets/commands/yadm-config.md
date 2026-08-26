# TAGLINE

管理 yadm 配置项

# TLDR

**列出配置**

```yadm config --list```

**设置配置项**

```yadm config [name] [value]```

**设置本地类别**

```yadm config local.class [work]```

# SYNOPSIS

**yadm** **config** [_options_] [_name_] [_value_]

# PARAMETERS

**--list**
> 列出所有配置项。

**--get** _name_
> 获取配置项的值。

**--unset** _name_
> 移除配置项。

**local.class**
> 用于替代文件的系统类别。

**local.hostname**
> 覆盖主机名。

# DESCRIPTION

**yadm config** 管理 yadm 的配置。它为替代文件的选择设置本地系统属性，并封装 git config 来管理 yadm 特有的配置项。

# INSTALL

```pacman: sudo pacman -S yadm```

```apk: sudo apk add yadm```

```zypper: sudo zypper install yadm```

```brew: brew install yadm```

```nix: nix profile install nixpkgs#yadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yadm](/man/yadm)(1), [yadm-alt](/man/yadm-alt)(1)
