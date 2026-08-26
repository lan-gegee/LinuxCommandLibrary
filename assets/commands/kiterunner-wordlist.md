# TAGLINE

管理 Kiterunner API 端点发现所用的字典

# TLDR

**列出可用字典**

```kr wordlist list```

**下载字典**

```kr wordlist download [wordlist-name]```

**将字典转换为 kite 格式**

```kr wordlist convert [input.txt] -o [output.kite]```

# SYNOPSIS

**kr** **wordlist** _subcommand_ [_options_]

# PARAMETERS

**list**
> 列出可用的字典。

**download** _name_
> 下载字典。

**convert** _input_
> 转换为 kite 格式。

**-o** _file_
> 输出文件路径。

# DESCRIPTION

**kr wordlist** 管理 Kiterunner API 端点发现所用的字典。提供精选的面向 API 的字典访问能力，以及将自定义字典转换为优化 kite 格式的工具。

# INSTALL

```nix: nix profile install nixpkgs#kiterunner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kiterunner-brute](/man/kiterunner-brute)(1)
