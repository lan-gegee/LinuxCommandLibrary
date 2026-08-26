# TAGLINE

校验 Prometheus 告警和记录规则

# TLDR

**检查 Prometheus 规则**

```pint lint [rules.yaml]```

**对照运行中的 Prometheus 检查规则**

```pint -c [config.yaml] lint [rules.yaml]```

**监视变更**

```pint watch [rules/]```

**显示规则问题**

```pint lint --output=json [rules.yaml]```

**CI 模式**

```pint ci```

**列出可用的检查项**

```pint checks```

# SYNOPSIS

**pint** [_-c config_] _command_ [_options_] [_files_]

# PARAMETERS

**lint**
> 检查规则中的问题。

**watch**
> 持续监视并检查。

**ci**
> CI/CD 模式。

**checks**
> 列出可用的检查项。

**-c**, **--config** _FILE_
> 配置文件。

**--output** _FORMAT_
> 输出格式。

**--no-color**
> 禁用彩色输出。

**-v**, **--verbose**
> 详细输出。

# CHECKS

**promql/syntax** - 查询语法
**promql/series** - 序列是否存在
**alerts/for** - 告警持续时间
**alerts/template** - 模板错误
**rule/duplicate** - 重复规则

# DESCRIPTION

**pint** 校验 Prometheus 告警和记录规则，在部署之前捕获错误。它超越了基本的语法检查，会查询运行中的 Prometheus 服务器，验证引用的指标确实存在且选择器能返回数据。

关键能力包括：PromQL 语法校验、对照运行中 Prometheus 的序列存在性检查、告警模板校验（注解和标签渲染）、重复规则检测，以及昂贵查询的成本估算。

**ci** 模式专为拉取请求工作流设计——只报告已更改文件中的问题，因此适用于大型规则仓库。**watch** 模式持续监控规则文件并在变更时重新检查。

# CAVEATS

实时检查需要能够访问 Prometheus 服务器的网络。对于间歇性抓取的指标，某些检查可能产生误报。需要配置才能将 pint 连接到 Prometheus 实例。

# HISTORY

**pint** 由 **Cloudflare** 创建，用于大规模校验其 Prometheus 规则。它提供比 Prometheus 内置规则检查更深入的分析。

# INSTALL

```pacman: sudo pacman -S pint```

```brew: brew install pint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[promtool](/man/promtool)(1), [prometheus](/man/prometheus)(1), [amtool](/man/amtool)(1)
