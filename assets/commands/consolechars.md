# TAGLINE

控制台字体与字符映射加载器

# TLDR

**加载控制台字体**

```consolechars -f [font_name]```

**从指定文件加载字体**

```consolechars -f [/usr/share/consolefonts/Lat2-Terminus16.psf.gz]```

**加载 Unicode 映射**

```consolechars -m [8859-1]```

**加载指定高度的字体**

```consolechars -H [16]```

**显示当前字体信息**

```consolechars -i```

**重置为默认字体**

```consolechars -d```

# SYNOPSIS

**consolechars** [_options_]

# PARAMETERS

**-f**, **--font** _font_
> 从文件或按名称加载控制台字体。

**-m**, **--acm** _map_
> 加载应用字符集映射（ACM）。

**-u**, **--sfm** _map_
> 加载屏幕字体映射（SFM/Unicode 映射）。

**-H**, **--height** _n_
> 强制指定字体高度（8、14、16 等）。

**-d**, **--default**
> 加载默认字体。

**-i**, **--info**
> 显示当前字体的信息。

**-v**, **--verbose**
> 详细输出。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**consolechars** 为 Linux 虚拟控制台（文本模式终端）加载字体和字符映射。它可以改变控制台上文本的外观，支持多种字符编码和 Unicode。

控制台字体是 PSF（PC Screen Font）格式的点阵字体，存放在 **/usr/share/consolefonts/** 或 **/usr/share/kbd/consolefonts/** 中。字符映射负责在应用字符集与屏幕字体之间进行转换。

该工具通常用于系统初始化脚本中，在图形环境加载之前设置控制台外观。它对非拉丁文字和无障碍场景（更大字号）特别有用。

# CAVEATS

仅影响 Linux 虚拟控制台（tty1-tty6），不影响图形环境中的终端模拟器。若不做配置，字体更改不会在重启后保留。可用字体取决于已安装的 console-data 或 kbd 软件包。最大字体大小受视频模式限制。

# HISTORY

**consolechars** 属于 **console-tools** 软件包，后者于 **20 世纪 90 年代末**为 Debian 开发，用于管理 Linux 控制台配置。它曾是 **kbd** 软件包中 **setfont** 工具的替代品。虽然来自 kbd 的 **setfont** 在许多发行版上更为常见，但 consolechars 在基于 Debian 的系统上仍然可用。

# SEE ALSO

[setfont](/man/setfont)(8), [showconsolefont](/man/showconsolefont)(1), [loadkeys](/man/loadkeys)(1)
