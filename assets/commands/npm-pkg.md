# TAGLINE

操作 package.json

# TLDR

**获取 package.json 字段**

```npm pkg get [name]```

**设置 package.json 字段**

```npm pkg set [name]="[value]"```

**删除字段**

```npm pkg delete [field]```

**获取多个字段**

```npm pkg get [name] [version]```

**设置嵌套字段**

```npm pkg set [scripts.test]="[jest]"```

# SYNOPSIS

**npm** **pkg** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> pkg 子命令。

**get** _FIELD_
> 读取字段值。

**set** _FIELD=VALUE_
> 写入字段值。

**delete** _FIELD_
> 移除字段。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm pkg** 操作 package.json 的字段，可以以编程方式读写属性。

该命令用于修改 package.json，适合脚本和自动化场景。

# CAVEATS

会修改 package.json。支持 JSON 路径。值需要加引号。

# HISTORY

npm pkg 让你可以从命令行**操作 package.json**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-init](/man/npm-init)(1), [npm-version](/man/npm-version)(1)
