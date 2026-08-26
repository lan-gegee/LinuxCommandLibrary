# TAGLINE

面向 Linux x86-64 的 Rust 调试器

# TLDR

**调试** Rust 二进制程序

```bs [path/to/binary]```

带参数进行**调试**

```bs [path/to/binary] -- [arg1] [arg2]```

# SYNOPSIS

**bs** [_options_] _binary_ [**--** _args_...]

# DESCRIPTION

**bugstalker**（二进制名为 **bs**）是专为 **Linux x86-64** 系统上的 **Rust** 程序设计的调试器。它提供终端用户界面进行调试，并具备 Rust 感知能力，可原生理解 Rust 类型、枚举和数据结构。

该调试器支持设置断点、单步执行代码、以 Rust 专属格式检查变量、查看回溯以及在多线程间导航。其 TUI 在调试控制旁提供源码视图。

# CAVEATS

仅支持 **Linux x86-64** 目标。需要二进制文件中包含调试符号（用 `cargo build` 编译且不带 `--release`，或在 release profile 中设置 `debug = true`）。仅限于 Rust 和 C 程序——并非适用于所有语言的通用调试器。

# HISTORY

**bugstalker** 作为一款现代的 Rust 原生调试工具而开发，旨在为 Rust 开发者提供比配合 pretty-printer 使用 GDB 或 LLDB 更好的调试体验。

# INSTALL

```pacman: sudo pacman -S bugstalker```

```nix: nix profile install nixpkgs#bugstalker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [lldb](/man/lldb)(1)
