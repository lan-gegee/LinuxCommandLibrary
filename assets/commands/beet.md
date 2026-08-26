# TAGLINE

音乐库管理器和元数据整理工具

# TLDR

从目录**导入**音乐并使用 MusicBrainz 打标签

```beet import [path/to/directory]```

**导入单曲**到库中

```beet import -s [path/to/file]```

**查询**音乐库

```beet list [query]```

显示**整个音乐库的统计信息**

```beet stats```

显示特定查询的**统计信息**

```beet stats [query]```

# SYNOPSIS

**beet** _command_ [_options_] [_arguments_]

# DESCRIPTION

**beet**（beets）是一个命令行音乐库管理器和元数据整理工具。它会自动从 MusicBrainz 获取元数据、整理音乐文件，并提供强大的查询接口。

Beets 可以修复标签、根据元数据重命名文件、抓取专辑封面，还能通过插件获得播放、Web 界面和格式转换等附加功能。

# SUBCOMMANDS

**import**
> 将音乐添加到库中并自动打标签

**list**（或 **ls**）
> 查询音乐库

**stats**
> 显示音乐库统计信息

**update**
> 文件变化后更新音乐库

**remove**（或 **rm**)
> 从音乐库中移除条目

**move**（或 **mv**）
> 移动或重命名库中的文件

**write**
> 将元数据更改写入文件

# PARAMETERS

**-s, --singletons**
> 将文件作为单曲导入（而非专辑曲目）

**-A, --noautotag**
> 不尝试自动打标签

**-l, --library** _path_
> 指定音乐库数据库的位置

**-c, --config** _path_
> 指定配置文件

# CONFIGURATION

**~/.config/beets/config.yaml**
> 主配置文件，控制库路径、导入行为、插件和元数据偏好。

# CAVEATS

首次导入大量收藏可能耗时较长。MusicBrainz 查询有速率限制。应先配置好配置文件以获得最佳行为。

# HISTORY

**beets** 由 Adrian Sampson 创建，于 **2010** 年首次发布。它已成长为一个拥有活跃插件生态的综合音乐库管理器。

# INSTALL

```dnf: sudo dnf install beets```

```pacman: sudo pacman -S beets```

```apk: sudo apk add beets```

```zypper: sudo zypper install beets```

```brew: brew install beets```

```nix: nix profile install nixpkgs#beets```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[id3v2](/man/id3v2)(1), [mp3info](/man/mp3info)(1)
