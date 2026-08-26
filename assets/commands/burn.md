# TAGLINE

用于刻录数据光盘、音频 CD、ISO 和复制光盘的控制台前端

# TLDR

**从目录树刻录数据 CD**

```burn -D -p [path/to/dir]```

**将 ISO 镜像刻录**到光盘

```burn -I -n [image.iso]```

**从 MP3、Ogg 或 WAV 文件创建音频 CD**

```burn -A -a [track1.mp3] -a [track2.wav]```

**即时复制一张 CD**

```burn -C```

**模拟**刻录而不实际写入

```burn -D -s -p [path/to/dir]```

**刻录多区段数据 CD**

```burn -D -m -p [path/to/dir]```

# SYNOPSIS

**burn** _MAIN_MODE_ [_options_]... [_file/s_]...

# PARAMETERS

**-D**, **--data-cd**
> 从文件和目录创建数据 CD。

**-I**, **--iso-cd**
> 将已有的 ISO 镜像刻录到光盘。

**-C**, **--copy-cd**
> 复制一张 CD，可选即时复制。

**-A**, **--audio-cd**
> 从 MP3、Ogg 或 WAV 输入文件创建音频 CD。

**-s**, **--simulate**
> 执行刻录模拟（不进行激光写入）；可用于测试介质和流程。

**-p**, **--path** _path_
> 将 _path_ 的内容添加到 CD 根目录，不包裹目录本身。

**-r**, **--preserve-path** _path_
> 添加文件的同时保留原始目录结构。

**-x**, **--exclude-path** _pattern_
> 排除匹配 _pattern_ 的文件或目录。

**-c**, **--change-path** _from_=_to_
> 在刻录时重命名 CD 上的路径。

**-l**, **--follow-symlink**
> 跟随符号链接目录，而不是只记录链接本身。

**-m**, **--multisession**
> 将区段标记为可追加，以便日后继续添加数据。

**-n**, **--name** _file_
> 要刻录的 ISO 镜像名称（与 **-I** 一起使用）。

**-a**, **--audio-file** _file_
> 要添加的音轨（与 **-A** 一起使用）；重复使用可添加更多音轨。

**--help**
> 打印内置帮助并退出。

# DESCRIPTION

**burn** 是标准 CD 刻录工具链（**cdrecord/wodim**、**mkisofs/genisoimage** 以及 MP3 和 Ogg 解码器）之上的控制台封装，通过单一命令暴露常见的刻录工作流。四个互斥的主模式之一决定是写入数据、ISO 镜像、另一张光盘的副本，还是由压缩与非压缩来源组合而成的音频 CD。

程序会在写入前透明地解码音频文件，为数据光盘生成所需的 ISO9660 文件系统，并将生成的轨道交给底层刻录程序。刻录参数和刻录机设备从用户及系统配置中读取；命令行选项可在每次调用时覆盖它们。

# CONFIGURATION

**/etc/burn.conf**
> 系统级配置：设备路径、速度、默认文件系统选项。

**~/.burn/burn.conf**
> 每个用户对系统配置的覆盖。

# CAVEATS

需要在 **PATH** 中有可用的 **cdrecord** 或 **wodim** 以及 **mkisofs**/**genisoimage**。音频模式依赖外部解码器（**lame**、**oggdec**）来处理非 WAV 输入。光介质已基本过时；现代工作流建议考虑 USB 镜像以及 **dd**、**xorriso** 或 **growisofs**。

# HISTORY

**burn** 由 **Ben Finney** 和 **Gaetano Paolone** 编写，是对 cdrtools 套件的友好 Bash 封装，自 **2000 年代初**起就被打包进 **Debian**。它以 **GNU GPL v2** 或更高版本许可分发。

# SEE ALSO

[wodim](/man/wodim)(1), [cdrecord](/man/cdrecord)(1), [growisofs](/man/growisofs)(1), [genisoimage](/man/genisoimage)(1)
