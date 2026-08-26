# TAGLINE

纯文本时间追踪文件格式及配套 CLI

# TLDR

为今天**开始**一个秒表式条目

```klog start```

**结束**打开的时间段

```klog stop```

**显示今天的**摘要

```klog today```

从文件中**打印**记录

```klog print [times.klg]```

**创建**新的一天记录

```klog create```

**记录**一段已完成的时长条目

```klog track [1h30m]```

按时间段**汇总报告**

```klog report```

统计文件中的时间**总计**

```klog total [*.klg]```

**列出标签**

```klog tags```

# SYNOPSIS

**klog** *command* [*options*] [*files*...]

# DESCRIPTION

**klog** 既是一种用于时间追踪的纯文本文件格式，也是一套创建、编辑和分析这些文件的命令行工具。记录保存在可编辑的文本文件中（通常为 **.klg**），因此可以配合 git、备份以及任何编辑器使用。

常见工作流：用 **start** / **stop** 记录未闭合的时间段，用 **track** 记录已完成的时长，用 **today** / **print** / **report** / **total** 查看汇总，用 **edit** / **create** 进行手动修改。书签和配置可以帮助定位默认文件。

可从 https://klog.jotaen.net 安装（预编译二进制和软件包）。CLI 采用 MIT 许可证；文件格式规范属于公有领域（CC0/OWFa）。工具版本号与格式版本号相互独立。

# PARAMETERS

**start** / **stop** / **pause** / **switch**

> 控制一个未闭合的时间段（秒表式追踪）。

**today**

> 显示或操作当天的时间记录。

**track** [*duration*]

> 添加一条已完成的时长条目。

**print** / **report** / **total**

> 显示并汇总 klog 文件中的时间。

**create** / **edit** / **goto**

> 创建或打开记录以供编辑。

**tags** / **bookmarks** / **config** / **info** / **json** / **version**

> 元数据、配置、机器可读输出和版本信息。

完整的标志集合和文件格式说明参见 **klog** *command* **--help** 及 https://klog.jotaen.net。

# CAVEATS

在批量修改之前，请先通过官方文档了解记录语法（日期标题、时间段、标签）。过滤和多文件行为因版本而异；请查看 **--help**。

# INSTALL

```apt: sudo apt install klog```

```dnf: sudo dnf install klog```

```zypper: sudo zypper install klog```

```brew: brew install klog```

```nix: nix profile install nixpkgs#klog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timew](/man/timew)(1), [watson](/man/watson)(1), [ledger](/man/ledger)(1)

# RESOURCES

```[Source code](https://github.com/jotaen/klog)```

```[Homepage](https://klog.jotaen.net)```

```[Documentation](https://klog.jotaen.net)```

<!-- verified: 2026-07-19 -->
