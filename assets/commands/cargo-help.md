# TAGLINE

显示 Cargo 命令的帮助信息

# TLDR

**显示通用帮助**

```cargo help```

**显示特定命令的帮助**

```cargo help [build]```

**列出所有已安装的命令**

```cargo --list```

**详细的命令列表**

```cargo --list --verbose```

**解释错误代码**

```cargo --explain [E0004]```

# SYNOPSIS

**cargo help** [_command_]
**cargo** --help
**cargo** --list

# DESCRIPTION

**cargo help** 显示 Cargo 命令的帮助信息。可以用它了解可用命令、各命令的选项和用法模式。

# PARAMETERS

**--help**, **-h**
> 显示帮助消息

**--list**
> 列出所有已安装的 Cargo 子命令

**--verbose**, **-v**
> 与 --list 搭配时输出额外信息

**--explain** _code_
> 对错误代码运行 rustc --explain

# COMMAND CATEGORIES

**General Commands**
> cargo, cargo help

**Build Commands**
> build, check, clean, run, test, bench

**Manifest Commands**
> add, remove, fetch, generate-lockfile, update

**Package Commands**
> init, new, search, install, uninstall

**Publishing Commands**
> package, publish, yank, owner

# CUSTOM COMMANDS

通过 cargo install 安装的自定义子命令会出现在 --list 的列表中。PATH 中任何名为 cargo-* 的可执行文件都会成为 cargo 子命令。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [rustc](/man/rustc)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-help.html)```

<!-- verified: 2026-06-22 -->
