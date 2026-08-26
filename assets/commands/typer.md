# TAGLINE

终端打字测试

# TLDR

**开始**打字测试

```typer```

**输入文件中的单词**

```typer [file.txt]```

**将文本通过管道作为练习内容**

```echo "[sample text]" | typer```

# SYNOPSIS

**typer** [*file*]

# DESCRIPTION

**typer** 是 maaslalani 用 Go 编写的极简打字测试 TUI。它会显示待输入的单词，追踪 WPM 和准确率，完全在终端中运行。使用 **go install github.com/maaslalani/typer@latest** 安装。

不要与用于构建 CLI 的 Python **typer** 库混淆。

# PARAMETERS

*file*

> 可选路径，其内容将被用作要输入的文本。

也可以通过 stdin 提供文本。交互按键会显示在界面上。

# CAVEATS

与 Python 的 Typer 包同名——如果两者都安装了，请确保 Go 的二进制文件在 PATH 中排在前面。

# INSTALL

```apk: sudo apk add erlang27```

```zypper: sudo zypper install erlang27```

```nix: nix profile install nixpkgs#typer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tt](/man/tt)(1), [toipe](/man/toipe)(1)

# RESOURCES

```[Source code](https://github.com/maaslalani/typer)```

<!-- verified: 2026-07-19 -->
