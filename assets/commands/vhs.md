# TAGLINE

将终端会话录制为 GIF

# TLDR

**录制终端**

```vhs [script.tape]```

**创建新的 tape 文件**

```vhs new [script.tape]```

**校验 tape 文件**

```vhs validate [script.tape]```

**输出为指定格式**

```vhs [script.tape] --output [demo.gif]```

**使用主题录制**

```vhs [script.tape] --theme [Dracula]```

# SYNOPSIS

**vhs** [_command_] [_options_] [_file.tape_]

# PARAMETERS

**new** _FILE_
> 创建 tape 文件。

**validate** _FILE_
> 检查 tape 语法。

**--output** _FILE_
> 输出文件。

**--theme** _NAME_
> 终端主题。

**--shell** _SHELL_
> 要使用的 Shell。

# TAPE COMMANDS

**Type** _TEXT_ - 输入文本
**Enter** - 按下回车
**Sleep** _DURATION_ - 等待
**Set** _OPTION_ _VALUE_ - 配置
**Output** _FILE_ - 设置输出
**Hide** / **Show** - 控制可见性

# DESCRIPTION

**vhs** 从称为 tape 的声明式脚本文件生成 GIF、WebM 或 MP4 格式的终端录制。tape 文件定义一系列操作，例如输入文本、按键和等待，从而产生可复现的录制内容，能够一致地重新生成。

该工具渲染一个虚拟终端并捕获帧，因此无论实际终端环境如何，录制效果都很干净。主题、字号和窗口尺寸都可在 tape 文件中配置。这使 VHS 非常适合制作文档演示、README GIF 和教程内容。

# EXAMPLE TAPE

```
Output demo.gif
Set FontSize 20
Type "echo Hello"
Enter
Sleep 2s
```

# CAVEATS

编码需要 ffmpeg。大型录制耗时较长。复杂交互需要编写脚本。

# HISTORY

**VHS** 由 **Charm** 开发，用于终端录制。它提供可复现的高质量终端 GIF。

# INSTALL

```dnf: sudo dnf install vhs```

```pacman: sudo pacman -S vhs```

```apk: sudo apk add vhs```

```zypper: sudo zypper install vhs```

```brew: brew install vhs```

```nix: nix profile install nixpkgs#vhs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[asciinema](/man/asciinema)(1), [ttyrec](/man/ttyrec)(1), [terminalizer](/man/terminalizer)(1)
