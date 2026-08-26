# TAGLINE

从 CUE 文件中提取音轨切分点

# TLDR

从 CUE 文件中**提取切分点**

```cuebreakpoints [file.cue]```

以样本数格式输出

```cuebreakpoints --input-format samples [file.cue]```

在前面补上 2 秒间隙

```cuebreakpoints --prepend-gaps [file.cue]```

将间隙附加到上一轨末尾

```cuebreakpoints --append-gaps [file.cue]```

输出供 shnsplit 使用

```cuebreakpoints [file.cue] | shnsplit -o flac [file.wav]```

# SYNOPSIS

**cuebreakpoints** [_options_] _file.cue_

# PARAMETERS

**--input-format** _format_
> 输入时间格式：cue（默认）或 samples。

**--prepend-gaps**
> 将音轨间隙置于每轨开头。

**--append-gaps**
> 将间隙附加到上一轨末尾（第 1 轨的前置间隙除外）。

**--split-gaps**
> 将间隙平分给相邻音轨。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**cuebreakpoints** 读取 CUE 文件并以适合 **shnsplit** 等音频切分工具使用的格式输出音轨切分点。CUE 文件描述了一张音频 CD 如何划分为各条音轨，包括精确的帧位置。

输出是以 mm:ss.ff 格式（分:秒.帧，75 fps）表示的时间戳列表，标明每条音轨的起始位置。这些信息通过管道传给切分工具，用于把单个音频文件分割成独立的音轨。

间隙处理选项控制音轨之间的静音如何分配。不同的抓轨/编码流程可能要求间隙置于前面、附于后面或在相邻音轨间拆分。


# CAVEATS

CUE 文件必须与音频文件精确匹配（采样级精度）。错误的 CUE 文件会导致错误的切分结果。只适用于单文件镜像；多文件的 CUE 无需切分。必须安装 cuetools 软件包。

# HISTORY

cuebreakpoints 是 **cuetools** 的一部分，这是一套由 **Svend Sorensen** 创建的处理 CUE 文件的工具。这套工具开发于 **2000 年代中期**，用于辅助处理 CD 镜像，尤其是把单文件抓轨（Exact Audio Copy 常见做法）转换为独立音轨的同时保留准确的元数据。

# INSTALL

```apt: sudo apt install cuetools```

```dnf: sudo dnf install cuetools```

```pacman: sudo pacman -S cuetools```

```apk: sudo apk add cuetools```

```brew: brew install cuetools```

```nix: nix profile install nixpkgs#cuetools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cuetag](/man/cuetag)(1), [shnsplit](/man/shnsplit)(1), [flac](/man/flac)(1)
