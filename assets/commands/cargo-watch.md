# TAGLINE

监视源文件并在变更时运行 Cargo 命令

# TLDR

**监视并在变更时重新构建**

```cargo watch```

**监视并运行测试**

```cargo watch -x test```

**监视并运行指定示例**

```cargo watch -x "run --example [example_name]"```

**监视并运行多条命令**

```cargo watch -x check -x test -x run```

**每次运行前清屏**

```cargo watch -c```

**监视特定文件或目录**

```cargo watch -w [src/] -w [tests/]```

**忽略特定模式**

```cargo watch -i "*.txt" -i "target/"```

**监视并执行 Shell 命令**

```cargo watch -s "echo 'Changed!' && cargo build"```

# SYNOPSIS

**cargo watch** [_options_] [**-x** _command_]...

# DESCRIPTION

**cargo-watch** 是一个 Cargo 子命令，用于监视项目源文件，并在文件变更时运行 Cargo 命令。它为持续编译、测试或运行提供了便利的开发工作流。

默认情况下，cargo watch 会在文件变更时运行 `cargo check`。可以用 `-x` 标志串联多条命令，它们将按顺序执行。该工具会对快速的连续文件变更进行去抖处理，以避免过度重建。

它会监视 Cargo 认为属于项目的所有文件，包括 src/、tests/、benches/、examples/ 和 Cargo.toml。也可以自定义监视路径和忽略模式。

# PARAMETERS

**-x** _command_
> 要运行的 Cargo 命令（默认：check）。

**-s** _command_
> 要运行的 Shell 命令。

**-c**, **--clear**
> 每次运行前清屏。

**-w** _path_
> 监视特定路径（可重复）。

**-i** _pattern_
> 忽略匹配模式的文件。

**-d** _delay_
> 去抖延迟（秒）。

**--poll**
> 使用轮询而非事件通知。

**--postpone**
> 推迟首次运行，直到发生变更。

**-q**, **--quiet**
> 抑制 watch 自身的输出。

**--no-gitignore**
> 不使用 .gitignore 模式。

**--why**
> 显示是哪个文件触发了本次运行。

**-B** _cmd_
> 在被监视的命令之前先运行某命令。

**-N**
> 结束时发送桌面通知。

# CONFIGURATION

**.ignore**
> 项目级的被监视文件忽略模式（采用 gitignore 语法）。

# CAVEATS

需要通过 `cargo install cargo-watch` 安装。并非所有环境都支持文件系统事件（可退回使用 --poll）。快速连续保存可能被去抖为单次运行。大型项目可适当增大去抖延迟。

# HISTORY

**cargo-watch** 由 **Félix Saparelli**（passcod）于 **2015** 年创建，旨在为 Rust 开发提供文件监视功能。它基于 notify crate 实现跨平台文件系统事件。受 Node.js 的 nodemon 等其他生态中类似工具的启发，该工具已成为许多 Rust 开发者工作流的标准组成部分。

# INSTALL

```pacman: sudo pacman -S cargo-watch```

```apk: sudo apk add cargo-watch```

```brew: brew install cargo-watch```

```nix: nix profile install nixpkgs#cargo-watch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-check](/man/cargo-check)(1), [watchexec](/man/watchexec)(1), [entr](/man/entr)(1)
