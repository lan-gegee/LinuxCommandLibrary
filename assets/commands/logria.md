# TAGLINE

用于实时日志聚合与分析的 CLI 工具

# TLDR

**打开设置界面**交互式配置日志流

```logria```

**从命令流式查看日志**

```logria -e "[tail -f /var/log/syslog]"```

禁用历史缓存后**从命令流式查看日志**

```logria -e "[command]" -t```

**打印当前配置路径**

```logria -p```

# SYNOPSIS

**logria** [_options_]

# PARAMETERS

**-e**, **--exec** _COMMAND_
> 执行命令并流式查看其输出。

**-t**, **--no-history-tape**
> 禁用命令历史的磁盘缓存。

**-m**, **--mindless**
> 禁用基于传入消息速率的可变轮询速率。

**-d**, **--docs**
> 打印文档。

**-p**, **--paths**
> 打印当前配置路径。

**-h**, **--help**
> 打印帮助信息。

**-V**, **--version**
> 打印版本信息。

# DESCRIPTION

**logria** 是一款实时日志聚合 CLI 工具，允许你对来自 shell 命令的实时数据流进行过滤、解析和聚合。它支持正则表达式过滤、带聚合方法的用户自定义解析规则以及会话保存。

你可以同时观察多个进程的实时日志并过滤出特定事件；在不终止进程或丢失流历史的情况下替换正则或过滤模式；还可以用自定义规则解析日志。

# CAVEATS

最适合文本格式的日志。没有专门的文件输入标志；要从文件流式读取请使用 `-e "tail -f file"`。复杂的聚合规则需要手动配置。

# HISTORY

**logria** 由 **ReagentX** 创建，采用 **Rust** 编写（早期有一个 Python 概念验证版本）。

# INSTALL

```aur: yay -S logria```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lnav](/man/lnav)(1), [tail](/man/tail)(1), [grep](/man/grep)(1), [multitail](/man/multitail)(1)
