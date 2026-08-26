# TAGLINE

显示 Koji 命令的帮助信息

# TLDR

显示**所有可用命令**

```koji help```

显示**指定类别**的帮助

```koji help [category]```

显示本命令的**帮助**

```koji help --help```

# SYNOPSIS

**koji help** [_category_]

# DESCRIPTION

**koji help** 显示 Koji 命令的帮助信息。不带参数时会列出所有可用命令。带类别参数时，会显示该类别下的命令。

# PARAMETERS

**category**
> 按类别过滤命令（例如 admin、all、bind、build、download、info、misc、monitor、search）。

**--admin**
> 显示管理员命令。

**-h, --help**
> 显示帮助信息

# CAVEATS

要查看具体命令的详细帮助，请使用 `koji [subcommand] --help`，而不是这份总体概览。

# INSTALL

```dnf: sudo dnf install koji```

```brew: brew install koji```

```nix: nix profile install nixpkgs#koji```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[koji](/man/koji)(1)
