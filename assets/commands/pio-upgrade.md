# TAGLINE

将 PlatformIO Core 升级到最新版本

# TLDR

**升级** PlatformIO Core 到最新 **stable（稳定）版本**

```pio upgrade```

**升级**到最新 **development（开发）版本**

```pio upgrade --dev```

# SYNOPSIS

**pio upgrade** [_options_]

# PARAMETERS

**--dev**
> 升级到最新的开发版本而非稳定版。可在正式发布前体验新功能，但稳定性可能较差。

# DESCRIPTION

**pio upgrade** 用于检查并将 PlatformIO Core CLI 工具本身升级到最新发布版本。默认安装最新的稳定版本。使用 **--dev** 可安装开发版本，以便在官方正式发布前测试新功能。

与更新项目平台软件包和库的 **pio update** 不同，**pio upgrade** 针对的是底层的 PlatformIO Core 安装。

# CAVEATS

需要联网以下载更新。根据安装方式的不同（例如系统级的 pip install），可能需要提升权限。升级后，请重启所有正在运行的 PlatformIO 进程或 IDE 集成。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-update](/man/pio-update)(1), [pio](/man/pio)(1), [pip](/man/pip)(1)
