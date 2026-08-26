# TAGLINE

从 MP3 或其他音频源构建、切分 M4B 有声书并添加标签

# TLDR

将**一个 MP3 文件夹合并**为带章节的 M4B

```m4b-tool merge [folder/] --output-file=[audiobook.m4b]```

按章节**将有声书切分**为单独的文件

```m4b-tool split --audio-format=mp3 [audiobook.m4b]```

**刷新内嵌章节**标记

```m4b-tool chapters --adjust-by-silence [audiobook.m4b]```

带完整元数据**合并**

```m4b-tool merge [folder/] --output-file=[book.m4b] --name="[Title]" --artist="[Author]" --album="[Series]"```

**将单个 MP3 转换**为 M4B

```m4b-tool merge [file.mp3] --output-file=[file.m4b]```

为现有文件**添加封面图片**

```m4b-tool meta --cover=[cover.jpg] [audiobook.m4b]```

# SYNOPSIS

**m4b-tool** _command_ [_options_] [_input_]

# PARAMETERS

**merge**
> 将多个输入文件合成为一个保留章节信息的 M4B。

**split**
> 按章节将 M4B 切分，每章一个文件。

**chapters**
> 检查、生成或重写章节标记（支持 **--adjust-by-silence**）。

**meta**
> 读取或更新标题、作者、封面图、简介等标签。

**--output-file** _FILE_
> 输出文件的路径（M4B）。

**--audio-format** _FORMAT_
> **split** 的输出音频格式（m4b、m4a、mp3 等）。

**--name** _TITLE_
> 书名或专辑名。

**--artist** _NAME_
> 作者或朗读者姓名。

**--album** _TEXT_
> 专辑/系列名。

**--cover** _FILE_
> 内嵌封面图片（JPEG 或 PNG）。

**--jobs** _N_
> 并行编码任务数。

**--no-cache**
> 禁用对中间分析结果的缓存。

# DESCRIPTION

**m4b-tool** 是基于 PHP 的命令行工具，封装了 **ffmpeg** 和 **mp4v2**，用于创建、切分、重新打标以及检查 M4B 有声书文件。**merge** 子命令将一个目录下的音频文件（MP3、M4A、WAV、FLAC 等）拼接为单个 AAC 编码的 M4B，并根据输入文件的顺序或随附的 **chapters.txt** 自动插入章节标记。

**split** 子命令执行相反的过程，把每一章导出为所选格式的独立文件。**chapters** 用于检查或重写章节表，并可通过 **--adjust-by-silence** 将标记对齐到检测到的静音处，以获得更好的播放体验。**meta** 用于编辑 ID3/MP4 标签并可嵌入封面图。

持久化缓存可以加速对相同文件的重复运行；当输入的变化未被检测到时，可用 **--no-cache** 将其禁用。

# CAVEATS

需要 PATH 中存在 **ffmpeg** 和 **mp4v2** 可执行文件，以及可用的 **PHP 7.4+** 运行环境。编码质量由 ffmpeg 参数决定；高码率的 libfdk_aac 构建效果最佳。较长的有声书在合并阶段可能占用大量 CPU 和磁盘空间。

# HISTORY

**m4b-tool** 由 **Andreas Sandberg**（sandreas）编写，采用 MIT 许可证发布。作为商业 M4B 构建工具的开源替代品而广受欢迎，尤其受到使用 Audiobookshelf 或 Plex 维护有声书库的 Linux 用户青睐。

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [mp4box](/man/mp4box)(1), [sox](/man/sox)(1)
