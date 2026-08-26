# TAGLINE

用于分析 ELF 二进制文件的 TUI 工具

# TLDR

**分析 ELF 二进制文件**

```binsider [path/to/binary]```

**分析二进制文件**并从静态分析标签页开始

```binsider -t static [path/to/binary]```

**以自定义最小字符串长度分析二进制文件**

```binsider -n [8] [path/to/binary]```

**从字符串标签页开始分析二进制文件**，最小长度设为 8

```binsider -t strings -n 8 [path/to/binary]```

# SYNOPSIS

**binsider** [_options_] [_file_...]

# PARAMETERS

**-n**, **--min-len** _value_
> 要提取的字符串的最小长度（默认：15）

**-t**, **--tab** _tab_
> 应用启动时打开的初始标签页（默认：general）

**--accent-color** _color_
> 应用的强调色

**-h**, **--help**
> 显示帮助信息

**-V**, **--version**
> 显示版本信息

# DESCRIPTION

**binsider** 是一个终端用户界面，可对 ELF（Executable and Linkable Format）二进制文件进行静态和动态分析。它将多个标准 Unix 工具的功能整合到一个交互式界面中，堪称逆向工程师的瑞士军刀。

**general analysis** 标签页显示文件元数据，如大小、所有者、权限和时间戳（类似 **stat**），以及链接的共享库（类似 **ldd**）。选中某个共享库后可以递归分析其依赖。

**static analysis** 标签页在不执行二进制的情况下检查 ELF 结构，显示文件头、notes、程序头、节头、符号、动态符号、动态链接信息和重定位（类似 **readelf**）。

**dynamic analysis** 标签页在执行二进制的同时追踪系统调用和信号（类似 **strace** 和 **ltrace**），显示进程 ID、调用参数和返回值。执行摘要提供计时数据、调用频率和错误计数。该功能由 **lurk** 追踪库驱动。

**strings** 标签页提取二进制中的内嵌字符串（类似 **strings**），可用于发现 URL、凭据或其他敏感数据。最小字符串长度可通过 +/- 键交互调整，或通过 **-n** 标志指定。

**hexdump** 标签页提供一个带丰富仪表盘的结构化十六进制查看器。它支持键盘驱动的导航、搜索、跳转到指定字节偏移量，以及直接编辑十六进制内容并将修改保存回文件。该功能由 **heh** 十六进制编辑器驱动。

binsider 基于 Rust 和 Ratatui TUI 框架构建，全程使用键盘导航。用 Tab/Shift+Tab 切换标签页，用 h/j/k/l 或方向键浏览条目，按斜杠键发起搜索。

# CAVEATS

动态分析需要执行目标二进制文件，且仅在 Linux 上可用。十六进制编辑会就地修改二进制文件，保存更改前应先备份。必须以读写模式打开文件才能进行编辑。ELF 分析功能仅针对 ELF 格式，不适用于 PE 或 Mach-O 等其他二进制格式。

# HISTORY

**binsider** 由 **Orhun Parmaksiz** 创建，于 **2024 年 9 月**首次发布。它以 Rust 编写，采用 Apache License 2.0 与 MIT 双许可证。项目托管在 GitHub 上并持续活跃开发，网站与文档位于 https://binsider.dev。

# INSTALL

```pacman: sudo pacman -S binsider```

```zypper: sudo zypper install binsider```

```brew: brew install binsider```

```nix: nix profile install nixpkgs#binsider```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[readelf](/man/readelf)(1), [strace](/man/strace)(1), [ltrace](/man/ltrace)(1), [strings](/man/strings)(1), [ldd](/man/ldd)(1), [objdump](/man/objdump)(1), [hexdump](/man/hexdump)(1), [stat](/man/stat)(1), [nm](/man/nm)(1), [file](/man/file)(1)
