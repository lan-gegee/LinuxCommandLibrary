# TAGLINE

DNS 区域校验与调试工具

# TLDR

**检查 DNS 区域**错误

```dnswalk [domain.com.]```

以**详细输出**进行检查

```dnswalk -r [domain.com.]```

**检查指定的**区域文件

```dnswalk -l [domain.com.]```

**调试模式**

```dnswalk -d [domain.com.]```

**强制尝试**区域传送

```dnswalk -F [domain.com.]```

# SYNOPSIS

**dnswalk** [_options_] _domain_

# PARAMETERS

_DOMAIN_
> 要检查的域名（必须以点号结尾）。

**-r**
> 递归下钻各子域名。

**-l**
> 检查 lame delegation（失效委派）。

**-d**
> 调试模式（详细输出）。

**-F**
> 即使通常会被禁止也强制执行区域传送。

**-i**
> 跳过无效字符检查。

**-a**
> 开启所有警告标志。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dnswalk** 是一个 DNS 调试器，用于检查区域配置中的常见错误和不一致之处。它执行区域传送并分析得到的数据，查找诸如失效委派（lame delegation）、缺失 PTR 记录和无效数据等问题。

该工具能识别孤立 CNAME 记录、重复 A 记录、缺失反向条目以及指向不存在主机的记录等问题。它可以帮助 DNS 管理员维护区域健康状态并及时发现配置错误。

dnswalk 会遍历区域层级结构，并可选择递归进入子域名，从而对 DNS 基础设施提供全面的校验。

# CAVEATS

需要区域传送权限（通常受限）。域名必须以点号结尾。对有效但不常见的配置可能产生误报。需要 Perl 依赖。

# HISTORY

dnswalk 由 **David Barr** 于 20 世纪 90 年代初编写，是一款 DNS 调试与维护工具。它在校验区域配置方面至今仍然实用，数十年来一直是 DNS 管理员工具箱中的一员。

# INSTALL

```aur: yay -S dnswalk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dig](/man/dig)(1), [nslookup](/man/nslookup)(1)
