# TAGLINE

管理 Pulumi provider 插件

# TLDR

**列出已安装的插件**

```pulumi plugin ls```

**安装插件**

```pulumi plugin install resource [name] [version]```

**移除插件**

```pulumi plugin rm resource [name]```

**移除所有未使用的插件**

```pulumi plugin rm --all```

# SYNOPSIS

**pulumi** **plugin** _command_ [_options_]

# PARAMETERS

**ls**
> 列出已安装的插件。

**install** _kind_ _name_ _version_
> 安装插件。

**rm** _kind_ _name_
> 移除插件。

**--all**
> 移除所有插件。

**--yes**
> 跳过确认。

# DESCRIPTION

**pulumi plugin** 管理 Pulumi 插件。插件为云平台提供资源 provider。可为不同的云提供商和服务安装、更新和移除插件。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-install](/man/pulumi-install)(1)
