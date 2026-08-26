# TAGLINE

命令行工作时长追踪工具

# TLDR

**打卡上班（开始计时）**

```moro hi```

**在指定时间打卡上班**

```moro hi [09:30]```

**打卡下班（停止计时）**

```moro bye```

**以分钟为单位设置休息时间**

```moro break [30]```

**显示今日工作报告**

```moro report```

**显示所有日期的报告**

```moro report --all```

**设置默认休息时间**

```moro config --break [45]```

**清除所有已记录的数据**

```moro clear```

# SYNOPSIS

**moro** [_command_] [_options_]

# PARAMETERS

**hi** [_HH:MM_]
> 打卡上班。可选指定一个过去的开始时间。

**bye** [_HH:MM_]
> 打卡下班。可选指定一个过去的结束时间。

**break** _MINUTES_
> 以分钟为单位设置休息时间。

**report** [**--all**]
> 显示工作报告。使用 --all 显示所有日期。

**config** **--break** _MINUTES_
> 设置默认休息时间。

**clear**
> 清除所有已记录的数据。

**--help**
> 显示帮助信息。

# DESCRIPTION

**moro** 是一个命令行工作时长追踪工具。它记录上下班打卡时间，并计算扣除休息后的总工作时长。

计算公式为：（下班时间）-（上班时间）-（休息时长）= 工作时长。默认休息时间为 30 分钟。

# CAVEATS

基于 Node.js。使用简单的平面文件存储，且仅在本机记录。该项目已弃用；已发布的 npm 版本被视为唯一的稳定版本。

# HISTORY

moro 的诞生初衷是为在终端中工作的开发者提供一个**简单的计时工具**。

# INSTALL

```aur: yay -S moro```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timew](/man/timew)(1), [watson](/man/watson)(1)
