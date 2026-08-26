# TAGLINE

加载 Rails 环境的交互式 Ruby 控制台

# TLDR

**启动交互式控制台**并加载 Rails 应用

```rails console```

**使用短别名**

```rails c```

**以沙盒模式启动**（退出时回滚所有数据库变更）

```rails console --sandbox```

**在指定环境中启动控制台**

```rails console -e [production|test|development]```

**在指定环境中使用沙盒**

```rails console -e staging --sandbox```

# SYNOPSIS

**rails console** [**-e** _environment_] [**--sandbox**] [**--skip-executor**] [**-h**]

**rails c** [_options_]

# PARAMETERS

**-e**, **--environment** _ENV_
> 指定 Rails 环境（development、test、production）。默认为 development。

**--sandbox**, **-s**
> 退出时回滚会话期间所做的所有数据库变更。

**--skip-executor**, **-w**
> 不用 Rails Executor 包装控制台（跳过查询缓存、重载和回调）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**rails console** 会打开一个交互式 Ruby（IRB）会话，并加载完整的 Rails 应用环境。其中包括所有模型、配置和数据库连接，是探索和调试应用的强大工具。

该控制台提供对 ActiveRecord 模型的直接访问，可用于查询和操作数据、测试方法和业务逻辑，以及检查应用状态。它继承指定 Rails 环境的完整上下文。

沙盒模式将整个会话包装在一个数据库事务中，退出时自动回滚。这让你可以安全地试验数据而不产生永久变更，适合测试破坏性操作或调试生产环境问题。

# CAVEATS

必须在 Rails 应用目录内运行。控制台会加载整个应用，因此启动时间随应用规模增长。

在生产环境中修改数据时要格外谨慎。即使不用沙盒模式，控制台也以当前用户权限提供完整的数据库访问。

沙盒模式只保护数据库变更。文件系统修改、外部 API 调用或其他副作用不会被回滚。

# SEE ALSO

[rails](/man/rails)(1), [irb](/man/irb)(1), [rails-db](/man/rails-db)(1), [rails-server](/man/rails-server)(1), [ruby](/man/ruby)(1)
