# TAGLINE

通用语音合成系统

# TLDR

朗读文本

```echo "[Hello world]" | festival --tts```

朗读文件内容

```festival --tts [file.txt]```

启动交互模式

```festival```

用指定嗓音朗读

```echo "[text]" | festival --tts --voice [voice_name]```

将语音保存为 WAV

```echo "[Hello]" | text2wave -o [output.wav]```

列出可用嗓音

```festival -b "(voice.list)"```

# SYNOPSIS

**festival** [_options_] [_file_]

# DESCRIPTION

**festival** 是一个通用语音合成系统。它使用多种合成技术将文本转换为语音，可以通过交互方式或脚本控制。

该系统支持多种语言和嗓音，并且可以扩展新嗓音。它被用于无障碍辅助、语音界面和音频内容生成等场景。

# PARAMETERS

**--tts**
> 文本转语音模式（从 stdin 读取）。

**-b** _expression_
> 求值 Scheme 表达式。

**-i**
> 交互模式。

**--voice** _name_
> 选择嗓音。

**--otype** _type_
> 输出类型（riff、aiff 等）。

**--server**
> 作为服务器运行。

**--heap** _size_
> 堆大小（字节）。

**--help**
> 显示帮助。

# RELATED COMMANDS

**text2wave**: 将文本转换为音频文件
**festival_client**: 连接到服务器

# CAVEATS

嗓音质量参差不齐。长文本可能较慢。部分嗓音需要额外下载。自定义时了解 Scheme 会很有帮助。

# HISTORY

**Festival** 由 **Alan Black** 和 **Paul Taylor** 于 **20 世纪 90 年代**起在**爱丁堡大学言语技术研究中心**开发。它成为广泛使用的开源 TTS 系统。

# INSTALL

```apt: sudo apt install festival```

```dnf: sudo dnf install festival```

```pacman: sudo pacman -S festival```

```zypper: sudo zypper install festival```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak](/man/espeak)(1), [pico2wave](/man/pico2wave)(1), [say](/man/say)(1), [flite](/man/flite)(1)

# RESOURCES

```[Homepage](http://www.cstr.ed.ac.uk/projects/festival/)```

<!-- verified: 2026-07-15 -->
