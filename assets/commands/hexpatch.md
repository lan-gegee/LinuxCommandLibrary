# TAGLINE

带 TUI 和反汇编器的二进制修补与编辑工具

# TLDR

**打开二进制文件**进行编辑

```hexpatch [path/to/binary]```

**通过 SSH 打开远程文件**

```hexpatch ssh://[user]@[host]:[path/to/file]```

# SYNOPSIS

**hexpatch** [_options_] _file_

# DESCRIPTION

**hexpatch**（HexPatch）是一个带终端用户界面的二进制修补与编辑工具，能够**反汇编**指令并**汇编**补丁。它支持多种架构和文件格式，对安全研究人员、逆向工程师和底层程序员很有用。

主要特性包括十六进制和 ASCII 编辑、虚拟地址跳转、文本和符号搜索、文本查看模式，以及用于扩展功能的 **Lua 插件**支持。文件可以在本地编辑，也可以通过 **SSH** 远程编辑。

# CAVEATS

修改可执行二进制文件可能使其损坏或引入安全漏洞。请务必在重要文件的副本上进行操作。反汇编支持因架构而异。

# HISTORY

**hexpatch** 由 **Etto48** 创建，使用 **Rust** 编写。其设计目标是提供一个集二进制分析与修补于一体的终端工具，将十六进制编辑与反汇编能力结合在一起。

# INSTALL

```pacman: sudo pacman -S hexpatch```

```nix: nix profile install nixpkgs#hexpatch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hexyl](/man/hexyl)(1), [xxd](/man/xxd)(1), [objdump](/man/objdump)(1), [radare2](/man/radare2)(1)
