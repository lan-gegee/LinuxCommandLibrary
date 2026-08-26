# TAGLINE

实时编码环境

# TLDR

**启动 Orca**

```orca-c```

**打开文件**

```orca-c [file.orca]```

**设置 BPM**

```orca-c --bpm [120] [file.orca]```

**设置 MIDI 输出**

```orca-c --portmidi-list```

# SYNOPSIS

**orca-c** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要打开的 Orca 文件。

**--bpm** _BPM_
> 每分钟节拍数。

**--portmidi-list**
> 列出 MIDI 设备。

**--help**
> 显示帮助信息。

# DESCRIPTION

**orca-c** 是 Orca 实时编码环境。通过可视化编程创作音乐。

该工具提供基于网格的音序器。可生成 MIDI 输出。

# CAVEATS

基于终端的界面。需要配置 MIDI。采用独特的编程范式。

# HISTORY

Orca 由 **Hundred Rabbits** 创建，是一款实验性的实时编码环境。

# INSTALL

```nix: nix profile install nixpkgs#orca-c```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[supercollider](/man/supercollider)(1)
