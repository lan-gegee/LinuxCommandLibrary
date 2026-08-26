# TAGLINE

移除 Rails 生成器创建的文件

# TLDR

**移除模型**

```rails destroy model [Name]```

**移除控制器**

```rails destroy controller [Name]```

**移除脚手架**

```rails destroy scaffold [Name]```

**移除迁移**

```rails destroy migration [Name]```

# SYNOPSIS

**rails** **destroy** _generator_ _name_ [_options_]

# PARAMETERS

**model** _name_
> 移除模型。

**controller** _name_
> 移除控制器。

**scaffold** _name_
> 移除脚手架。

**migration** _name_
> 移除迁移。

**-p**, **--pretend**
> 仅预览，不移除。

# DESCRIPTION

**rails destroy** 是 **rails generate** 的逆操作，会移除生成器先前创建的所有文件和修改。它删除被脚手架生成的模型文件、控制器、视图、迁移、测试文件和路由条目，干净地撤销生成器的工作而不留下孤立代码。

**--pretend** 标志可以预览哪些文件会被移除而不实际删除任何内容，便于在执行操作前进行确认。该命令接受与 **rails generate** 相同的生成器名称和参数，因此可以轻松撤销之前的任何脚手架操作。

# SEE ALSO

[rails](/man/rails)(1), [rails-generate](/man/rails-generate)(1)
