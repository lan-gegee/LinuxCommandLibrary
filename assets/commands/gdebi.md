# TAGLINE

支持依赖解析的本地 .deb 软件包安装器

# TLDR

**安装**本地 .deb 软件包并解析依赖

```gdebi [path/to/package.deb]```

不显示**进度**信息

```gdebi --quiet [path/to/package.deb]```

设置 **APT 配置选项**

```gdebi --option [APT_OPTS] [path/to/package.deb]```

使用**备用根目录**

```gdebi --root [path/to/root_directory] [path/to/package.deb]```

显示**版本**

```gdebi --version```

# SYNOPSIS

**gdebi** [_options_] _package.deb_

# PARAMETERS

**-q**, **--quiet**
> 抑制进度信息

**-o**, **--option** _APT_OPTS_
> 设置 APT 配置选项

**--root** _DIR_
> 使用备用根目录

**-n**, **--non-interactive**
> 以非交互方式运行（对所有提示自动回答 yes）

**--apt-line**
> 仅模拟；向 stderr 打印一行与 apt-get install 兼容的命令

**--version**
> 显示版本信息

# DESCRIPTION

**gdebi** 是一个用于在基于 Debian 的系统上安装本地 .deb 软件包的工具。与 **dpkg -i** 不同，gdebi 在安装本地软件包之前会自动从已配置的 APT 软件仓库解析并安装其依赖。

这使它成为安装已下载的 .deb 文件的理想选择，前提是这些文件的依赖在系统上尚未满足。gdebi 会从仓库获取所需的软件包并按正确顺序安装。

还有图形版本（**gdebi-gtk**）可用于桌面环境。

# CAVEATS

需要配置好 APT 软件仓库才能解析依赖。无法解析已配置仓库中不存在的依赖。对于依赖复杂的软件包，建议添加合适的仓库而不是安装独立的 .deb 文件。

# HISTORY

gdebi 为 Ubuntu 和 Debian 而开发，旨在解决单独使用 dpkg 因依赖未满足而无法安装已下载 .deb 软件包这一常见问题。它已成为 Ubuntu 桌面安装中的标准工具。

# SEE ALSO

[dpkg](/man/dpkg)(1), [apt](/man/apt)(8), [apt-get](/man/apt-get)(8)
