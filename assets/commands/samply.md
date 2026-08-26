# TAGLINE

跨平台 CPU 采样分析器，输出 Firefox Profiler 格式

# TLDR

**分析一条命令**并在浏览器中打开结果

```samply record [path/to/command] [arg1] [arg2]```

以赫兹为单位**设置采样率**

```samply record --rate [1000] [path/to/command]```

**录制但不打开浏览器**，而是保存到文件

```samply record --save-only --output [profile.json] -- [path/to/command]```

**加载之前保存的**性能剖析文件

```samply load [path/to/profile.json]```

从其他分析器**导入**剖析文件

```samply import [path/to/perf.data]```

按 PID **分析正在运行的进程**（macOS/Linux）

```samply record --pid [12345]```

**附加到系统上的所有进程**（Linux/Windows）

```samply record -a```

# SYNOPSIS

**samply**  _command_  [_options_]  [**--**]  [_program_]  [_args_ ...]

# COMMANDS

**samply record** [_options_] **--** _command_ [_args_]
> 启动 _command_ 并记录其执行期间的 CPU 剖析。命令退出后，默认会在 **profiler.firefox.com** 中打开剖析结果。

**samply load** _profile_
> 在 Firefox Profiler 中打开之前保存的剖析文件。

**samply import** _file_
> 将其他格式的剖析文件（Linux **perf.data**、Xcode .trace、ETW 等）转换后在 Firefox Profiler 中打开。

**samply setup**
> 在 macOS 上为 **samply** 二进制文件签名，使其能够附加到已存在的进程。

# PARAMETERS

**--rate** _hz_
> 每秒采样次数表示的采样频率。默认：_1000_。

**--duration** _seconds_
> 在经过 _seconds_ 秒的挂钟时间后停止录制。

**--save-only**
> 不打开浏览器；只将剖析文件写入磁盘。

**-o**, **--output** _file_
> 输出剖析文件的路径（默认：_profile.json.gz_）。

**--profile-name** _name_
> 设置在 Firefox Profiler 界面中显示的剖析名称。

**--port** _n_
> 本地符号服务器的端口（默认：_3000_）。

**--no-open**
> 保存剖析文件并启动本地符号服务器，但不启动浏览器。

**--presymbolicate**
> 在保存时解析符号并嵌入到剖析文件中，使其可以在没有原始二进制文件的机器上使用。

**--pid** _pid_
> 分析已在运行的进程，而不是启动新进程。

**-a**, **--all**
> 分析系统上的所有进程（全系统剖析）。

**--reuse-threads**
> 在 fork 之间保持线程 ID 稳定；适用于长期运行的守护进程。

# DESCRIPTION

**samply** 是一款可运行在 **macOS**、**Linux** 和 **Windows** 上的采样分析器，生成 Firefox Profiler JSON 格式的剖析文件。它会周期性中断目标进程，为每个线程捕获一次栈轨迹，并将聚合的样本写入磁盘；录制结束后，**samply** 会启动一个小型本地 Web 服务器，在默认浏览器中打开 **profiler.firefox.com**，剖析器再从该服务器获取数据和符号。

在 macOS 和 Windows 上，**samply** 同时报告 on-CPU 和 off-CPU 样本，因此在磁盘、网络或锁上阻塞的情况也会在火焰图中可见。在 Linux 上目前仅报告 on-CPU 样本，使用内核的 **perf_event_open** 子系统（无需内核模块或 LD_PRELOAD）。

输出与 Firefox 内置分析器使用的 JSON 格式相同，因此火焰图、标记链、调用树、堆栈图和源码视图都开箱即用，甚至可以跨机器使用：剖析文件可以通过上传到公共的 Firefox Profiler 实例或直接交换 JSON 文件来共享。

# CAVEATS

在 **Linux** 上，**samply** 需要访问性能事件。如果 **/proc/sys/kernel/perf_event_paranoid** 大于 _1_，录制将失败并报 "permission denied"。可以临时降低该值：

```echo 1 | sudo tee /proc/sys/kernel/perf_event_paranoid```

或通过 _sysctl kernel.perf_event_paranoid=1_ 持久化设置。

在 **macOS** 上，代码签名默认阻止附加到已有进程。运行一次 **samply setup** 为二进制文件自签名后，**--pid** 即可使用。

符号由 **samply** 启动的本地 Web 服务器按需解析；如果关闭了终端会话，浏览器中的剖析文件将无法访问符号。请使用 **--presymbolicate** 将符号嵌入其中。

# HISTORY

**samply** 由 **Mozilla** 的 **Markus Stange** 于 **2021 年**创建，目的是让外部开发者也能使用 **Gecko Profiler** 自 **2011 年**以来为 Firefox 生成的剖析格式。项目位于 _github.com/mstange/samply_，采用 MIT 或 Apache-2.0 许可证发布。

# INSTALL

```pacman: sudo pacman -S samply```

```zypper: sudo zypper install samply```

```brew: brew install samply```

```nix: nix profile install nixpkgs#samply```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perf](/man/perf)(1), [strace](/man/strace)(1), [gprof](/man/gprof)(1), [valgrind](/man/valgrind)(1), [hyperfine](/man/hyperfine)(1)
