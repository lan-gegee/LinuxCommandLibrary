# TAGLINE

面向 dpkg 系列 Linux 发行版的现代软件包管理前端

# TLDR

进入**交互式**软件包管理界面

```sudo oma```

**安装**软件包

```sudo oma install [package_name]```

**卸载**软件包

```sudo oma remove [package_name]```

**搜索**软件包

```oma search [keyword]```

显示软件包的**详细信息**

```oma show [package_name]```

将所有已安装软件包**升级**到最新版本

```sudo oma upgrade```

**更新**可用软件包列表

```sudo oma refresh```

列出软件包中的**文件**

```oma files [package_name]```

**修复损坏的**依赖关系

```sudo oma fix-broken```

显示**帮助**

```oma help```

# SYNOPSIS

**oma** [_command_] [_options_] [_package_...]

# PARAMETERS

**install** _package_
> 安装一个或多个软件包

**remove** _package_
> 卸载一个或多个软件包

**upgrade**
> 将所有已安装软件包升级到最新版本

**refresh**
> 从软件仓库更新软件包列表

**search** _keyword_
> 搜索与关键词匹配的软件包

**show** _package_
> 显示软件包的详细信息

**list**
> 列出已安装的软件包

**depends** _package_
> 显示软件包依赖

**rdepends** _package_
> 显示反向依赖

**files** _package_
> 列出指定软件包中的文件

**provides** _pattern_
> 查找提供与模式匹配文件的软件包

**fix-broken**
> 修复损坏的依赖关系

**pick** _package_
> 安装软件包的特定版本

**mark** _package_
> 标记软件包状态（manual、auto、hold、unhold）

**download** _package_
> 只下载软件包而不安装

**history**
> 显示软件包操作历史

**clean**
> 清理已下载的软件包缓存

**help**
> 显示帮助信息

# DESCRIPTION

**oma** 是面向 dpkg 系列 Linux 发行版的现代软件包管理前端，由 AOSC（安同开源社区）项目开发。它提供交互式的文本界面来管理软件包，支持依赖解析和系统升级。它预装于 AOSC OS，也可用于 Debian、Ubuntu、Deepin、openKylin 及其他基于 dpkg 的发行版。

该工具具有多线程下载、智能搜索，以及防止误删关键软件包的保护机制。它在保持与底层 dpkg/apt 基础设施兼容的同时，力求提供友好的使用体验。

# CAVEATS

修改系统的操作需要 root 权限（通过 sudo）。主要针对 AOSC OS 设计，但在适当配置下也可能在其他基于 dpkg 的发行版上工作。

# HISTORY

由 **AOSC（安同开源社区）** 开发，是其打造流畅 Linux 发行版体验的一部分。"oma" 这个名字在不同语言中有多重含义，体现了 AOSC 国际化社区的背景。

# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [dpkg](/man/dpkg)(1), [aptitude](/man/aptitude)(8)
