# TAGLINE

备份和恢复电子游戏存档数据

# TLDR

**备份所有已知游戏**

```ludusavi backup```

**备份指定游戏**

```ludusavi backup --by-title "[Game Name]"```

**恢复所有备份**

```ludusavi restore```

**恢复指定游戏**

```ludusavi restore --by-title "[Game Name]"```

**预览备份**（试运行）

```ludusavi backup --preview```

**备份到自定义位置**

```ludusavi backup --path [/path/to/backups]```

**列出已备份的游戏**

```ludusavi backups```

**更新游戏清单**

```ludusavi manifest update```

# SYNOPSIS

**ludusavi** [_backup_] [_restore_] [_backups_] [_--by-title name_] [_--path dir_] [_options_]

# PARAMETERS

**backup**
> 备份存档数据。

**restore**
> 从备份恢复存档数据。

**backups**
> 列出可用的备份。

**--by-title** _NAME_
> 按标题对特定游戏进行操作。

**--by-steam-id** _ID_
> 按 Steam ID 对游戏进行操作。

**--path** _DIR_
> 自定义备份目录。

**--preview**
> 显示将要进行的操作而不实际执行。

**--force**
> 不经确认直接覆盖。

**--compression** _TYPE_
> 压缩类型（none、deflate、bzip2、zstd）。

**--format** _TYPE_
> 备份格式（simple、zip）。

**--merge**
> 与现有备份合并。

**manifest update**
> 更新游戏数据库。

**--config** _FILE_
> 使用自定义配置文件。

**--help**
> 显示帮助。

# DESCRIPTION

**ludusavi** 用于备份和恢复电子游戏存档数据。它知道游戏将存档存储在哪里，可以自动处理数千款游戏。

其清单涵盖了 Windows、Linux 和 macOS 上游戏存档的路径，覆盖 Steam、GOG、Epic 及其他平台。对于不支持的游戏可以添加自定义条目。

备份格式包括简单目录和压缩的 ZIP 文件。多种压缩算法可在速度与体积之间权衡。

可以配置定时备份以自动运行。合并选项将新存档添加到现有备份中而不替换旧的备份。

该工具通过插件与 Playnite 及其他游戏启动器集成。GUI 版本为偏好的用户提供了可视化管理。

# CAVEATS

并非所有游戏都在清单中。云存档可能冲突。部分游戏使用注册表项（Windows）。非常大的存档可能需要较长时间压缩。

# HISTORY

**ludusavi** 于 **2020 年**左右创建，是 GameSave Manager 的开源替代品。它使用 PCGamingWiki 清单获取存档位置，受益于社区维护的数千款游戏的数据。

# INSTALL

```brew: brew install ludusavi```

```nix: nix profile install nixpkgs#ludusavi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restic](/man/restic)(1), [rsync](/man/rsync)(1), [rclone](/man/rclone)(1)
