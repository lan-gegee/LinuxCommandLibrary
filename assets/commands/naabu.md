# TAGLINE

Go 编写的快速端口扫描器

# TLDR

**扫描目标的开放端口**

```naabu -host [example.com]```

**扫描指定端口**

```naabu -host [example.com] -p [80,443,8080]```

**扫描端口范围**

```naabu -host [example.com] -p [1-1000]```

**扫描常用端口**

```naabu -host [example.com] -top-ports [100]```

**从文件读取目标**

```naabu -list [targets.txt]```

**输出到文件**

```naabu -host [example.com] -o [results.txt]```

**以限速扫描**

```naabu -host [example.com] -rate [1000]```

**JSON 输出**

```naabu -host [example.com] -json```

# SYNOPSIS

**naabu** [_-host target_] [_-p ports_] [_-top-ports n_] [_-o file_] [_options_]

# PARAMETERS

**-host** _TARGET_
> 要扫描的目标。

**-list** _FILE_
> 包含目标的文件。

**-p** _PORTS_
> 要扫描的端口。

**-top-ports** _N_
> 扫描最常用的 N 个端口。

**-exclude-ports** _PORTS_
> 要排除的端口。

**-o** _FILE_
> 输出文件。

**-json**
> JSON 输出。

**-rate** _N_
> 每秒数据包数。

**-c** _N_
> 并发主机数。

**-timeout** _MS_
> 超时时间（毫秒）。

**-retries** _N_
> 重试次数。

**-verify**
> 验证开放端口。

**-nmap**
> 对发现的端口运行 nmap。

**-silent**
> 静默模式。

**-v**
> 详细输出。

# DESCRIPTION

**naabu** 是 Go 编写的快速端口扫描器。它使用 SYN 扫描以获得速度，同时通过验证保持准确性。

该扫描器通过可配置的限速来优化速度。它可以在遵守网络限制的前提下快速扫描数千台主机。

常用端口模式扫描最常见的开放端口，将资源集中在可能的目标上。自定义端口列表则可针对特定服务。

nmap 集成会将发现的端口交给 nmap 进行服务检测。这结合了 naabu 的速度与 nmap 详细的指纹识别能力。

输出格式包括纯文本、JSON 和兼容 nmap 的结果。与其他安全工具集成十分简单。

该工具专为执行授权评估的安全专业人员设计。

# CAVEATS

SYN 扫描需要 root/管理员权限。激进的扫描可能触发 IDS/IPS。只对已授权的目标使用。在生产网络上限速很重要。

# HISTORY

**naabu** 由 **ProjectDiscovery** 开发，是其安全工具套件的一部分。它与 nuclei、httpx、subfinder 等工具互补，构成完整的安全测试工作流。

# INSTALL

```brew: brew install naabu```

```nix: nix profile install nixpkgs#naabu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [masscan](/man/masscan)(1), [rustscan](/man/rustscan)(1), [zmap](/man/zmap)(1)
