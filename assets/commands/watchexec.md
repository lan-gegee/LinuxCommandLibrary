# TAGLINE

在文件系统变化时运行命令

# TLDR

文件变化时**运行命令**

```watchexec [command]```

**监视特定目录**

```watchexec -w [src] -w [tests] [command]```

**按文件扩展名过滤**

```watchexec -e rs,toml [cargo build]```

文件变化时**重启服务器**

```watchexec -r [./server]```

每次运行前**清屏**

```watchexec -c [command]```

**忽略特定路径**

```watchexec -i [node_modules] -i [*.log] [command]```

**自定义防抖延迟**（毫秒）

```watchexec -d [500] [command]```

等到首次变化再运行

```watchexec --postpone [command]```

# SYNOPSIS

**watchexec** [_options_] [_--_] _command_ [_args ..._]

# PARAMETERS

**-w**, **--watch** _path_
> 要监视的路径（可多次指定）。

**-e**, **--exts** _extensions_
> 按文件扩展名过滤（逗号分隔）。

**-f**, **--filter** _pattern_
> 用于包含文件的 gitignore 风格模式。

**-i**, **--ignore** _pattern_
> 用于排除文件的 gitignore 风格模式。

**-r**, **--restart**
> 变化发生时如果命令仍在运行则重启它。

**-s**, **--signal** _signal_
> 发送信号以停止命令（例如 SIGHUP、SIGKILL）。

**-c**, **--clear**
> 每次运行命令前清屏。

**-d**, **--debounce** _ms_
> 两次命令运行之间的最小毫秒数（默认：50）。

**-W**, **--watch-when-idle**
> 命令运行期间忽略变化。

**--postpone**
> 等到第一次变化后才运行命令。

**--no-vcs-ignore**
> 不使用 .gitignore 文件。

**--no-default-ignore**
> 不使用内置的忽略模式。

**--poll** _interval_
> 使用轮询而不是原生文件系统事件。

**-v**, **--verbose**
> 打印调试信息。

**-V**, **--version**
> 打印版本信息。

**-h**, **--help**
> 打印帮助信息。

# DESCRIPTION

**watchexec** 监视文件系统路径，并在检测到变化时执行命令。它使用原生文件系统通知 API 实现高效监视，并支持 gitignore 风格的过滤。

该工具常用于开发工作流，例如自动重新编译代码、重启服务器、运行测试或重新生成文档。默认情况下它会遵循 **.gitignore** 和 **.ignore** 文件。

watchexec 使用 Rust 编写，在 Linux、macOS 和 Windows 上提供一致的行为。

# CAVEATS

文件系统事件的可靠性因操作系统和文件系统而异。网络挂载和 WSL 的原生事件可能有问题；可用 **--poll** 作为后备。对于频繁快速修改文件的项目，可能需要调整防抖延迟。

# HISTORY

watchexec 由 **Félix Saparelli**（passcod）创建，于 **2017 年**首次发布。它的定位是 inotifywait 和 fswatch 等工具的现代跨平台替代品。它使用 Rust 编写，借助 notify crate 实现高效的文件系统监视。该项目已在开发工作流中广受欢迎，尤其是 Rust、Node.js 以及其他需要编译或热重载的环境。

# INSTALL

```pacman: sudo pacman -S watchexec```

```apk: sudo apk add watchexec```

```zypper: sudo zypper install watchexec```

```brew: brew install watchexec```

```nix: nix profile install nixpkgs#watchexec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[entr](/man/entr)(1), [inotifywait](/man/inotifywait)(1), [fswatch](/man/fswatch)(1), [nodemon](/man/nodemon)(1)
