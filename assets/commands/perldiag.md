# TAGLINE

收录 Perl 所有可能产生的诊断信息的 Perl 文档文件

# TLDR

**查看全部 Perl 诊断信息**

```perldoc perldiag```

**搜索特定消息**

```perldoc perldiag | grep "[error message]"```

**用 splain 获取解释**

```perl [script.pl] 2>&1 | splain```

**启用详细警告**

```perl -Mdiagnostics [script.pl]```

# SYNOPSIS

**perldoc perldiag**

**splain** [_error_message_]

# DESCRIPTION

**perldiag** 是一个 Perl 文档文件，收录了 Perl 可能产生的所有诊断信息。每条消息都附有解释和修复建议。

可通过 perldoc 阅读，或使用 diagnostics 模块在运行时获取解释。
# 阅读完整诊断信息
perldoc perldiag

# 在脚本中使用 diagnostics 模块
perl -Mdiagnostics script.pl

# 解释错误消息
echo "Use of uninitialized value" | splain
```

# IN SCRIPT

```perl
use diagnostics;      # Verbose messages
use warnings;         # Enable warnings

# Or for specific categories
use warnings qw(all);
no warnings qw(uninitialized);
```

# MESSAGE TYPES

```
(W) Warning - may indicate problem
(D) Deprecation - feature being removed
(S) Severe warning - almost certainly wrong
(F) Fatal - compilation error
(X) Alien - error from external source
```

# CAVEATS

属于 Perl 核心文档。diagnostics 模块会带来运行时开销。仅建议在开发期间使用。

# HISTORY

perldiag 属于由 **Larry Wall** 和 Perl 社区共同编写的 **Perl** 核心文档。

# SEE ALSO

[perl](/man/perl)(1), [perlre](/man/perlre)(1), [perldoc](/man/perldoc)(1)
