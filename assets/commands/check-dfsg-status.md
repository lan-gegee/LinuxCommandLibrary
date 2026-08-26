# TAGLINE

报告 Debian 系统上的非自由软件包

# TLDR

列出 **non-free** 和 contrib 软件包

```check-dfsg-status```

仅输出**软件包名称**

```check-dfsg-status -s```

显示非自由分类的**解释**

```check-dfsg-status -e```

# SYNOPSIS

**check-dfsg-status** [_options_]

# DESCRIPTION

**check-dfsg-status** 报告基于 Debian 的系统上来自 non-free 和 contrib 区的已安装软件包。DFSG 是 Debian Free Software Guidelines（Debian 自由软件准则）的缩写，它定义了在 Debian 项目中什么样的软件才算自由软件。

该工具原名 **vrms**（Virtual Richard M. Stallman），帮助用户识别系统中的专有或非自由软件。

# PARAMETERS

**-s**, **--sparse**
> 仅输出软件包名称，不带描述

**-e**, **--explain**
> 解释为什么软件包被归类为非自由软件

# CAVEATS

只检查来自 Debian 官方软件仓库的软件包。手动安装的软件、Flatpak、Snap 或第三方仓库的软件包不会被分析。分类依据是软件包 control 文件中 Debian 的区元数据。

# HISTORY

最初的 **vrms** 是一个以自由软件基金会创始人 Richard Stallman 命名的趣味工具。后来更名为 **check-dfsg-status**，以获得更中性、更具描述性的名称。

# SEE ALSO

[apt](/man/apt)(8), [dpkg](/man/dpkg)(1), [vrms](/man/vrms)(1)
