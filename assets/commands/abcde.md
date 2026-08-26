# TAGLINE

自动化 CD 抓轨与编码工具

# TLDR

将 CD **抓取**为默认格式（通常是 Ogg Vorbis）

```abcde```

将 CD **抓取**为 MP3 格式

```abcde -o mp3```

将 CD **抓取**为 FLAC 格式

```abcde -o flac```

同时**抓取为多种格式**

```abcde -o flac,mp3,ogg```

利用**多个 CPU 核心**抓轨以加快编码

```abcde -j [4]```

以**非交互模式**抓轨（不提示）

```abcde -N```

只抓取 CD 上的**指定音轨**

```abcde [1] [3] [5]```

从指定的 CD 设备抓轨

```abcde -d [/dev/sr0]```

# SYNOPSIS

**abcde** [_options_] [_tracks_]

# PARAMETERS

**-o** _format_
> 输出格式：mp3、ogg、flac、opus、m4a、wav、spx、mpc、mka、wv、ape、mp2、tta、aiff

**-d** _device_
> 指定 CD 设备（默认：/dev/cdrom）

**-j** _n_
> 同时运行 n 个编码进程（适用于多核系统）

**-a** _actions_
> 指定动作：cddb、read、normalize、encode、tag、move、replaygain、playlist、clean

**-N**
> 非交互模式；从不请求输入

**-n**
> 跳过 CDDB 查询；使用通用音轨名

**-1**
> 将整张 CD 编码为单一音轨

**-c** _file_
> 使用指定的配置文件

**-C** _discid_
> 使用指定的 CDDB 唱片 ID 进行查询

**-p**
> 音轨编号补前导零

**-P**
> 用 Unix 管道编码（减少磁盘占用）

**-r** _host_
> 从指定主机远程抓轨

**-S** _speed_
> 设置光驱读取速度

**-t** _n_
> 音轨从 n 开始编号

**-T** _n_
> 与 -t 相同，但还会修改播放列表

**-x**
> 抓轨完成后弹出 CD

**-w** _comment_
> 向编码后的文件添加注释

**-W** _n_
> 为多碟专辑设置碟号

**-k**
> 编码后保留 wav 文件

**-l**
> 使用低磁盘空间模式

**-V**
> 显示版本信息

**-h**
> 显示帮助信息

# DESCRIPTION

**abcde**（A Better CD Encoder）是一个 shell 脚本，用于自动完成音频 CD 抓轨并编码为多种压缩格式的过程。它负责从读盘到给最终文件打标签的全部流程。

该工具会查询在线数据库（CDDB、MusicBrainz）来自动获取音轨名称、艺术家信息和专辑详情。它使用 **cdparanoia** 等后端程序进行安全抓轨，并用 **lame**、**oggenc**、**flac**、**opusenc** 等编码器进行压缩。

一次运行即可生成多种输出格式，并可通过 **-j** 选项在多个 CPU 核心上并行编码。配置通过 **/etc/abcde.conf** 或 **~/.abcde.conf** 管理，可自定义编码器设置、输出路径和命名规则。

# CONFIGURATION

**/etc/abcde.conf**
> 面向所有用户的系统级默认配置文件。

**~/.abcde.conf**
> 覆盖系统默认值的每用户配置文件。控制输出格式、编码器选项、文件命名模板、CDDB 服务器和后处理动作。

关键配置变量包括 **OUTPUTTYPE**（输出格式）、**OUTPUTDIR**（目标目录）、**LAMEOPTS** / **OGGENCOPTS** / **FLACOPTS**（各编码器专属选项）、**CDDBMETHOD**（元数据查询方式）和 **MUNGEDFILENAME**（文件名字符处理）。

# CAVEATS

需要单独安装抓轨后端（cdparanoia 或 cdda2wav）和编码器（MP3 用 lame、Ogg 用 oggenc、FLAC 用 flac 等）。CDDB 查询需要网络连接。出于专利考虑，lame 等部分编码器可能需要从 non-free 软件仓库安装。

# HISTORY

**abcde** 由 **Robert Woodcock** 于 **1998 年**创建，目的是提供一种在 Linux 上自动抓取 CD 的简单方法。其名字意为"A Better CD Encoder"，反映出简化此前多步骤手动操作的目标。它一直得到积极维护，陆续支持了 Opus 和 AAC 等现代格式，同时始终保持纯 shell 脚本的实现。

# INSTALL

```dnf: sudo dnf install abcde```

```aur: yay -S abcde```

```apk: sudo apk add abcde```

```zypper: sudo zypper install abcde```

```brew: brew install abcde```

```nix: nix profile install nixpkgs#abcde```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cdparanoia](/man/cdparanoia)(1), [lame](/man/lame)(1), [flac](/man/flac)(1), [opusenc](/man/opusenc)(1)

# RESOURCES

```[Source code](https://git.einval.com/cgi-bin/gitweb.cgi?p=abcde.git)```

```[Homepage](https://abcde.einval.com/)```

<!-- verified: 2026-06-10 -->
