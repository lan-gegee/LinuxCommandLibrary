# TAGLINE

读取和修改 package.json 字段

# TLDR

**获取 package.json 字段**

```bun pm pkg get [field]```

**设置 package.json 字段**

```bun pm pkg set [field]=[value]```

**删除 package.json 字段**

```bun pm pkg delete [field]```

# SYNOPSIS

**bun** **pm** **pkg** _subcommand_ [_args_]

# SUBCOMMANDS

**get** _field_
> 获取 package.json 字段的值。

**set** _field=value_
> 设置 package.json 字段。

**delete** _field_
> 删除 package.json 字段。

# DESCRIPTION

**bun pm pkg** 提供以编程方式读取和修改 package.json 字段的命令。这对脚本编写和自动化很有用。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-pm](/man/bun-pm)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
