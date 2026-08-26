# TAGLINE

通过 Speech Dispatcher 进行文字转语音

# TLDR

**朗读文本**

```spd-say "[Hello, world]"```

**使用指定的嗓音类型朗读**

```spd-say -t [female1] "[Hello]"```

**调整语速**（-100 到 100）

```spd-say -r [50] "[Speaking faster]"```

**调整音调**（-100 到 100）

```spd-say -p [-20] "[Lower pitch]"```

**以指定语言朗读**

```spd-say -l [es] "[Hola mundo]"```

**逐字母拼读文本**

```spd-say -s "[ABC]"```

**将语音保存为 WAV 文件**

```spd-say -o [output.wav] "[Hello]"```

**从 stdin 读取**

```echo "[Hello world]" | spd-say -e```

**列出可用嗓音**

```spd-say --list-voices```

# SYNOPSIS

**spd-say** [_options_] "_text_"

**spd-say** -e

# PARAMETERS

**-r** _RATE_, **--rate** _RATE_
> 语速（-100 到 100，默认：0）

**-p** _PITCH_, **--pitch** _PITCH_
> 音调（-100 到 100，默认：0）

**-v** _VOLUME_, **--volume** _VOLUME_
> 音量（-100 到 100，默认：0）

**-l** _LANG_, **--language** _LANG_
> 语言代码（en, es, fr, de 等）

**-t** _TYPE_, **--voice-type** _TYPE_
> 嗓音类型（male1, male2, male3, female1, female2, female3, child_male, child_female）

**-o** _MODULE_, **--output-module** _MODULE_
> 要使用的输出模块

**-m** _MODE_, **--punctuation-mode** _MODE_
> 标点模式（none, some, all）

**-s**, **--spelling**
> 逐字母拼读文本

**-x**, **--ssml**
> 将输入解析为 SSML

**-e**, **--pipe-mode**
> 从 stdin 读取文本

**-w**, **--wait**
> 等待语音播放完毕

**-S**, **--stop**
> 停止任何正在进行的语音

**-C**, **--cancel**
> 取消当前语音

**-P**, **--priority** _LEVEL_
> 消息优先级（important, message, text, notification, progress）

**--list-voices**
> 列出可用嗓音

**--list-output-modules**
> 列出可用的输出模块

# DESCRIPTION

**spd-say** 是 Speech Dispatcher 的命令行客户端，可将文本转换为语音。它将文本发送给 speech-dispatcher 守护进程，后者将其路由到配置好的语音合成器（通常是 eSpeak NG、Festival 或类似工具）。

该命令为脚本和应用程序提供了一个简单的文字转语音接口。可以调整语速、音调和音量等嗓音特性。根据已安装的合成器，可支持多种语言和嗓音类型。

Speech Dispatcher 充当中心枢纽，允许多个应用程序共享语音合成资源。**spd-say** 命令提供对这套系统的直接访问，可用于测试、脚本编写和无障碍用途。

# CAVEATS

需要 speech-dispatcher 守护进程正在运行。可用的嗓音和语言取决于已安装的语音合成器。音频输出需要正常工作的声音系统。用于保存 WAV 的 **-o** 选项可能并非对所有输出模块都有效。某些合成器可能不支持所有嗓音类型。

# HISTORY

Speech Dispatcher 作为 **Free(b)Soft** 项目的一部分开发，旨在为 Linux 无障碍功能提供统一的文字转语音接口。开发始于 **2001 年**前后，由 **Hynek Hanke** 和 **Tomas Cerha** 主导。该项目致力于为视障用户提供语音输出以及通用的文字转语音功能。它与 Orca 等屏幕阅读器集成，并提供 **spd-say** 命令供脚本和命令行访问。

# INSTALL

```apt: sudo apt install speech-dispatcher```

```dnf: sudo dnf install speech-dispatcher```

```pacman: sudo pacman -S speech-dispatcher```

```apk: sudo apk add speech-dispatcher```

```zypper: sudo zypper install speech-dispatcher```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espeak-ng](/man/espeak-ng)(1), [festival](/man/festival)(1), [speech-dispatcher](/man/speech-dispatcher)(1), [say](/man/say)(1)
