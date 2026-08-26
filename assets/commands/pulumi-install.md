# TAGLINE

安装 Pulumi 项目依赖和插件

# TLDR

**安装项目依赖和插件**

```pulumi install```

**不安装语言依赖**

```pulumi install --no-dependencies```

**不安装插件**

```pulumi install --no-plugins```

**即使插件已存在也重新安装所有插件**

```pulumi install --reinstall```

**以自定义并行度安装**

```pulumi install --parallel [8]```

**使用语言版本工具设置运行时**

```pulumi install --use-language-version-tools```

# SYNOPSIS

**pulumi** **install** [_options_]

# PARAMETERS

**--no-dependencies**
> 跳过安装语言依赖。

**--no-plugins**
> 跳过安装插件。

**--reinstall**
> 即使插件已存在也重新安装。

**--parallel** _int_
> 最大并发安装数（默认 4）。

**--use-language-version-tools**
> 使用语言版本工具来设置并安装语言运行时。

# DESCRIPTION

**pulumi install** 安装你的 Pulumi 程序或策略包所需的软件包和插件。如果 **Pulumi.yaml** 文件中包含 'packages' 部分，该命令会自动为所有声明的软件包安装 SDK。在克隆项目或更新依赖后运行此命令。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-plugin](/man/pulumi-plugin)(1), [pulumi-new](/man/pulumi-new)(1), [pulumi-up](/man/pulumi-up)(1)
