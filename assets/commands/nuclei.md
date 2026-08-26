# TAGLINE

快速漏洞扫描器

# TLDR

**用所有模板扫描目标**

```nuclei -u [https://example.com]```

**用指定模板扫描**

```nuclei -u [https://example.com] -t [template.yaml]```

**扫描多个目标**

```nuclei -l [targets.txt]```

**按严重程度扫描**

```nuclei -u [https://example.com] -s critical,high```

**按标签扫描**

```nuclei -u [https://example.com] -tags [cve,oast]```

**更新模板**

```nuclei -ut```

**以 JSONL 格式保存输出**

```nuclei -u [https://example.com] -jsonl -o [results.jsonl]```

# SYNOPSIS

**nuclei** [_options_]

# PARAMETERS

**-u** _URL_
> 要扫描的目标 URL。

**-l** _FILE_
> 包含目标列表的文件。

**-t** _TEMPLATE_
> 要使用的模板或目录。

**-s**, **-severity** _LEVEL_
> 按严重程度过滤（info、low、medium、high、critical）。

**-tags** _TAGS_
> 按标签过滤模板（逗号分隔）。

**-o** _FILE_
> 将结果输出到文件。

**-jsonl**
> 以 JSONL 格式输出结果。

**-ut**, **-update-templates**
> 将 nuclei 模板更新到最新版本。

**-rl**, **-rate-limit** _NUM_
> 每秒最大请求数（默认：150）。

**-c**, **-concurrency** _NUM_
> 并行执行模板的最大数量（默认：25）。

**-silent**
> 输出中只显示结果。

**-stats**
> 显示扫描统计信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nuclei** 是由 ProjectDiscovery 开发的快速基于模板的漏洞扫描器。它使用 YAML 模板定义针对 HTTP、DNS、TCP 等多种协议的扫描逻辑。

该工具基于庞大的社区驱动模板库进行针对性扫描，其中包含数千项针对 CVE、错误配置、敏感信息暴露和默认凭据的检查。模板可以自定义或从头编写。

# CAVEATS

仅可用于已授权的目标。模板需要定期更新以包含新的检查项。可能产生大量网络流量；在生产环境中应使用速率限制。某些模板可能触发 IDS/IPS 告警。

# HISTORY

Nuclei 由 **ProjectDiscovery** 创建，是一款基于模板的漏洞扫描器。

# INSTALL

```dnf: sudo dnf install nuclei```

```brew: brew install nuclei```

```nix: nix profile install nixpkgs#nuclei```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [nikto](/man/nikto)(1), [httpx](/man/httpx)(1)
