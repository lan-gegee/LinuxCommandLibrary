# TAGLINE

管理 Homebrew 软件包的后台服务

# TLDR

**列出所有服务**

```brew services list```

**启动服务**

```brew services start [postgresql]```

**停止服务**

```brew services stop [postgresql]```

**重启服务**

```brew services restart [postgresql]```

在前台**运行服务**

```brew services run [postgresql]```

**停止所有服务**

```brew services stop --all```

清理未使用的服务

```brew services cleanup```

# SYNOPSIS

**brew services** [_subcommand_] [_formula_] [_options_]

# DESCRIPTION

**brew services** 管理已安装 Homebrew formula 的后台服务。在 macOS 上，它通过 LaunchAgent plist 文件使用 launchd；在 Linux 上，它使用 systemd 用户单元。

用此命令配置的服务会在用户登录时自动启动。

# SUBCOMMANDS

**list**
> 列出所有受管服务及其状态。

**start** _formula_
> 启动服务并配置为登录时自启。

**stop** _formula_
> 停止服务并取消登录自启。

**restart** _formula_
> 重启服务。

**run** _formula_
> 在前台运行服务（不配置登录自启）。

**cleanup**
> 移除不再使用的服务文件。

**info** _formula_
> 显示服务信息。

# PARAMETERS

**--all**
> 应用于所有服务。

**--json**
> 以 JSON 格式输出。

**--file** _path_
> 使用自定义服务文件。

# SERVICE FILES

**macOS**
> ~/Library/LaunchAgents/homebrew.mxcl.<formula>.plist

**Linux**
> ~/.config/systemd/user/homebrew-<formula>.service

# CAVEATS

在 Linux 上需要正在运行的用户 systemd 实例。常见用途包括数据库（postgresql、mysql）、缓存（redis）和 Web 服务器。开发场景建议使用 **run**，以避免写入启动配置。

# HISTORY

随 Homebrew 0.9.9（2014 年 2 月）推出，最初用于支持 macOS 的 launchd。Linux/systemd 支持通过 Linuxbrew 引入，并于 2020 年前后并入 Homebrew 核心。

# SEE ALSO

[brew](/man/brew)(1), [launchctl](/man/launchctl)(1), [systemctl](/man/systemctl)(1)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-22 -->
