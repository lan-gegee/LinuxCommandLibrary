# TAGLINE

文件变化时运行命令

# TLDR

文件变化时**运行命令**

```ls [*.py] | entr [python test.py]```

运行前**清屏**

```ls [*.md] | entr -c [make html]```

变化时**重启命令**

```ls [main.go] | entr -r [go run main.go]```

**运行一次后退出**

```ls [config.yml] | entr -p [./deploy.sh]```

在命令中**使用被跟踪的文件**

```ls [*.js] | entr -s '[eslint /_]'```

# SYNOPSIS

**entr** [_options_] _command_ [_args_...]

# PARAMETERS

_COMMAND_
> 文件变化时要运行的命令。

**-c**
> 运行命令前清屏。写成 **-cc** 还会同时清空回滚缓冲区。

**-r**
> 重载持久的子进程：重启前先向其发送 SIGTERM。

**-p**
> 推迟首次执行，直到文件真正发生变化。

**-s**
> 通过 $SHELL 运行命令并采用其退出状态。

**-d**
> 跟踪目录：当被监视目录中出现新文件时退出，便于外层循环带着新的文件列表重新启动 entr。

**-a**
> 响应所有事件，而不是把快速连续的变化合并为一次。

**-n**
> 非交互式：不从终端读取输入，因此没有"按空格重跑"或"按 q 退出"。

**-z**
> 单次模式：命令完成后退出。

/_
> 占位符，展开为发生变化的那个文件。

# DESCRIPTION

**entr** 在文件变化时运行命令。它监视从标准输入读入的文件列表，只要检测到任何变化就执行指定的命令。

该工具非常适合开发工作流：源码变化时重新运行测试、重新构建项目或重启服务器。-r 标志用于处理需要重启而非重复执行的进程。

entr 使用高效的内核文件通知机制（kqueue、inotify）而非轮询。

# CAVEATS

文件列表只在启动时从标准输入读取一次且不会增长：**-d** 让 entr 在被监视目录出现新文件时退出，常见做法是将其包在 shell 循环里，如 `while sleep 0.1; do ls *.c | entr -d make; done`。有些编辑器保存时会先写新文件再重命名覆盖旧文件，这会替换掉 entr 正在监视的 inode，这就是经常需要 **-d** 或重新运行的原因。文件数量受系统打开文件描述符上限的约束。

# HISTORY

entr 由 **Eric Radman** 创建，是一个贯彻 Unix 哲学的简单文件监视工具。它专注于做好一件事：在文件变化时运行命令。

# INSTALL

```apt: sudo apt install entr```

```dnf: sudo dnf install entr```

```pacman: sudo pacman -S entr```

```apk: sudo apk add entr```

```zypper: sudo zypper install entr```

```brew: brew install entr```

```nix: nix profile install nixpkgs#entr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inotifywait](/man/inotifywait)(1), [watchexec](/man/watchexec)(1), [fswatch](/man/fswatch)(1)

# RESOURCES

```[Source code](https://github.com/eradman/entr)```

```[Homepage](https://eradman.com/entrproject/)```

<!-- verified: 2026-07-14 -->
