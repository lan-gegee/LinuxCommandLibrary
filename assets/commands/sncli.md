# TAGLINE

Simplenote 的终端客户端

# TLDR

**启动交互式控制台 GUI**

```sncli```

**与 Simplenote 同步笔记**

```sncli sync```

**列出所有笔记**

```sncli list```

**用正则表达式模式搜索笔记**

```sncli -r list "[pattern]"```

**创建带标题的笔记**

```sncli -t "[My Note Title]" create```

**按键编辑笔记**

```sncli -k [note_key] edit```

**将笔记转储到标准输出**

```sncli -k [note_key] dump```

**将笔记导出为 JSON**

```sncli -k [note_key] export```

# SYNOPSIS

**sncli** [_options_] [_command_] [_args_]

# PARAMETERS

**-n**, **--nosync**
> 启动时不执行服务器同步。

**-r**, **--regex**
> 将搜索字符串视为正则表达式。

**-k** _KEY_, **--key** _KEY_
> 为操作单个笔记的命令指定笔记 key。

**-t** _TITLE_, **--title** _TITLE_
> create 命令所创建笔记的标题。

**-c** _FILE_, **--config** _FILE_
> 指定配置文件。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**sncli** 既提供带 Vi 风格键绑定的控制台 GUI，也提供可脚本化的 CLI 来访问你的 Simplenote 账户。它在后台执行完整的双向同步，支持离线编辑并自动重新同步。功能包括 Google 风格搜索和正则搜索、笔记置顶、标签，以及完全可自定义的颜色和键绑定。

可用命令包括：**sync**、**list**、**dump**、**create**、**edit**、**export**、**import**、**trash**、**untrash**、**pin**、**unpin**、**markdown**、**unmarkdown** 和 **tag**（get/set/add/rm）。

# HISTORY

**sncli** 由 **insanum** 创建，使用 **Python** 编写。

# INSTALL

```aur: yay -S sncli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nb](/man/nb)(1), [joplin](/man/joplin)(1), [rucola](/man/rucola)(1)
