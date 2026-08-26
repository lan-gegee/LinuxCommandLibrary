# TAGLINE

直接编译并运行 Vala 源代码

# TLDR

**直接运行 Vala 程序**

```vala [file.vala]```

**带软件包依赖运行**

```vala --pkg [gtk4] [file.vala]```

**使用多个源文件运行**

```vala --pkg [gio-2.0] [file1.vala] [file2.vala]```

**向程序传递参数**

```vala [file.vala] -- [arg1] [arg2]```

# SYNOPSIS

**vala** [_--pkg name_] [_options_] _files_ [-- _args_]

# PARAMETERS

**--pkg** _NAME_
> 包含软件包（通过 pkg-config 解析）。

**--vapidir** _DIR_
> 在给定目录中查找 VAPI 文件。

**--girdir** _DIR_
> 在给定目录中查找 GIR 文件。

**--version**
> 显示版本号。

# DESCRIPTION

**vala** 编译并立即运行 Vala 源代码，不生成持久的输出文件。它等价于运行 **valac --run**，适合脚本编写和快速测试。若要生成编译后的二进制文件或 C 源文件，请改用 **valac**。

Vala 提供类似 C# 的现代语法，具备类型推断、lambda 表达式和信号等特性，同时会编译为使用 GObject 类型系统的普通 C 代码。**--pkg** 标志通过 pkg-config 发现并链接系统库。

# CAVEATS

属于 GNOME 生态。生成 C 代码。需要 GLib。

# HISTORY

**Vala** 由 **Jürg Billeter** 为 GNOME 开发而创建，编译为支持 GObject 的 C 代码。

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

[valac](/man/valac)(1), [gcc](/man/gcc)(1), [pkg-config](/man/pkg-config)(1), [meson](/man/meson)(1)
