# TAGLINE

用 Nix 免安装直接运行软件

# TLDR

**运行命令**而无需安装它

```, [command]```

**从指定软件包运行命令**

```, [command] --from [package]```

# SYNOPSIS

**,** [_command_] [_args_...]

# DESCRIPTION

**comma**（以 **,** 调用）无需永久安装即可运行软件。它封装了 **nix shell -c** 和 **nix-index**，先在 nixpkgs 中搜索该二进制程序，临时安装相关软件包，然后运行命令。

如果多个软件包提供同一个命令，comma 会提示你选择使用哪个软件包。结果会被缓存，后续运行同一命令时将复用之前的选择。

comma 需要可用的 Nix 安装以及最新的 nix-index 数据库。

# CAVEATS

需要 Nix 软件包管理器。nix-index 数据库必须保持更新才能获得准确的结果。首次运行某个命令时可能因下载软件包而较慢。缓存的路径会因垃圾回收而失效。

# INSTALL

```nix: nix profile install nixpkgs#comma```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-shell](/man/nix-shell)(1)
