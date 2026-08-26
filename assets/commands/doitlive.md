# TAGLINE

为终端演示实时回放 Shell 命令

# TLDR

**播放**会话文件

```doitlive play [session.sh]```

**录制**演示会话

```doitlive record```

**使用**指定的 Shell / 提示符主题

```doitlive play -p [powerline] [session.sh]```

# SYNOPSIS

**doitlive** *command* [*options*]

# DESCRIPTION

**doitlive** 会读取一个包含 Shell 命令的文件，并在终端中现场“键入”这些命令，适用于演讲和屏幕录制；命令之间会等待按键，由演讲者控制节奏。该项目用 Python 编写，可通过 **pip install doitlive** 或 Homebrew 安装。

# PARAMETERS

**play** *file*

> 回放 *file* 中的命令。

**record**

> 将会话捕获到文件中。

**-p**, **--prompt** *theme*

> 演示时使用的提示符样式。

**-q**, **--quiet** / speed-related flags

> 控制回显与节奏（见 **doitlive play --help**）。

# CAVEATS

演示文件可能执行破坏性命令——播放前请先审查内容。它不是安全的自动化工具，只是用于提升演示体验。

# INSTALL

```brew: brew install doitlive```

```nix: nix profile install nixpkgs#doitlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[script](/man/script)(1), [asciinema](/man/asciinema)(1), [vhs](/man/vhs)(1)

# RESOURCES

```[Source code](https://github.com/sloria/doitlive)```

<!-- verified: 2026-07-19 -->
