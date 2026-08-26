# TAGLINE

搜索和分析 SELinux 策略规则

# TLDR

搜索策略中的所有 **allow 规则**

```sesearch --allow```

搜索与**特定目标类型**相关的规则

```sesearch --allow -t [type_name]```

搜索与**特定源类型**相关的规则

```sesearch --allow -s [source_type]```

搜索具有特定**类和权限**的规则

```sesearch --allow -c [class_name] -p [permission]```

搜索 **type transition** 规则

```sesearch --type_transition -s [source_type]```

显示匹配规则的**详细**信息

```sesearch --allow -t [type_name] -v```

# SYNOPSIS

**sesearch** [_OPTIONS_] [_EXPRESSION_] [_POLICY_]

# PARAMETERS

**-A, --allow**
> 搜索 allow 和 allowxperm 规则

**-T, --type_transition**
> 搜索 type_transition 规则

**--auditallow**
> 搜索 auditallow 规则

**--dontaudit**
> 搜索 dontaudit 规则

**-s, --source** _NAME_
> 查找具有匹配源类型/属性的规则

**-t, --target** _NAME_
> 查找具有匹配目标类型/属性的规则

**-c, --class** _NAME_
> 查找具有匹配对象类的规则

**-p, --perm** _P1[,P2,...]_
> 查找具有匹配权限的规则（逗号分隔）

**-b, --bool** _NAME_
> 查找具有匹配条件布尔值的规则

**-ds**
> 直接匹配源类型，而非按属性匹配

**-dt**
> 直接匹配目标类型，而非按属性匹配

**-v, --verbose**
> 显示额外的规则信息

**--version**
> 打印版本并退出

# DESCRIPTION

**sesearch** 是来自 **setools** 软件包的 SELinux 策略查询工具，允许用户搜索和分析 SELinux 策略中的规则。它既能查询二进制策略文件（通常名为 policy.XX），也能查询模块化策略，是 SELinux 策略调试和开发的重要工具。

该工具支持搜索多种规则类型，包括 allow 规则、类型转换、基于角色的访问控制规则以及 MLS（多级安全）范围转换。结果可按源类型、目标类型、对象类、权限和布尔条件进行过滤。

# CAVEATS

策略文件必须可访问；在运行中的系统上默认位置为 **/sys/fs/selinux/policy**。不同策略版本的结果可能不同。不加过滤器地搜索大型策略可能产生大量输出。扩展权限规则（xperm）需要使用与标准权限搜索不同的标志。

# HISTORY

**sesearch** 是 **SETools**（SELinux Policy Tools）项目的一部分，最初由 **Tresys Technology** 于 **2001** 年起开发，旨在为 SELinux 策略提供分析能力。setools 软件包随 SELinux 一同演进，后者于 **2003** 年被合入 Linux 内核主线。目前的维护工作继续在 GitHub 上的 setools 项目中进行。

# INSTALL

```apt: sudo apt install setools```

```dnf: sudo dnf install setools```

```nix: nix profile install nixpkgs#setools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[seinfo](/man/seinfo)(1), [semodule](/man/semodule)(8), [sestatus](/man/sestatus)(8), [getsebool](/man/getsebool)(8)
