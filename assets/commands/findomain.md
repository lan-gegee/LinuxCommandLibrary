# TAGLINE

快速的跨平台子域名枚举工具

# TLDR

**查找域名的子域名**

```findomain -t [example.com]```

**输出到文件**

```findomain -t [example.com] -o```

**使用全部数据源**

```findomain -t [example.com] -a```

**检查存活的子域名**

```findomain -t [example.com] --resolved```

**以 JSON 输出**

```findomain -t [example.com] --json```

**从文件读取域名**

```findomain -f [domains.txt]```

# SYNOPSIS

**findomain** [_options_] -t _domain_

# DESCRIPTION

**findomain** 是一款跨平台的子域名枚举工具。它通过查询多个数据源来发现目标域名的子域名，可用于安全评估中的侦察环节。

该工具从证书透明度日志、搜索引擎以及其他被动来源聚合结果，不会直接向目标发起请求。

# PARAMETERS

**-t** _domain_
> 目标域名。

**-f** _file_
> 从文件读取域名列表。

**-o**
> 输出到文件。

**-a**, **--all-apis**
> 使用所有可用的 API。

**--resolved**
> 只显示能够解析的子域名。

**--ip**
> 显示 IP 地址。

**--json**
> 以 JSON 格式输出。

**-q**, **--quiet**
> 不输出提示性信息。

**-u**, **--unique**
> 去除重复项。

# CONFIGURATION

**~/.config/findomain/config.toml**
> SecurityTrails、Shodan、VirusTotal 等数据源的 API 密钥。

# CAVEATS

某些数据源需要 API 密钥。结果取决于可用数据的情况。不执行主动扫描。可能受到速率限制。

# HISTORY

**findomain** 由 **Eduard Tolosa** 创建，是一款追求速度的子域名枚举工具。它采用 Rust 编写以获得高性能，作为 Sublist3r、Amass 等工具的替代方案问世。该项目专注于让被动侦察更快、更可靠。

# INSTALL

```pacman: sudo pacman -S findomain```

```brew: brew install findomain```

```nix: nix profile install nixpkgs#findomain```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[amass](/man/amass)(1), [subfinder](/man/subfinder)(1), [sublist3r](/man/sublist3r)(1), [dnsx](/man/dnsx)(1)

# RESOURCES

```[Source code](https://github.com/Findomain/Findomain)```

<!-- verified: 2026-07-15 -->
