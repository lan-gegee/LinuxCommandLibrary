# TAGLINE

基于 Java 的 Web 内容发现工具

# TLDR

以 **GUI 模式**启动

```dirbuster -u [http://example.com]```

以**无头模式**启动

```dirbuster -H -u [http://example.com]```

设置要扫描的**文件扩展名**

```dirbuster -e [txt,html]```

启用**详细输出**

```dirbuster -v```

设置**报告位置**

```dirbuster -r [path/to/report.txt]```

# SYNOPSIS

**dirbuster** [_options_]

# DESCRIPTION

**dirbuster** 对 Web 服务器上的目录和文件名进行暴力破解。它使用词典来发现隐藏的 Web 内容，同时提供图形界面和无头两种模式。

常用于渗透测试，查找管理界面、备份文件及其他隐藏资源。

# PARAMETERS

**-u** _url_
> 目标 URL

**-H**
> 无头模式（无 GUI）

**-e** _extensions_
> 要扫描的文件扩展名

**-v**
> 详细输出

**-r** _file_
> 报告输出位置

**-l** _wordlist_
> 词典文件路径

**-t** _threads_
> 线程数

# CAVEATS

仅可用于获得授权的目标。基于 Java，需要 Java 运行时。如需更快的扫描速度可考虑 dirb 或 gobuster。属于 Kali Linux 安全工具。

# INSTALL

```nix: nix profile install nixpkgs#dirbuster```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dirb](/man/dirb)(1), [gobuster](/man/gobuster)(1), [nikto](/man/nikto)(1)

# RESOURCES

```[Source code](https://gitlab.com/kalilinux/packages/dirbuster)```

<!-- verified: 2026-07-11 -->
