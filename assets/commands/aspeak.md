# TAGLINE

命令行使用 Azure 神经网络文字转语音

# TLDR

用某种声音**朗读**文本

```aspeak -t "[Hello world]" -v [en-US-JennyNeural]```

**读取**文件

```aspeak -f [text.txt] -o [out.mp3]```

**列出**可用声音

```aspeak -l```

# SYNOPSIS

**aspeak** [*options*]

# DESCRIPTION

**aspeak** 是 Azure Cognitive Services 文字转语音（神经网络语音）的 CLI 客户端。可以从文本或文件合成语音，选择语言区域/声音，并将音频写入文件或直接播放。可通过 **pip install aspeak** 安装，Cargo 构建方式见上游文档。

# PARAMETERS

**-t**, **--text** *string*

> 要合成的文本。

**-f**, **--file** *path*

> 输入文本文件。

**-v**, **--voice** *name*

> 声音名称。

**-o**, **--output** *file*

> 输出音频路径。

**-l**, **--list-voices**

> 列出可用的声音（需要身份验证）。

身份验证通过环境变量或配置提供 Azure 语音密钥/区域——详见上游文档。

# CAVEATS

需要 Azure Speech 凭据和网络访问；使用会产生计费。声音的可用性因地区而异。

# INSTALL

```aur: yay -S aspeak```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[espeak](/man/espeak)(1), [festival](/man/festival)(1), [say](/man/say)(1)

# RESOURCES

```[Source code](https://github.com/kxxt/aspeak)```

<!-- verified: 2026-07-19 -->
