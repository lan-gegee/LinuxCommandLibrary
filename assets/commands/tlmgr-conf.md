# TAGLINE

显示和修改 TeX Live 配置

# TLDR

**显示常规 TeX Live 配置**

```tlmgr conf```

**显示所有 texmf.cnf 设置**

```tlmgr conf texmf```

**显示单个 tlmgr 设置的值**

```tlmgr conf tlmgr [setting]```

**设置一个 tlmgr 配置值**

```tlmgr conf tlmgr [setting] [value]```

**从 tlmgr 配置文件中删除某项设置**

```tlmgr conf tlmgr --delete [setting]```

**列出辅助 texmf 目录树**

```tlmgr conf auxtrees show```

**添加辅助 texmf 目录树**

```tlmgr conf auxtrees add [/path/to/tree]```

**移除辅助 texmf 目录树**

```tlmgr conf auxtrees remove [/path/to/tree]```

# SYNOPSIS

**tlmgr conf** [texmf|tlmgr|updmap [**--conffile** _file_] [**--delete**] [_key_ [_value_]]]

**tlmgr conf** auxtrees [**--conffile** _file_] [show|add|remove] [_value_]

# PARAMETERS

**texmf**
> 显示或设置 texmf.cnf 中的值。

**tlmgr**
> 显示或设置 tlmgr 配置文件中的值。

**updmap**
> 显示或设置找到的第一个 updmap.cfg 中的值。

**auxtrees**
> 管理额外的（辅助）texmf 目录树。子命令：show、add、remove。

**--conffile** _file_
> 使用指定的配置文件而不是默认配置文件。

**--delete**
> 将键从配置文件中彻底删除（而不是注释掉）。

_key_ _value_
> 在所选配置文件中将配置键设置为指定值。

# DESCRIPTION

**tlmgr conf** 显示和修改 TeX Live 配置设置。不带参数时显示常规配置信息（活动文件、路径和设置）。带系统参数（texmf、tlmgr 或 updmap）时显示相应配置文件中保存的所有键/值对。提供键则只显示该键的值；同时提供值则会进行设置。**--delete** 标志会彻底删除某个键而不是覆盖它。

**auxtrees** 子命令管理与标准 TeX Live 目录树一同搜索的额外 texmf 目录树。

TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-option](/man/tlmgr-option)(1), [tlmgr](/man/tlmgr)(1)
