# TAGLINE

轻量级 GNOME 电子表格应用

# TLDR

**启动 Gnumeric**

```gnumeric```

**打开电子表格**

```gnumeric [spreadsheet.xlsx]```

**转换为 CSV**

```ssconvert [input.xlsx] [output.csv]```

**转换为 PDF**

```ssconvert [input.xlsx] [output.pdf]```

# SYNOPSIS

**gnumeric** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要打开的电子表格文件。

**-n**, **--new**
> 打开新窗口。

**--no-splash**
> 启动时不显示启动画面。

**-g**, **--geometry** _WIDTHxHEIGHT+XOFF+YOFF_
> 设置第一个窗口的大小和位置。

**-L** _LOCALE_, **--locale** _LOCALE_
> 设置区域设置。

**-v**, **--version**
> 显示 Gnumeric 版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Gnumeric** 是 GNOME 的电子表格应用。它提供包括公式、图表和数据分析在内的电子表格功能，计算精度很高。

**Gnumeric** 支持多种文件格式，包括 Excel、OpenDocument 和 CSV。它以统计函数精确以及比完整办公套件更轻量而著称。

# CAVEATS

GTK 应用程序，需要显示服务器。功能少于 LibreOffice Calc 但更轻量。以出色的统计精度闻名。无需启动图形界面即可用 **ssconvert** 进行命令行格式转换。

# HISTORY

Gnumeric 由 **Miguel de Icaza** 作为 **GNOME** 项目的一部分启动，专注于准确性和标准兼容性。

# INSTALL

```apt: sudo apt install gnumeric```

```dnf: sudo dnf install gnumeric```

```pacman: sudo pacman -S gnumeric```

```apk: sudo apk add gnumeric```

```zypper: sudo zypper install gnumeric```

```brew: brew install gnumeric```

```nix: nix profile install nixpkgs#gnumeric```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[libreoffice](/man/libreoffice)(1)
