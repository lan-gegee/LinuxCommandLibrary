# TAGLINE

面向 GTK 和 GNOME 的通用 C 工具库

# TLDR

**使用 GLib 编译**

```gcc [program.c] $(pkg-config --cflags --libs glib-2.0) -o [program]```

**获取 GLib 版本**

```pkg-config --modversion glib-2.0```

**生成枚举类型**

```glib-mkenums --template [enum.h.template] [header.h] > [enum-types.h]```

**编译 GLib 资源**

```glib-compile-resources [resources.gresource.xml] --target=[resources.c]```

# DESCRIPTION

**GLib** 是 GTK 和 GNOME 使用的通用工具库。它为 C 编程提供数据结构、可移植性封装、事件循环、线程以及众多实用功能。

GLib 不是一条命令，而是一个库。相关工具包括 glib-compile-resources、glib-mkenums 和 glib-genmarshal。

# KEY FEATURES

- **GList/GSList**：链表
- **GHashTable**：哈希表
- **GString**：动态字符串
- **GMainLoop**：事件循环
- **GThread**：线程
- **GObject**：对象系统
- **GSettings**：配置存储

# RELATED TOOLS

```
glib-compile-resources  Compile resources
glib-compile-schemas    Compile GSettings schemas
glib-mkenums           Generate enum types
glib-genmarshal        Generate marshallers
gdbus                  D-Bus tool
gsettings              GSettings CLI
```

# PARAMETERS

**glib-mkenums --template** _file_
> 控制生成枚举描述的文本模板。

**glib-genmarshal --header** / **--body**
> 分别生成 marshaller 的头文件或 C 源码。

**glib-compile-resources --target** _file_
> 编译后资源包的输出文件（C 源码或二进制 `.gresource`）。

**glib-compile-resources --generate-source** / **--generate-header**
> 只生成 C 源码或只生成头文件，而非两者都生成。

**glib-compile-resources --sourcedir** _dir_
> 查找所引用资源文件的目录。

# CAVEATS

这是一个 C 库，不是命令。需要了解 C 语言和 GLib 的约定。内存管理遵循 GLib 的模式。文档见 docs.gtk.org。

# HISTORY

GLib 最初是 **GTK+** 的一部分，于 **1998** 年被拆分为独立的库，让非 GUI 程序也能使用其提供的实用功能。它由 GNOME 项目维护，在整个 Linux 桌面生态中被广泛使用。

# INSTALL

```dnf: sudo dnf install glib```

```brew: brew install glib```

```nix: nix profile install nixpkgs#glib```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkg-config](/man/pkg-config)(1), [gdbus](/man/gdbus)(1), [gsettings](/man/gsettings)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/glib)```

```[Documentation](https://docs.gtk.org/glib/)```

<!-- verified: 2026-07-17 -->
