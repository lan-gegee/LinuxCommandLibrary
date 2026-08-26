# TAGLINE

同步日历和联系人

# TLDR

**发现服务器上的集合**

```vdirsyncer discover```

**同步所有已配置的配对**

```vdirsyncer sync```

**同步特定配对**

```vdirsyncer sync [pair_name]```

**修复条目存储**

```vdirsyncer repair [storage_name]```

**显示版本**

```vdirsyncer --version```

# SYNOPSIS

**vdirsyncer** [_options_] _command_ [_arguments_]

# COMMANDS

**discover**: 查找远程服务器上的集合。

**sync**: 同步已配置的配对。

**repair**: 修复存储不一致问题。

**metasync**: 同步颜色等元数据。

# PARAMETERS

**--verbosity** _level_
> 设置输出详细程度（DEBUG、INFO、WARNING 等）。

**--config** _file_
> 使用替代的配置文件。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**vdirsyncer** 在服务器与本地存储之间同步日历（CalDAV）和联系人（CardDAV）。它将远程数据下载到本地目录，供 khal 和 khard 等工具访问和修改。

该工具支持双向同步，本地更改会同步回服务器。它也可以直接在两台服务器之间同步。配置中定义存储配对，指定源和目标。

首次运行需要 discover 来检测可用的集合（日历/通讯录），然后由 sync 下载数据。后续同步只传输双向的变化内容。

# CONFIGURATION

配置文件：~/.config/vdirsyncer/config

定义存储（本地或远程）以及连接它们的配对。支持 CalDAV、CardDAV 和本地文件系统存储类型。

# CAVEATS

首次 sync 之前必须先执行 discover。Google CardDAV 存在已知的数据完整性问题。首次同步前务必备份。冲突可能需要手动解决。

# HISTORY

**vdirsyncer** 作为 pimutils 项目的一部分创建，用于提供命令行个人信息管理。它之于日历和联系人，如同 OfflineIMAP 之于电子邮件，为 CalDAV/CardDAV 数据提供离线访问和本地工具支持。

# INSTALL

```dnf: sudo dnf install vdirsyncer```

```pacman: sudo pacman -S vdirsyncer```

```apk: sudo apk add vdirsyncer```

```brew: brew install vdirsyncer```

```nix: nix profile install nixpkgs#vdirsyncer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[khal](/man/khal)(1), [calcurse](/man/calcurse)(1)
