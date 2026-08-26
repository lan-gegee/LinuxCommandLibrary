# TAGLINE

查看软件包在 npm registry 上的信息

# TLDR

**查看软件包信息**

```npm view [package]```

**查看特定字段**

```npm view [package] version```

**查看所有已发布的版本**

```npm view [package] versions```

**查看软件包依赖**

```npm view [package] dependencies```

**查看嵌套字段**

```npm view [package] repository.url```

**以 JSON 输出**

```npm view [package] --json```

**查看 dist-tags**（latest、next 等）

```npm view [package] dist-tags```

**查看特定版本的信息**

```npm view [package]@[2.0.0]```

**从自定义 registry 查看信息**

```npm view [package] --registry [https://registry.example.com]```

# SYNOPSIS

**npm** **view** [_package_[@_version_]] [_field_[._subfield_]...]

# PARAMETERS

_PACKAGE_
> 软件包名称，可选带 @version 或 @tag。

_FIELD_
> 要显示的顶层字段（version、dependencies、license、repository 等）。

_FIELD.SUBFIELD_
> 嵌套字段访问（如 repository.url、dist.tarball）。

**versions**
> 列出所有已发布的版本。

**dependencies**
> 显示生产依赖。

**dist-tags**
> 显示分发标签。

**--json**
> 以 JSON 格式输出。

**--registry** _url_
> 查询自定义的 registry URL。

# DESCRIPTION

**npm view** 从 npm registry 获取并显示软件包的元数据。默认显示完整的软件包清单，也可以按需显示特定字段。

该命令支持用点号访问嵌套字段（如 `repository.url`）。当字段包含数组时，每个元素单独占一行输出。可以同时指定多个字段，一次显示多个值。

别名：**npm info**、**npm show**。

# CAVEATS

需要网络访问才能查询 registry。查看带作用域（scoped）的软件包时必须包含作用域（如 @scope/package）。输出格式在单值和数组之间有所不同。私有软件包需要身份验证。

# HISTORY

**npm view** 从 npm 早期版本起就已可用，为命令行提供对软件包 registry 元数据的访问，这些元数据支撑着 npm 的依赖解析。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-search](/man/npm-search)(1), [npm-pack](/man/npm-pack)(1), [npm-install](/man/npm-install)(1), [npm-publish](/man/npm-publish)(1), [npm-ls](/man/npm-ls)(1), [npm-outdated](/man/npm-outdated)(1)
