# TAGLINE

使用原理图（schematics）创建 Angular 构件

# TLDR

**生成组件**

```ng generate component [name]```

**生成服务**

```ng generate service [name]```

**生成模块**

```ng generate module [name]```

**使用简写形式生成**

```ng g c [name]```

**在指定路径下生成**

```ng generate component [path/name]```

**试运行**

```ng generate component [name] --dry-run```

# SYNOPSIS

**ng** **generate** _schematic_ _name_ [_options_]

# SCHEMATICS

**component** (c) / **directive** (d) / **pipe** (p) / **service** (s)
> 生成对应的 Angular 构件。

**module** (m)
> 生成一个 NgModule。

**guard** (g) / **interceptor**
> 生成路由守卫或 HTTP 拦截器。

**class** / **interface** / **enum**
> 生成普通的 TypeScript 类、接口或枚举。

**resolver**
> 生成路由数据解析器。

**library**
> 生成一个可发布的库工作区。

**application**
> 向多项目工作区中添加新应用。

**environments**
> 为项目创建环境文件。

# PARAMETERS

**--dry-run**, **-d**
> 只显示将要生成的内容，而不写入文件。

**--force**
> 覆盖已有文件。

**--skip-tests**
> 不生成 .spec.ts 测试文件。

**--skip-import**
> 不把生成的构件导入其 NgModule。

**--standalone**
> 以独立（standalone）方式生成组件/指令/管道（Angular 14+）。

**--inline-template**, **-t**
> 把 HTML 内联写在组件装饰器里。

**--inline-style**, **-s**
> 把 CSS 内联写在组件装饰器里。

**--style** _ext_
> 样式表扩展名：css、scss、sass、less、none。

**--prefix** _prefix_
> 覆盖项目的选择器前缀。

**--export**
> 从所属 NgModule 中导出生成的声明。

**--project** _name_
> 面向工作区中的特定项目。

# DESCRIPTION

**ng generate** 使用原理图（schematics）创建 Angular 构件。它会搭建组件、服务、模块、指令、管道、守卫、拦截器等代码骨架，把它们接入项目的 NgModule（或在较新版本的 Angular 中以 standalone 方式生成），并添加配套的 .spec.ts 文件。简写形式 **ng g** 与之等效。

原理图存放于 **@schematics/angular** 及其他 npm 包中；通过 **ng add** 安装的库也可以注册自己的原理图（例如 **@angular/material** 提供了 **material:navigation**）。可用列表可通过 **ng generate --help** 查看。

# CAVEATS

必须在 Angular CLI 工作区内（即包含 **angular.json** 的目录）运行。新生成的文件遵循项目的编码风格设置（选择器前缀、缩进、样式扩展名）。可用的原理图集合取决于通过 **ng add** 添加了哪些包。

# SEE ALSO

[ng](/man/ng)(1), [ng-add](/man/ng-add)(1)
