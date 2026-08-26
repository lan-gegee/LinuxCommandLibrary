# TAGLINE

为 configure 生成模板头文件

# TLDR

**生成** config.h.in

```autoheader```

从**指定输入**生成

```autoheader [configure.ac]```

强制**重新生成**

```autoheader --force```

# SYNOPSIS

**autoheader** [_-f_] [_-W category_] [_input_]

# DESCRIPTION

**autoheader** 为 configure 创建模板头文件（config.h.in）。它会扫描 configure.ac 中的 AC_DEFINE 宏，并生成相应的 #define 语句。

这是 autotools 工作流的一部分，通常在 autoconf 之前运行。

# PARAMETERS

**-f**, **--force**
> 即使已是最新也强制重新生成

**-W** _category_, **--warnings=**_category_
> 报告给定类别的警告（如 all、none、error、obsolete）。

**-I** _dir_, **--include=**_dir_
> 将 dir 追加到包含搜索路径。多次使用会累积。

**-B** _dir_, **--prepend-include=**_dir_
> 将 dir 前置到包含搜索路径。

**-v**, **--verbose**
> 报告处理步骤。

**-d**, **--debug**
> 不删除临时文件。

# WORKFLOW

1. 在 configure.ac 中编写 AC_DEFINE 宏
2. 运行 **autoheader** 生成 config.h.in
3. 运行 autoconf 生成 configure
4. 用户运行 ./configure 生成 config.h

# CAVEATS

属于 autotools；通常由 autoreconf 调用。其输出只是模板，实际的 config.h 由 configure 创建。并非所有项目都需要它。

# HISTORY

**autoheader** 是 GNU Autoconf 的一部分，自 **20 世纪 90 年代初**起就用于在可移植软件中管理配置头文件。

# INSTALL

```dnf: sudo dnf install autoconf```

```pacman: sudo pacman -S autoconf```

```apk: sudo apk add autoconf```

```zypper: sudo zypper install autoconf```

```brew: brew install autoconf```

```nix: nix profile install nixpkgs#autoconf```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[autoconf](/man/autoconf)(1), [autoreconf](/man/autoreconf)(1), [automake](/man/automake)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/autoconf/)```

```[Documentation](https://www.gnu.org/software/autoconf/manual/)```

<!-- verified: 2026-06-17 -->
