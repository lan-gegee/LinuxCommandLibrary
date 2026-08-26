# TAGLINE

管理 Pixi 软件包管理器的配置

# TLDR

**显示配置**

```pixi config list```

**设置配置值**

```pixi config set [key] [value]```

**获取配置值**

```pixi config get [key]```

**编辑配置文件**

```pixi config edit```

# SYNOPSIS

**pixi** **config** _command_ [_options_]

# PARAMETERS

**list**
> 显示当前配置。

**get** _key_
> 获取特定的配置值。

**set** _key_ _value_
> 设置配置值。

**edit**
> 在编辑器中打开配置文件。

**--global**
> 使用全局配置。

**--local**
> 使用项目配置。

# DESCRIPTION

**pixi config** 在全局和项目层级管理 Pixi 软件包管理器的配置。它提供命令行界面来读取、写入和编辑设置，无需手动编辑 TOML 文件。

配置控制默认频道、身份验证令牌、缓存目录以及其他 Pixi 行为。全局设置对所有项目生效，而 pixi.toml 中的本地设置会按项目覆盖它们。

# CONFIGURATION

**~/.pixi/config.toml**
> 所有 Pixi 操作的全局配置文件。

**pixi.toml**
> 位于项目根目录的项目级配置文件。

# INSTALL

```pacman: sudo pacman -S pixi```

```brew: brew install pixi```

```nix: nix profile install nixpkgs#pixi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pixi](/man/pixi)(1), [conda](/man/conda)(1)
