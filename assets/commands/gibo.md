# TAGLINE

从社区维护的模板生成 .gitignore 文件

# TLDR

**列出可用的样板模板**

```gibo list```

**组合多个样板模板并输出到标准输出**

```gibo dump [Python] [macOS] [VisualStudioCode]```

**按子串搜索样板模板**

```gibo search [node]```

**将样板模板追加到你的 .gitignore**

```gibo dump [Python] >> .gitignore```

**更新本地缓存的样板模板仓库**

```gibo update```

**显示样板模板在磁盘上的存储位置**

```gibo root```

# SYNOPSIS

**gibo** _command_ [_boilerplates_]

# PARAMETERS

**dump** _NAMES_...
> 将指定的样板模板写入标准输出，以标题分隔。名称与 github.com/github/gitignore 中的模板进行不区分大小写的匹配。

**list**
> 列出所有可用的样板模板，按类别分组。

**search** _STR_
> 列出名称包含 _STR_ 的样板模板。

**update**
> 从上游仓库获取最新的样板模板。

**root**
> 打印 gibo 存储样板模板本地克隆的目录。

**version**
> 打印当前 gibo 版本。

**help**
> 显示帮助文本。

# DESCRIPTION

**gibo**（gitignore boilerplates）根据托管在 GitHub 官方 gitignore 仓库中的社区维护模板生成 .gitignore 文件。它提供针对语言、框架、IDE 和操作系统的模板。

可以在一条命令中组合多个样板模板。该工具会将模板缓存到本地以便离线使用，并支持按名称搜索。

# CAVEATS

首次使用该工具时需要先执行一次 `gibo update`，以将上游样板模板仓库克隆到本地。请定期运行 `gibo update` 以获取新模板。样板模板名称不区分大小写，但必须匹配 github/gitignore 中的某个模板文件；可使用 `gibo list` 或 `gibo search` 查找有效名称。

# HISTORY

**gibo** 由 **Simon Whitaker** 创建，最初是一个包装 **github.com/github/gitignore** 本地克隆的 Shell 脚本。后来 Go 重写版（gibo-go）取代了原始的 Shell 实现，同时保持了相同的命令接口。

# INSTALL

```brew: brew install gibo```

```nix: nix profile install nixpkgs#gibo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1)
