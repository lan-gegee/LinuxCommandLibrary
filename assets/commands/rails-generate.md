# TAGLINE

从模板生成 Rails 应用组件

# TLDR

**生成模型**

```rails generate model [Name] [field:type]```

**生成控制器**

```rails generate controller [Name] [action]```

**生成脚手架**

```rails generate scaffold [Name] [field:type]```

**生成迁移**

```rails generate migration [Name]```

# SYNOPSIS

**rails** **generate** _generator_ _name_ [_options_]

# PARAMETERS

**model** _name_
> 生成模型。

**controller** _name_
> 生成控制器。

**scaffold** _name_
> 生成完整 CRUD。

**migration** _name_
> 生成迁移。

**-p**, **--pretend**
> 仅预览，不创建。

**--skip-routes**
> 不添加路由。

# DESCRIPTION

**rails generate** 根据模板为常见的 Rails 应用组件创建样板文件。它会按照 Rails 命名约定和目录结构自动生成：带数据库迁移的模型、带关联视图和路由的控制器，以及通过 scaffold 生成器创建的完整 CRUD 接口。

每个生成器都会产生相应的一组文件，包括源代码、测试存根和配置条目。**--pretend** 标志可预览将要创建的内容而不写入文件，**--skip-routes** 可阻止自动添加路由。可以创建自定义生成器以匹配项目特定的模式；逆操作 **rails destroy** 则移除生成器创建的所有文件。

# SEE ALSO

[rails](/man/rails)(1), [rails-destroy](/man/rails-destroy)(1)
