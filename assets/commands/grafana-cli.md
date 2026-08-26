# TAGLINE

Grafana 插件与管理工具

# TLDR

**安装插件**

```grafana-cli plugins install [plugin-id]```

**列出已安装的插件**

```grafana-cli plugins ls```

**更新所有已安装的插件**

```grafana-cli plugins update-all```

**更新插件**

```grafana-cli plugins update [plugin-id]```

**移除插件**

```grafana-cli plugins remove [plugin-id]```

**列出远程仓库中可用的插件**

```grafana-cli plugins list-remote```

**重置管理员密码**

```grafana-cli admin reset-admin-password [newpassword]```

# SYNOPSIS

**grafana-cli** [_global-options_] _command_ _subcommand_ [_args_]

# COMMANDS

**plugins install** _ID_ [_VERSION_]
> 安装插件，可选固定到特定版本。

**plugins ls**
> 列出已安装的插件。

**plugins update** _ID_
> 将单个插件更新到最新的兼容版本。

**plugins update-all**
> 更新所有已安装的插件。

**plugins remove** _ID_
> 移除已安装的插件。

**plugins list-remote**
> 列出所配置仓库中所有可用的插件。

**plugins list-versions** _ID_
> 列出给定插件的所有可用版本。

**admin reset-admin-password** _PASSWORD_
> 重置内置管理员账户的密码。

**admin data-migration encrypt-datasource-passwords**
> 将明文数据源密码迁移到 secureJsonData 字段。

# PARAMETERS

**--config** _FILE_
> 使用替代的 **grafana.ini** 配置文件。

**--homepath** _DIR_
> Grafana 主目录，用于定位配置和插件路径。

**--pluginsDir** _DIR_
> 覆盖插件安装目录。

**--pluginUrl** _URL_
> 从自定义 URL（zip）安装插件而不是从插件仓库安装。

**--repo** _URL_
> 使用不同的插件仓库。

**--insecure**
> 下载插件时跳过 TLS 验证。

**-d**, **--debug**
> 启用调试输出。

**-v**, **--version**
> 显示 CLI 版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grafana-cli** 管理 Grafana 插件和管理任务。它可以从 Grafana 插件仓库安装、更新和移除可视化插件与数据源。

该工具独立于 Grafana 服务器处理插件生命周期管理。它还提供密码重置和数据库迁移等管理命令。

# CAVEATS

需要相应的权限。可能需要重启 Grafana。插件兼容性因版本而异。

# HISTORY

grafana-cli 与 **Grafana** 一同开发，为该可视化平台提供命令行管理能力。

# INSTALL

```dnf: sudo dnf install grafana```

```pacman: sudo pacman -S grafana```

```apk: sudo apk add grafana```

```zypper: sudo zypper install grafana```

```brew: brew install grafana```

```nix: nix profile install nixpkgs#grafana```

<!-- packages: 2026-07-22 -->

# SEE ALSO
