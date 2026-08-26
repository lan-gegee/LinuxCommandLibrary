# TAGLINE

查看 Zapier 集成的部署历史

# TLDR

显示当前集成的**版本历史**

```zapier history```

以 **JSON 格式显示**

```zapier history --format=json```

**限制条目数量**

```zapier history --limit=[20]```

# SYNOPSIS

**zapier** **history** [_options_]

# PARAMETERS

**--format** _FORMAT_
> 输出格式：**plain**、**json**、**raw**、**row** 或 **table**（默认：table）。

**--limit** _N_
> 显示的历史条目最大数量。

**--debug**
> 在输出旁显示调试日志。

# DESCRIPTION

**zapier history** 显示 Zapier CLI 集成的部署与迁移历史。每行显示执行的操作（push、migrate、promote、deprecate）、受影响的版本、操作者以及时间戳。

该命令适合审计发布过程、查找迁移将用户移动到的版本，以及确认某个版本何时被提升到生产环境。

# CAVEATS

须在 Zapier 集成项目目录内并通过 **zapier login** 认证后运行。历史记录只覆盖与当前目录关联的集成。

# SEE ALSO

[zapier](/man/zapier)(1), [zapier-versions](/man/zapier-versions)(1)
