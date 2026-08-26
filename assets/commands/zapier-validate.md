# TAGLINE

校验 Zapier 集成配置

# TLDR

**校验集成**

```zapier validate```

**连同风格检查一起校验**

```zapier validate --include-style```

# SYNOPSIS

**zapier** **validate** [_--include-style_] [_--format_ _json|plain_]

# PARAMETERS

**--include-style**
> 运行 Zapier 应用审核所用的额外 lint/风格检查。

**--format** _FORMAT_
> 输出格式：plain（默认）或 json。

# DESCRIPTION

**zapier validate** 检查 Zapier 集成中的错误，验证集成的模式、必填字段和配置。请在 **zapier push** 之前运行以尽早发现问题，因为无效的集成无法上传。

# SEE ALSO

[zapier](/man/zapier)(1), [zapier-test](/man/zapier-test)(1), [zapier-push](/man/zapier-push)(1)
