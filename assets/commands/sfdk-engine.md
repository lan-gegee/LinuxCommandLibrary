# TAGLINE

管理 Sailfish SDK 构建引擎

# TLDR

**启动 SDK 引擎**

```sfdk engine start```

**停止 SDK 引擎**

```sfdk engine stop```

**显示引擎状态**

```sfdk engine status```

**在引擎内部运行命令**

```sfdk engine exec [command]```

# SYNOPSIS

**sfdk engine** _command_ [_options_]

# PARAMETERS

**start**
> 启动构建引擎虚拟机。

**stop**
> 停止构建引擎虚拟机。

**status**
> 显示引擎是否正在运行。

**exec** _command_
> 在运行中的引擎内执行命令。

# DESCRIPTION

**sfdk engine** 管理 Sailfish SDK 构建引擎，该引擎以虚拟机形式运行，提供 Sailfish OS 构建环境。必须先启动引擎才能使用其他 `sfdk` 构建命令，通常会在多次构建之间保持其运行。

# CAVEATS

构建引擎是一台虚拟机，需要可用的虚拟化后端（根据 SDK 变体不同为 VirtualBox 或 Docker）。首次启动引擎可能需要数秒钟。

# SEE ALSO

[sfdk](/man/sfdk)(1), [sfdk-build-shell](/man/sfdk-build-shell)(1)
