# TAGLINE

通过采样调用栈来分析运行中的进程

# TLDR

按 PID **采样进程** 10 秒

```sample [pid]```

**按名称采样进程**，指定采样时长

```sample [Safari] [30]```

以自定义间隔**采样**（毫秒）

```sample [pid] [10] [5]```

**等待进程启动后**再采样

```sample [MyApp] [10] -wait```

**将采样输出保存到文件**

```sample [pid] [10] -file [output.txt]```

**采样可能在采样期间退出的进程**

```sample [pid] [10] -mayDie```

# SYNOPSIS

**sample** _pid|partial-name_ [_duration_] [_interval_] [_-wait_] [_-mayDie_] [_-fullPaths_] [_-file filename_]

# PARAMETERS

**pid | partial-name**
> 要采样的进程 ID 或部分可执行文件名

**duration**
> 采样时长（秒）（默认：10）

**interval**
> 采样间隔（毫秒）（默认：1）

**-wait**
> 等待指定进程启动后再开始采样

**-mayDie**
> 立即捕获符号位置，以防进程在采样期间退出

**-fullPaths**
> 在输出中显示源文件的完整路径

**-file** _filename_
> 将输出写入指定文件而非标准输出

**-e**
> 采样完成后用 TextEdit 打开输出文件

# DESCRIPTION

**sample** 是 macOS 的命令行性能分析工具，它定期捕获进程中所有线程的调用栈。每次采样时它会短暂挂起进程，记录当前的栈轨迹，然后恢复执行。

生成的报告显示一棵精简的调用树，标明哪些函数正在执行以及它们在栈上出现的频率。这种采样方式能够高效地定位热点和性能瓶颈，而无需全量插桩的开销。

更快的采样率（更小的 interval 值）提供更多数据点，能更好地覆盖短生命周期的函数调用。输出可以作为文本进行分析，也可以在 Xcode Instruments 中打开进行图形化展示。

# CAVEATS

采样只捕获采样点上正在执行的函数，因此极快的函数可能被遗漏。每次采样期间进程会被短暂挂起，这可能影响对时序敏感的应用。采样其他用户的进程需要相应权限。

# HISTORY

**sample** 属于 Apple 的 macOS 开发者工具套件，提供了与 Instruments 和活动监视器相同的采样技术的命令行访问方式。它让性能分析无需完整的 Xcode IDE 即可完成。

# INSTALL

```apt: sudo apt install barcode```

```dnf: sudo dnf install barcode```

```pacman: sudo pacman -S barcode```

```apk: sudo apk add barcode```

```zypper: sudo zypper install barcode```

```nix: nix profile install nixpkgs#barcode```

<!-- packages: 2026-07-22 -->

# SEE ALSO
