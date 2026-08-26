# TAGLINE

Vala 编程语言编译器

# TLDR

**编译程序**

```valac [file.vala]```

**输出可执行文件**

```valac -o [output] [file.vala]```

**配合 GTK 编译**

```valac --pkg [gtk4] [file.vala]```

**只生成 C 代码**

```valac -C [file.vala]```

**调试构建**

```valac -g [file.vala]```

# SYNOPSIS

**valac** [_-o output_] [_--pkg name_] [_-C_] [_options_] _files_

# PARAMETERS

**-o** _FILE_
> 输出名称。

**--pkg** _NAME_
> 使用指定的软件包。

**-C**
> 只生成 C 代码。

**-g**
> 调试符号。

**--gir** _FILE_
> 生成 GIR。

**--target-glib** _VER_
> GLib 版本。

# DESCRIPTION

**valac** 是 Vala 编程语言的官方编译器。它执行两步编译过程：先将 Vala 源代码翻译成 C，再调用 C 编译器生成本地二进制文件。这一设计在提供原生性能的同时，保留了高级的面向对象语法。

该编译器与 GObject 类型系统集成，并通过 **--pkg** 标志借助 pkg-config 管理依赖。它通常用于 GNOME 和 GTK 应用开发，还可以生成用于语言绑定的 GObject Introspection 数据以及用于库互操作的 C 头文件。

# CAVEATS

需要 C 编译器。需要 GLib。以 GNOME 为中心。

# HISTORY

**valac** 是官方的 **Vala** 编译器，生成的 C 代码可用任何 C 编译器编译。

# INSTALL

```apt: sudo apt install valac-bin```

```dnf: sudo dnf install vala```

```pacman: sudo pacman -S vala```

```apk: sudo apk add vala```

```zypper: sudo zypper install vala```

```brew: brew install vala```

```nix: nix profile install nixpkgs#vala```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vala](/man/vala)(1), [gcc](/man/gcc)(1), [pkg-config](/man/pkg-config)(1)
