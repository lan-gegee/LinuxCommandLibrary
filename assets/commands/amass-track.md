# TAGLINE

跟踪外部攻击面随时间的变化

# TLDR

在不同枚举之间**跟踪**变化

```amass track -d [example.com]```

自**指定日期**起进行跟踪

```amass track -d [example.com] -since "2024-01-01"```

与**上一次枚举**比较

```amass track -d [example.com] -last [2]```

将**差异**输出到文件

```amass track -d [example.com] -o [changes.txt]```

# SYNOPSIS

**amass track** [_-d domain_] [_-since date_] [_-last n_] [_options_]

# DESCRIPTION

**amass track** 比较不同枚举运行的结果，以识别组织外部攻击面的变化。它能检测新增的子域名、被移除的资产以及基础设施变更。

这对于持续监控组织的数字足迹非常有用，可以让安全团队及时了解潜在的影子 IT 或未经授权的变更。

注意 **track** 是一个遗留子命令。在 Amass v4 中，它被移出核心 **amass** 二进制文件，放入独立的 oam-tools 包（即 **oam_track**），并且在 Amass v5 中工作流又被重新设计。在当前的 Amass 安装中，**amass track** 子命令可能不可用；请用 **amass -version** 检查版本。

# PARAMETERS

**-d** _domain_
> 要跟踪的域名

**-since** _date_
> 与指定日期以来的枚举进行比较

**-last** _n_
> 与最近 n 次枚举进行比较

**-history**
> 显示所有历史变化

**-o** _file_
> 输出文件

**-dir** _path_
> 数据库目录

# CONFIGURATION

**~/.config/amass/config.ini**
> Amass 配置文件，定义数据源、API 密钥和范围设置。

# CAVEATS

需要数据库中存有多次枚举运行的结果。检测质量取决于枚举设置的一致性。大型组织的正常变更可能很频繁。**track** 子命令已被弃用：它在 v4 中被移出核心 **amass** 二进制文件（移至 oam-tools 的 **oam_track**），并在 v5 中又被重新设计，因此在当前安装中可能不可用。

# HISTORY

**amass track** 的引入是为了支持持续监控场景，让安全团队能够检测攻击面随时间的变化。随着 Amass v4 的重新设计，该子命令被拆分到 oam-tools 包中成为 **oam_track**，跟踪工作流又在 Amass v5 中得到进一步改造。

# INSTALL

```aur: yay -S amass```

```brew: brew install amass```

```nix: nix profile install nixpkgs#amass```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amass](/man/amass)(1), [amass-enum](/man/amass-enum)(1), [amass-intel](/man/amass-intel)(1), [amass-db](/man/amass-db)(1)

# RESOURCES

```[Source code](https://github.com/owasp-amass/amass)```

```[Documentation](https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md)```

<!-- verified: 2026-06-11 -->
