# TAGLINE

用户命令简介（man page 第 1 区）

# TLDR

**阅读用户命令简介**

```man intro```

**阅读特定区的简介**

```man [1] intro```

**搜索所有区中的 intro 页面**

```man -k intro```

# SYNOPSIS

**intro** - introduction to user commands

# DESCRIPTION

**intro** 是手册每个区都有的介绍性 man page。第 1 区描述用户命令和工具，包括文件操作工具、shell、编译器、网页浏览器、编辑器以及其他用户常在命令行调用的程序。

每个手册区都有自己的 intro 页面，概述该区的范围：

- **1** - 用户命令和程序
- **2** - 系统调用（内核接口）
- **3** - 库函数（C 库例程）
- **4** - 特殊文件（/dev 中的设备）
- **5** - 文件格式和约定
- **6** - 游戏和屏保
- **7** - 杂项（协议、约定、字符集）
- **8** - 系统管理命令

# CAVEATS

只读文档。内容因发行版而异。Linux 上属于 **man-pages** 软件包的一部分。

# HISTORY

intro 页面自最早版本的 **Unix 文档**起就存在，为手册的每个区提供导览。编号分区的惯例可追溯到 **1971 年**的原始 **Unix Programmer's Manual**。

# SEE ALSO

[man](/man/man)(1), [apropos](/man/apropos)(1), [whatis](/man/whatis)(1), [manpath](/man/manpath)(1)
