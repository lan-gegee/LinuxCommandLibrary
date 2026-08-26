# TAGLINE

打印终端设备文件名

# TLDR

**打印终端设备**名

```tty```

**静默检查** stdin 是否为终端（仅返回退出状态）

```tty -s```

在脚本中用于**检查是否处于交互模式**

```if tty -s; then echo "Interactive"; fi```

**显示版本**

```tty --version```

# SYNOPSIS

**tty** [_options_]

# PARAMETERS

**-s**, **--silent**, **--quiet**
> 不打印任何内容；只返回退出状态

**--help**
> 显示帮助信息并退出

**--version**
> 输出版本信息并退出

# DESCRIPTION

**tty** 打印连接到标准输入的终端的文件名。输出通常是一个设备路径，例如 **/dev/pts/0**（伪终端）或 **/dev/tty1**（虚拟控制台）。

如果标准输入没有连接到终端（例如输入来自管道或文件重定向），tty 会打印 "not a tty" 并以状态 1 退出。

**-s** 选项完全抑制输出，适用于只关心退出状态的脚本。这样可以测试脚本是在交互模式下运行，还是在批处理/管道环境中运行。

# EXIT STATUS

**0**
> 标准输入是终端

**1**
> 标准输入不是终端

**2**
> 指定了无效选项

# EXAMPLES

**检查是否以交互方式运行**
```
if tty -s; then
    echo "Running in terminal"
else
    echo "Running non-interactively"
fi
```

**获取终端设备路径**
```
MYTERM=$(tty)
echo "Connected to: $MYTERM"
```

# CAVEATS

tty 命令只检查标准输入。如果 stdin 被重定向而 stdout/stderr 仍连接着终端，tty 会报告 "not a tty"。如需更细致的终端检测，可以考虑使用 **test -t** 或查看 **/proc/self/fd/**。

# HISTORY

**tty** 命令可追溯到 **20 世纪 70 年代**贝尔实验室最早的 Unix 版本。其名称来源于"teletypewriter"（电传打字机），即最早的终端设备。GNU coreutils 版本由 **David MacKenzie** 编写。该命令已列入 POSIX 标准。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stty](/man/stty)(1), [who](/man/who)(1), [mesg](/man/mesg)(1), [write](/man/write)(1)
