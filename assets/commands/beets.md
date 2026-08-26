# TAGLINE

音乐库管理器和元数据整理工具

# TLDR

**将音乐导入音乐库**

```beet import [path/to/music]```

**导入**时不自动打标签

```beet import -A [path/to/music]```

**列出所有专辑**

```beet ls -a```

**搜索曲目**

```beet ls [artist:beatles]```

**更新**音乐库统计信息

```beet stats```

**移动文件**以匹配音乐库的组织结构

```beet move```

**修改元数据**

```beet modify [query] [field=value]```

**抓取缺失的专辑封面**

```beet fetchart```

# SYNOPSIS

**beet** _command_ [_options_] [_query_]

# PARAMETERS

**import** [_path_]
> 将音乐文件导入音乐库，并通过 MusicBrainz 打标签。

**list** (**ls**) [_query_]
> 列出与查询匹配的曲目或专辑。

**modify** _query_ _field=value_
> 修改匹配条目的元数据。

**move** (**mv**) [_query_]
> 移动（使用 -c 则为复制）文件以匹配配置的路径。

**remove** (**rm**) _query_
> 从音乐库中移除条目（加 -d 可同时删除文件）。

**update** (**upd**) [_query_]
> 根据磁盘上标签的变化更新音乐库。

**write** [_query_]
> 将数据库中的元数据写回文件标签。

**stats** [_query_]
> 显示音乐库统计信息。

**fields**
> 列出可用于查询的元数据字段。

**config** [**-pe**]
> 显示配置（-p 显示路径，-e 在 $EDITOR 中编辑）。

**-a**, **--album**
> 以专辑而非单曲为操作单位。

**-f**, **--format** _template_
> list 输出的自定义格式字符串。

**-A**, **--noautotag**
> 导入时跳过 MusicBrainz 自动打标签。

**-s**, **--singletons**
> 将曲目作为独立单曲而非专辑导入。

**-c**, **--copy** / **-C**, **--nocopy**
> 将文件复制到音乐库目录（或保留在原处）。

**-t**, **--timid**
> 对每个导入候选都提示确认。

# QUERY SYNTAX

**artist:name**: 匹配艺术家字段
**album:name**: 匹配专辑字段
**year:2020**: 匹配年份
**year:2018..2022**: 年份范围
**bitrate:320..**: 最低比特率
**path:/music/**: 匹配文件路径

# DESCRIPTION

**beets** 是一个音乐库管理器和整理工具，能够自动标记、组织和管理音乐收藏。它查询 MusicBrainz 等在线数据库来识别专辑并修正元数据。

导入过程中，beets 会识别专辑、修正元数据、下载专辑封面，并将文件移动到结构化的目录层级中。其查询系统支持跨整个音乐库的强大搜索和批量修改。

插件系统通过抓取歌词、管理播放次数、转换格式以及与音乐播放器集成等功能扩展了它的能力。配置保存在 **~/.config/beets/config.yaml**。

# PLUGINS

**fetchart**: 下载专辑封面
**lyrics**: 抓取歌词
**lastgenre**: 从 Last.fm 获取流派
**convert**: 转码为其他格式
**duplicates**: 查找重复曲目
**web**: 用于浏览的 Web 界面

# CONFIGURATION

**~/.config/beets/config.yaml**
> 主配置文件，控制库路径、导入行为、插件和元数据偏好。可设置 **BEETSDIR** 环境变量来使用其他目录（及库数据库）。运行 `beet config -p` 可打印当前生效的路径。

# CAVEATS

由于需要在线查询，首次导入大型音乐库可能耗时较长。对于冷门发行版本或标签混乱的文件，自动匹配可能失败。数据库必须与实际文件保持同步；绕过 beets 直接移动文件可能导致不一致。

# HISTORY

Beets 由 **Adrian Sampson** 于 **2010** 年前后在其攻读计算机科学博士期间作为研究项目创建。它从一个个人工具成长为功能全面的音乐管理系统。该项目自诞生起就是开源的，并受益于社区贡献的众多插件。它至今仍是最强大的命令行音乐库管理器之一。

# INSTALL

```dnf: sudo dnf install beets```

```pacman: sudo pacman -S beets```

```zypper: sudo zypper install beets```

```brew: brew install beets```

```nix: nix profile install nixpkgs#beets```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[picard](/man/picard)(1), [kid3](/man/kid3)(1), [metaflac](/man/metaflac)(1), [mpd](/man/mpd)(1), [mpc](/man/mpc)(1), [ffmpeg](/man/ffmpeg)(1)

# RESOURCES

```[Source code](https://github.com/beetbox/beets)```

```[Documentation](https://beets.readthedocs.io/)```

<!-- verified: 2026-06-19 -->
