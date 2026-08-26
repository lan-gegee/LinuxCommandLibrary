# TAGLINE

管理 PlatformIO 库（已废弃，请使用 pio pkg）

# TLDR

**搜索库**

```pio lib search [mqtt]```

**安装库**

```pio lib install [PubSubClient]```

**安装特定版本**

```pio lib install "[email protected]"```

**列出已安装的库**

```pio lib list```

**卸载库**

```pio lib uninstall [PubSubClient]```

**更新所有已安装的库**

```pio lib update```

# SYNOPSIS

**pio lib** _command_ [_options_]

# PARAMETERS

**search** _query_
> 搜索库注册表。

**install** _library_
> 安装库。

**uninstall** _library_
> 移除库。

**list**
> 列出已安装的库。

**update**
> 更新已安装的库。

**show** _library_
> 显示库详情。

**builtin**
> 显示内置库。

**register**
> 在 PlatformIO 注册表中注册一个库。

**stats**
> 显示库统计信息。

**-d**, **--storage-dir** _dir_
> 管理自定义库存储目录。

**-g**, **--global**
> 操作全局 PlatformIO 库存储。

**-e**, **--environment** _name_
> 针对特定的项目构建环境。

# DESCRIPTION

**pio lib** 用于管理 PlatformIO 库。可以从 PlatformIO 注册表搜索、安装和更新库，并自动处理嵌入式项目的依赖。此命令自 PlatformIO 6.0 起已废弃，请改用 **pio pkg**。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-pkg](/man/pio-pkg)(1), [pio-init](/man/pio-init)(1), [pio-run](/man/pio-run)(1), [pio](/man/pio)(1)
