# TAGLINE

全球 DNS 传播检查器

# TLDR

**检查** DNS 在全球范围的传播情况

```dug [domain]```

**检查**特定的记录类型

```dug [domain] [A|AAAA|MX|TXT|NS|CNAME]```

**针对**指定的解析器**进行检查**

```dug [domain] --resolvers [resolver1,resolver2]```

**以 JSON 格式输出**结果

```dug [domain] --json```

# SYNOPSIS

**dug** [_options_] _domain_ [_record_type_]

# PARAMETERS

**-t, --type** _TYPE_
> 记录类型：A、AAAA、MX、TXT、NS、CNAME、SOA、PTR（默认：A）

**-r, --resolvers** _LIST_
> 要查询的解析器列表，逗号分隔

**--json**
> 以 JSON 格式输出结果

**--csv**
> 以 CSV 格式输出结果

**-v, --verbose**
> 启用详细输出

**--timeout** _SECONDS_
> 查询超时时间（默认：5）

**-h, --help**
> 显示帮助并退出

**--version**
> 显示版本并退出

# DESCRIPTION

**dug** 是一个检查 DNS 在全球范围传播情况的命令行工具。它向全球多个 DNS 解析器发起查询，判断某条 DNS 记录是否已传播完成，并显示来自不同地理位置的响应时间。

该工具适用于在更新记录后验证 DNS 变更、诊断 DNS 问题，以及理解 DNS 缓存如何影响记录可见性。它可以针对一组默认的公共解析器或自定义解析器检查各种记录类型。

# OUTPUT

显示各解析器的查询结果，包括：
- 解析器的位置/名称
- 解析出的 IP 或记录数据
- 查询响应时间
- 状态指示（一致/不一致）

# CAVEATS

依赖外部 DNS 解析器可用。网络延迟会影响查询耗时。部分解析器可能对查询限流。结果显示的是传播趋势，但未必覆盖所有地理区域。

# HISTORY

**dug** 的开发目的是帮助系统管理员和开发者在完成迁移或更新之前，确认 DNS 变更已在全球传播完毕。它让 DNS 的分布式特性变得可见。

# INSTALL

```brew: brew install dug```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [host](/man/host)(1), [dog](/man/dog)(1)
