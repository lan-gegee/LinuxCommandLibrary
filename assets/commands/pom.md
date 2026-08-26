# TAGLINE

显示月相

# TLDR

**显示月相**

```pom```

**显示特定日期的月相**

```pom [YYYYMMDD]```

**显示日期范围内的月相**

```pom [start_date] [end_date]```

# SYNOPSIS

**pom** [_date_] [_date_]

# PARAMETERS

_DATE_
> YYYYMMDD 格式的日期。

# DESCRIPTION

**pom** 显示当前的月相，包括照亮百分比和相位名称（新月、上弦月、满月、下弦月）。它还可以计算特定日期的月相。

给定一个或两个 YYYYMMDD 格式的日期时，会显示该日期或日期范围的月相。这是一款 BSD 实用工具，可在 macOS 和 BSD 系统上使用。

# CAVEATS

BSD 实用工具。日期格式为 YYYYMMDD。

# HISTORY

pom 作为显示月相的 **BSD 实用工具**而创建。

# INSTALL

```nix: nix profile install nixpkgs#pom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cal](/man/cal)(1), [date](/man/date)(1)
