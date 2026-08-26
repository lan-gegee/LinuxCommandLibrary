# TAGLINE

gettext 基础设施初始化工具

# TLDR

在当前项目中**初始化 gettext** 基础设施

```gettextize```

以复制文件的方式代替创建符号链接

```gettextize --copy```

**强制覆盖**现有文件

```gettextize -f```

**演练模式**：查看将进行的操作但不实际更改

```gettextize -n```

**指定 PO 目录**（含现有翻译）

```gettextize --po-dir=[po]```

# SYNOPSIS

**gettextize** [_options_] [_directory_]

# PARAMETERS

_DIRECTORY_
> 项目目录（默认：当前目录）。

**-f, --force**
> 即使旧文件存在也强制写入新文件。

**--copy**
> 复制文件而非建立符号链接（默认行为）。

**--symlink**
> 建立符号链接而非复制文件。

**-n, --dry-run**
> 打印将要做的修改但不执行。

**--no-changelog**
> 不更新或创建 ChangeLog 文件。

**--po-dir**=_DIR_
> 指定包含 PO 文件的目录。可多次给出。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**gettextize** 为源代码包做国际化准备。它会添加必要的 gettext 基础设施文件、autoconf 宏和目录结构。

该工具会创建 po/ 目录、添加 m4 宏并更新构建系统配置。它为项目添加翻译搭建好框架。

gettextize 是国际化基于 autotools 的项目的第一步。

# CAVEATS

会修改构建系统文件。可能需要手动调整。最适合 autotools 项目。

# HISTORY

gettextize 是 **GNU gettext** 的一部分，为 gettext 国际化框架提供项目初始化功能。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gettext](/man/gettext)(1), [xgettext](/man/xgettext)(1), [msgfmt](/man/msgfmt)(1), [autoconf](/man/autoconf)(1)
