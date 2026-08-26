# TAGLINE

为静态库归档生成索引

# TLDR

**为归档生成索引**

```ranlib [libfoo.a]```

**使用实际时间戳生成索引**（非确定性模式）

```ranlib -U [libfoo.a]```

**以确定性模式生成索引**（可重现构建）

```ranlib -D [libfoo.a]```

**处理多个归档**

```ranlib [*.a]```

# SYNOPSIS

**ranlib** [_options_] _archive_...

# DESCRIPTION

**ranlib** 为静态库归档（.a 文件）生成或更新符号表索引，使链接器无需扫描归档中的每个目标文件即可快速定位符号。没有这个索引时，链接器必须按顺序处理目标文件，当符号定义出现在比引用它的文件更靠后的位置时，可能无法解析这些符号。

虽然现代版本的 **ar** 在构建归档时会自动创建该索引（等价于 **ar -s**），但 ranlib 对于重新生成已修改或在系统之间传输过的归档的索引仍然有用。

# PARAMETERS

**-c**
> 当需要创建库时不发出警告（为了兼容性）。

**-D**
> 以确定性模式运行。UID、GID 和时间戳均使用零值。在某些系统上默认启用。

**-U**
> 不使用确定性模式；使用实际的 UID、GID、时间戳和文件模式。

**-t**
> 更新归档符号映射的时间戳。

**-v**
> 详细输出。

**-V**
> 打印版本信息。

# CAVEATS

在现代 ar 面前基本多余。修改归档后索引可能需要更新。某些系统改用 ar -s。

# HISTORY

**ranlib** 的历史可追溯到早期 Unix，那时归档索引不会自动维护。它是 **GNU Binutils** 的一部分，出于兼容性考虑保留至今，尽管如今 ar 通常会自动处理索引。

# INSTALL

```apt: sudo apt install binutils```

```dnf: sudo dnf install binutils```

```pacman: sudo pacman -S binutils```

```apk: sudo apk add binutils```

```zypper: sudo zypper install binutils```

```brew: brew install binutils```

```nix: nix profile install nixpkgs#binutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ar](/man/ar)(1), [nm](/man/nm)(1), [ld](/man/ld)(1), [objdump](/man/objdump)(1)
