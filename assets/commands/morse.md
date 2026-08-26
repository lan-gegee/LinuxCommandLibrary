# TAGLINE

将文本翻译为摩尔斯电码

# TLDR

**将文本翻译为摩尔斯电码（点和划）**

```morse -s "[Hello World]"```

**将明文翻译为可听的摩尔斯电码（扬声器播放）**

```morse -p "[Hello World]"```

**将摩尔斯点/划解码回文本**

```morse -d "[.... . .-.. .-.. ---]"```

**从文件而非参数读取文本**

```morse -e [file.txt]```

**播放音频时调整每分钟字数**

```morse -p -w [20] "[CQ]"```

# SYNOPSIS

**morse** [**-dlps**] [**-e** _file_] [**-w** _wpm_] [**-c** _cpm_] [_string_...]

# PARAMETERS

_string_
> 要编码的文本（或配合 **-d** 解码的摩尔斯点/划序列）。

**-d**
> 将摩尔斯电码（点和划）解码为文本。

**-e** _file_
> 从 _file_ 而非命令行读取输入。

**-l**
> 生成适合 LED 闪光器的"行模式"输出。

**-p**
> 通过扬声器以声音播放摩尔斯电码。

**-s**
> 输出短点/划，而不是 "dit"/"dah"。

**-w** _wpm_
> 播放音频时的每分钟字数（默认 20）。

**-c** _cpm_
> 每分钟字符数。是 **-w** 的替代方式。

# DESCRIPTION

**morse** 从参数或文件读取输入文本，并输出对应的摩尔斯电码。使用 **-s** 时输出为常见的 **... --- ...** 形式；默认形式则会拼出 **dit** 和 **dah**。使用 **-p** 时，每个符号会通过系统扬声器以可配置的速度播放。使用 **-d** 时，该工具执行反向转换，把点和划还原成文本。

大小写字母同等对待。未知字符会被静默跳过。

# CAVEATS

声音输出（**-p**）需要控制台或 PC 扬声器；在多数现代 Linux 系统上，除非已加载 **pcspkr**，否则不会有任何输出。**bsdgames** 实现在 Linux 和 macOS 上提供的选项有所不同——若具体选项不一致，请查阅本地 man page。

# HISTORY

**morse** 是经典的 **BSD 游戏**之一，自早期 4BSD 发行版起便已存在，最初是面向业余无线电爱好者的教学工具。

# INSTALL

```apt: sudo apt install morse```

```brew: brew install morse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[beep](/man/beep)(1), [espeak](/man/espeak)(1)
