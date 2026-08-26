# TAGLINE

就地修改 Matroska 元数据，无需重新封装

# TLDR

从 Matroska 文件中**删除标题**

```mkvpropedit -d title [path/to/file.mkv]```

将字幕轨道 3 标记为 **SDH**（听障人士字幕）

```mkvpropedit [path/to/file.mkv] -e track:s3 -s flag-hearing-impaired=1```

将音频轨道 2 标记为**默认**

```mkvpropedit [path/to/file.mkv] -e track:a2 -s flag-default=1```

**删除**视频轨道 1 的名称

```mkvpropedit [path/to/file.mkv] -e track:v1 -d name```

为音频轨道 1 设置**轨道语言**

```mkvpropedit [path/to/file.mkv] -e track:a1 -s language=eng```

**列出所有可编辑的属性**

```mkvpropedit -l```

# SYNOPSIS

**mkvpropedit** [_options_] _source-filename_ [**-e** _selector_] [**-s** _name=value_] [**-d** _name_]

# PARAMETERS

**-e, --edit _selector_**
> 选择要编辑的段信息或轨道（info、track:n、track:an、track:vn、track:sn）

**-s, --set _name=value_**
> 设置属性值；不存在时创建

**-a, --add _name=value_**
> 添加属性；允许重复

**-d, --delete _name_**
> 移除属性

**-t, --tags _selector:filename_**
> 添加、替换或移除标签

**-c, --chapters _filename_**
> 添加、替换或移除章节

**--add-attachment _filename_**
> 将文件附加到容器中

**--delete-attachment _selector_**
> 移除附件

**-l, --list-property-names**
> 显示所有可编辑属性及其说明

**-p, --parse-mode _mode_**
> 设置解析模式：fast（默认）或用于受损文件的 full

**-v, --verbose**
> 在处理时显示 Matroska 元素

# DESCRIPTION

**mkvpropedit** 修改已有 Matroska 文件的属性，无需完整重新封装。它可以编辑段信息（标题、UID）、轨道头（语言代码、名称、标志）、章节、标签和附件。

轨道选择器使用 track:TYPE_NUMBER 格式，其中 TYPE 为 v（视频）、a（音频）、s（字幕）或 b（按钮），NUMBER 从 1 开始。使用 track:n 会选择第 n 个轨道而不区分类型。

# CAVEATS

更改会直接修改原文件。属性名必须完全匹配；可用 -l 列出有效名称。某些属性无法添加到原本不包含它们的轨道上。语言修改默认会同时影响 IETF 和旧式语言元素。

# HISTORY

**mkvpropedit** 属于 **MKVToolNix**，由 **Moritz Bunkus** 开发。MKVToolNix 提供一整套用于创建、检查和修改 Matroska 多媒体容器文件的工具。

# INSTALL

```apt: sudo apt install mkvtoolnix```

```dnf: sudo dnf install mkvtoolnix```

```apk: sudo apk add mkvtoolnix```

```zypper: sudo zypper install mkvtoolnix```

```brew: brew install mkvtoolnix```

```nix: nix profile install nixpkgs#mkvtoolnix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkvmerge](/man/mkvmerge)(1), [ffmpeg](/man/ffmpeg)(1)
