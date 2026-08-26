# TAGLINE

终端倒计时器与秒表

# TLDR

**倒计时器**

```termdown [5m]```

**倒计时到指定时刻**

```termdown [14:30]```

**在计时器上方显示标题**

```termdown -T "[Break time]" [10m]```

**结束时闪烁**

```termdown -b [5m]```

**使用文字转语音进行语音倒计时**

```termdown -v [Alex] [5m]```

**临界时间警告（最后 N 秒显示为红色）**

```termdown -c [10] [5m]```

**秒表模式（向上计时，不带时间参数）**

```termdown```

**使用另一种冒号分隔的格式**

```termdown -a [5m]```

# SYNOPSIS

**termdown** [_-t text_] [_-b_] [_-v voice_] [_options_] _time_

# PARAMETERS

**-t** _TEXT_, **--text** _TEXT_
> 倒计时结束时显示的文本。

**-b**
> 归零时闪烁。

**-v** _VOICE_, **--voice** _VOICE_
> 使用文字转语音进行语音倒计时（Linux 上需要 espeak，macOS 上需要 say）。

**-c** _SEC_, **--critical** _SEC_
> 最后 N 秒以红色显示并用 --voice 单独播报（默认为 3）。

**-f** _FONT_, **--font** _FONT_
> Figlet 字体名或 OTF/TTF 文件路径。

**-s**, **--no-seconds**
> 到达临界阈值前不显示秒。

**-a**, **--alt-format**
> 使用冒号分隔的时间格式。

**-B**, **--no-bell**
> 倒计时结束时不响铃。

**-T** _TITLE_, **--title** _TITLE_
> 显示在倒计时/秒表上方的文本。

**-q** _N_, **--quit-after** _N_
> 倒计时归零 N 秒后退出。

**-o** _PATH_, **--outfile** _PATH_
> 将当前剩余/已用时间写入该文件。

**--exec-cmd** _CMD_
> 倒计时期间每秒执行一次 CMD。

**--no-figlet**
> 显示时不使用 ASCII 艺术。

# DESCRIPTION

**termdown** 在终端中显示倒计时器和秒表，使用大号 figlet 风格文字以获得高可见度。它接受多种时间格式：秒、分钟（如 **5m**）、小时（如 **1h30m**），或具体的目标时刻（如 **14:30**）。

计时器可以使用文字转语音（通过 espeak 或 macOS 的 say）播报倒计时、闪烁显示以及显示自定义标题。临界阈值选项会在时间快到时改变显示颜色。若未给出时间，则以秒表模式向上计时。

# CAVEATS

仅在终端中显示。Figlet 字体是可选的，但建议使用以获得清晰的大号文本。--voice 选项在 Linux 上需要 espeak，macOS 上需要 say。

# HISTORY

**termdown** 作为终端倒计时器而创建，采用 figlet 风格的大字显示以保证可见性。

# INSTALL

```pacman: sudo pacman -S termdown```

```nix: nix profile install nixpkgs#termdown```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(1), [watch](/man/watch)(1), [sleep](/man/sleep)(1)
