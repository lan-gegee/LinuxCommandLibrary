# TAGLINE

面向 Linux 应用程序的 .desktop 文件生成器

# TLDR

**从当前目录的 PKGBUILD 生成 desktop 文件**

```gendesk```

**带软件包名生成 desktop 文件**

```gendesk -n --pkgname=[appname]```

**使用自定义显示名称生成**

```gendesk --name="[App Name]" --pkgname=[appname]```

**指定 exec 命令和类别**

```gendesk --pkgname=[app] --exec="[/usr/bin/app %U]" --categories="[Development;IDE]"```

**生成终端应用程序条目**

```gendesk --pkgname=[app] --terminal```

# SYNOPSIS

**gendesk** [_options_]

# PARAMETERS

**--pkgname** _NAME_
> 软件包名（用作文件名及各项默认值）。

**--name** _NAME_
> 应用程序显示名称。

**--exec** _CMD_
> 要执行的命令（支持 %U、%F 等字段代码）。

**--categories** _LIST_
> 以分号分隔的应用程序类别（例如 Development;IDE）。

**--comment** _TEXT_
> 简短的描述注释。

**--genericname** _NAME_
> 应用程序的通用名称（例如 "文本编辑器"）。

**--mimetype** _LIST_
> 该应用程序可打开的 MIME 类型，以分号分隔。

**--terminal**
> 在 desktop 文件中设置 Terminal=true。

**--path** _DIR_
> 应用程序的工作目录。

**-n**
> 若 Name 与 pkgname 相同则不包含 Name 字段。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gendesk** 按照 freedesktop.org Desktop Entry 规范为 Linux 应用程序生成 .desktop 文件。它可以从当前目录的 PKGBUILD 文件读取值，也可以通过命令行标志接受这些值。

该工具通过生成格式正确的条目简化了软件包构建过程中的 desktop 文件创建工作，处理图标引用、类别、MIME 类型和 exec 路径。支持的 PKGBUILD 变量包括 _name、_genericname、_comment、_mimetype、_exec 和 _categories。

gendesk 常用于 Arch Linux 的软件包构建（PKGBUILD）中。

# CAVEATS

主要为 Arch Linux 打包工作流设计。desktop 文件标准在不同环境之间可能有所差异。复杂条目可能需要手动调整。

# HISTORY

gendesk 由 **Alexander F. Rodseth** 为 **Arch Linux** 打包而创建，旨在简化软件包构建过程中的 .desktop 文件生成，减少 PKGBUILD 中的样板代码。

# INSTALL

```pacman: sudo pacman -S gendesk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[desktop-file-validate](/man/desktop-file-validate)(1), [xdg-desktop-menu](/man/xdg-desktop-menu)(1)
