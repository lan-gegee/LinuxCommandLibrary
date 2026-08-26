# TAGLINE

管理 npm 配置

# TLDR

**列出全部配置**

```npm config list```

**获取配置值**

```npm config get [registry]```

**设置配置值**

```npm config set [registry] [https://registry.npmjs.org/]```

**删除配置**

```npm config delete [key]```

**编辑配置文件**

```npm config edit```

**列出全部配置及默认值**

```npm config list -l```

**设置全局配置**

```npm config set [key] [value] -g```

# SYNOPSIS

**npm** **config** [_command_] [_options_]

# PARAMETERS

**set** _KEY=VALUE_
> 设置一个配置值。

**get** _KEY_
> 将配置值输出到 stdout。

**list**
> 显示所有配置。用 **-l** 显示默认值。用 **--json** 以 JSON 格式输出。

**delete** _KEY_
> 从所有配置文件中移除某个键。

**edit**
> 在编辑器中打开配置文件。用 **--global** 编辑全局配置。

**fix**
> 修复无效的配置项。

**-g**, **--global**
> 操作全局配置文件。

**--location** _user|global|project_
> 针对特定层级的配置。

# DESCRIPTION

**npm config** 管理多个层级的 npm 配置。它从命令行、环境变量和 .npmrc 文件（项目级、用户级和全局）读取设置。

配置文件是纯 ini 格式的 key = value 键值对列表。以 **npm_config_** 为前缀的环境变量也会被识别为配置项。

# CAVEATS

存在多个 .npmrc 位置，其优先顺序为：project > user > global > 默认值。凭据和令牌可能存储在 .npmrc 文件中。

# HISTORY

npm config 是用于自定义 npm 行为的**配置管理**系统。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npmrc](/man/npmrc)(5)
