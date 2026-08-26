# TAGLINE

终端里的节律共振呼吸引导器

# TLDR

按一天中的时段自动选择预设并**开始练习**

```breathe```

**使用命名预设**（balanced、calm、extended）

```breathe --preset calm```

**进行 5 分钟自定义练习**，吸气 4 秒、呼气 6 秒

```breathe --duration 5 --ratio 4-6```

**静音模式**，无音频提示且不显示启动警告

```breathe --no-sound --quiet```

**跳过记录**本次会话，不写入 CSV 日志

```breathe --no-log```

**列出全部内置预设**

```breathe --list-presets```

**打印日志文件路径**后退出

```breathe --log```

开始前**显示安全须知**

```breathe --safety```

# SYNOPSIS

**breathe** [_-p preset_] [_-d minutes_] [_-r in-ex_] [_-n_] [_-q_] [_--no-log_] [_--log_] [_--safety_] [_--list-presets_] [_--version_]

# PARAMETERS

**-p**, **--preset** _NAME_
> 使用命名预设。有效值：**balanced**、**calm**、**extended**。

**-d**, **--duration** _MINUTES_
> 会话时长，单位为分钟（1 到 60）。

**-r**, **--ratio** _IN-EX_
> 吸气与呼气的秒数，写作 _IN-EX_（例如 **5-5** 或 **4-6**）。

**-n**, **--no-sound**
> 禁用音频提示。

**-q**, **--quiet**
> 不显示启动警告。

**--no-log**
> 不将本次会话追加到 CSV 日志。

**--log**
> 打印日志文件路径后退出。

**--safety**
> 显示关于节律呼吸的安全信息后退出。

**--list-presets**
> 显示内置预设表格后退出。

**--version**
> 显示版本号。

# PRESETS

**balanced**
> 10 分钟，吸气 5 秒，呼气 5 秒（每分钟 6 次呼吸）。

**calm**
> 15 分钟，吸气 4 秒，呼气 6 秒（每分钟 6 次呼吸）。

**extended**
> 20 分钟，吸气 4 秒，呼气 6 秒（每分钟 6 次呼吸）。

# DESCRIPTION

**breathe** 是一个单文件 Python 终端应用，引导用户完成节律共振呼吸练习，目标约为每分钟 6 次呼吸，以此作为迷走神经张力的训练节奏。它使用直接的 ANSI 转义码（不用 curses）绘制移动的进度条引导器，播放可选的音频提示，并把每次完成的会话记录到 CSV 文件。

不带参数运行时，**breathe** 会根据一天中的时段选择一个预设。**--preset**、**--duration** 和 **--ratio** 选项可覆盖默认值，让用户独立配置会话时长和吸呼比。

# RUNTIME CONTROLS

**space**
> 暂停和恢复当前会话。

**s**
> 开关音频提示。

**q**、**Ctrl+C**
> 退出当前会话。

# CONFIGURATION

**~/.breathe_log.csv**
> 每次完成的会话之后写入的会话日志。列包括：日期、时间、预设、吸呼比、目标时长、实际时长、呼吸次数、完成百分比和状态。

# CAVEATS

节律呼吸是一种健康练习，不是医疗手段。内置的 **--safety** 界面提醒：驾驶或操作机器时、以及感到头晕时不要使用。音频提示需要可用的终端响铃或系统音频；在极简终端上，**--no-sound** 可能是唯一合理的选择。

# HISTORY

**breathe** 由 **Marek Kowalczyk** 编写，于 2026 年以 MIT 许可证发布，是一个单文件 Python 工具。它通过 PyPI 和 Homebrew tap 分发，也可以直接作为 **breathe.py** 运行。

# SEE ALSO

[python](/man/python)(1), [sleep](/man/sleep)(1), [watch](/man/watch)(1)
