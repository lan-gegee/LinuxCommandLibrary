# TAGLINE

自动找出最快的 Debian 镜像并生成 sources.list

# TLDR

**使用最快的镜像生成 sources.list**

```sudo netselect-apt```

**指定 Debian 发行版（默认为 stable）**

```sudo netselect-apt [testing]```

**包含 non-free 区段**

```sudo netselect-apt -n```

**将镜像限制在特定国家**

```sudo netselect-apt -c [India]```

**为源码包添加 deb-src 行**

```sudo netselect-apt -s```

**将输出写入自定义文件**

```sudo netselect-apt -o [/etc/apt/sources.list]```

**指定体系结构**

```sudo netselect-apt -a [amd64]```

# SYNOPSIS

**netselect-apt** [_options_] [_distribution_]

# PARAMETERS

**-a**, **--arch** _arch_
> 使用包含指定体系结构的镜像。默认采用 dpkg 报告的体系结构。

**-c**, **--country** _name_
> 将镜像选择限制在特定国家（ISO-3166 代码或完整英文名称）。

**-f**, **--ftp**
> 使用 FTP 镜像而非 HTTP。

**-n**, **--non-free**
> 在生成的 sources.list 中包含 non-free 区段。

**-o**, **--outfile** _file_
> 将输出写入指定文件而非 sources.list。

**-s**, **--sources**
> 为源码包添加 deb-src 行。

**-t**, **--tests** _num_
> 测试镜像有效性的主机数量（默认 10）。

**-i**, **--infile** _file_
> 使用本地镜像列表文件而不在线下载。必须是 mirrors_full 格式。

_distribution_
> Debian 发行版名称：stable、testing、unstable、experimental，或代号（如 bookworm、trixie）。默认为 stable。

# DESCRIPTION

**netselect-apt** 会自动找出最快的 Debian 镜像并生成相应的 sources.list 文件。它会下载官方的 Debian 镜像列表，可选地按国家过滤，用 **netselect** 测试各服务器的延迟，然后使用最快的镜像创建 sources.list。

这在搭建新的 Debian 系统或从默认镜像下载软件包速度缓慢时特别有用。

# CAVEATS

进行 ICMP 网络测试需要 root 权限。网络状况随时间变化；建议定期运行以找到当前最优的镜像。替换系统文件前应先检查生成的 sources.list。镜像延迟不一定能反映大文件的实际下载速度。

# INSTALL

```apt: sudo apt install netselect```

```nix: nix profile install nixpkgs#netselect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[netselect](/man/netselect)(1), [apt](/man/apt)(8), [apt-get](/man/apt-get)(8)
