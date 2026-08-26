# TAGLINE

检查软件包名在 npm 上是否可用

# TLDR

**检查名称是否可用**

```npm-name [package-name]```

**检查多个名称**

```npm-name [name1] [name2] [name3]```

**检查带作用域的名称**

```npm-name [@scope/name]```

# SYNOPSIS

**npm-name** [_names_]

# PARAMETERS

_NAMES_
> 要检查的软件包名称。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm-name** 检查软件包名在 npm registry 上是否可用。它会查询 npm registry API，并报告每个名称是空闲还是已被占用。支持带作用域的软件包（@scope/name）。发布新软件包前用来避免名称冲突很有用。

# CAVEATS

第三方工具；使用 **npm install -g npm-name-cli** 安装。需要网络访问以查询 npm registry。不会检查商标冲突或相似名称。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1)
