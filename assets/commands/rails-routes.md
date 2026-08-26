# TAGLINE

显示 Rails 应用的 URL 路由表

# TLDR

**列出应用中的所有路由**

```rails routes```

**搜索匹配模式的路由**

```rails routes -g [pattern]```

**显示指定控制器的路由**

```rails routes -c [controller_name]```

**以展开格式显示路由**

```rails routes --expanded```

# SYNOPSIS

**rails routes** [**-g** _pattern_] [**-c** _controller_] [**--expanded**]

# PARAMETERS

**-g**, **--grep** _pattern_
> 按模式过滤路由（匹配名称、HTTP 动词、路径或 controller#action）

**-c**, **--controller** _name_
> 只显示指定控制器的路由

**--expanded**, **-E**
> 以展开的表格格式打印路由（每行一个属性）

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**rails routes** 显示 Rails 应用中定义的所有路由。路由将传入的 URL 映射到控制器动作，定义在 **config/routes.rb** 中。

输出内容包括路由名称（用于 URL 辅助方法）、HTTP 动词、URL 模式以及处理请求的 controller#action。命名路由可在视图和控制器中以 **_path** 和 **_url** 后缀的形式使用。

grep 选项对拥有大量路由的大型应用很有用。它会搜索所有列，方便按 URL 模式、控制器名称或路由辅助方法名称查找路由。

# CAVEATS

必须在 Rails 应用目录内运行。该命令会加载应用环境，大型应用可能耗时较长。

路由按匹配顺序显示。第一个匹配的路由处理请求，因此当路由可能重叠时顺序很重要。

# SEE ALSO

[rails](/man/rails)(1), [rails-server](/man/rails-server)(1), [rake](/man/rake)(1)
