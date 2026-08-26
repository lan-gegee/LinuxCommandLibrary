# TAGLINE

多种工具的上下文切换器

# TLDR

**显示当前上下文**

```ic```

**切换上下文**

```ic [context-name]```

**列出上下文**

```ic -l```

**创建上下文**

```ic -c [name]```

# SYNOPSIS

**ic** [_options_] [_context_]

# PARAMETERS

_CONTEXT_
> 要切换到的上下文名称。

**-l**, **--list**
> 列出上下文。

**-c**, **--create** _NAME_
> 创建新上下文。

**-d**, **--delete** _NAME_
> 删除上下文。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ic** 是面向多种工具的上下文切换器。针对 kubectl 上下文、AWS 配置文件及其他多环境工具，存在不同的实现。

该工具简化了配置之间的切换。它提供对不同环境或集群的快速访问。

# CAVEATS

多个工具使用此名称。请确认安装的是哪个版本。行为因具体上下文而异。

# HISTORY

ic 在各种 CLI 工具中常被用作交互式上下文切换的简称。

# SEE ALSO

[kubectx](/man/kubectx)(1), [aws-vault](/man/aws-vault)(1)
