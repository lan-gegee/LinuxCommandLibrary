# TAGLINE

基于配方规则的邮件投递代理与过滤器

# TLDR

**按配方规则投递邮件**

```procmail < [email.txt]```

**测试配方文件**

```procmail -m [VERBOSE=on] [recipe] < [email.txt]```

**指定 maildir**

```procmail -d [maildir]```

# SYNOPSIS

**procmail** [_options_] [_parameters_] [_recipes_...]

# DESCRIPTION

**procmail** 是一个邮件投递代理和过滤程序。它根据 .procmailrc 中定义的规则将收到的邮件分类到各个文件夹，实现邮件的自动整理。

该工具可以过滤垃圾邮件、归类邮件列表、转发邮件，并根据邮件内容执行脚本。

# PARAMETERS

**-d** _maildir_
> 投递目录。

**-m** [_params_]
> 作为过滤器使用。

**-t**
> 若未以守护进程方式运行则失败。

**-v**
> 详细模式。

**-f** _fromline_
> 设置 From 行。

# RECIPE FORMAT

```
:0 [flags] [:lockfile]
* condition
action
```

**Flags**: H=header, B=body, h=header to pipe, b=body to pipe

# CONFIGURATION

**~/.procmailrc**
> 用户级配方文件，定义邮件过滤规则、投递动作以及 MAILDIR 和 LOGFILE 等变量设置。

**~/.forward**
> 邮件转发文件，将收到的邮件通过管道传给 procmail，通常包含 `"|IFS=' ' && exec /usr/bin/procmail -f- || exit 75"`。

**/etc/procmailrc**
> 系统级配方文件，在个人 .procmailrc 规则之前应用于所有用户。

# CAVEATS

配方语法复杂。安全性依赖细致的配置。已在很大程度上被服务器端过滤器取代。维护可能比较麻烦。

# HISTORY

**procmail** 由 **Stephen van den Berg** 自 **1990 年**开始编写。它曾是标准的 Unix 邮件过滤工具，但随着网页邮箱和服务器端过滤的普及，其使用已逐渐减少。它仍被用于高级的本地邮件处理。

# INSTALL

```apt: sudo apt install procmail```

```dnf: sudo dnf install procmail```

```zypper: sudo zypper install procmail```

```brew: brew install procmail```

```nix: nix profile install nixpkgs#procmail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fetchmail](/man/fetchmail)(1), [formail](/man/formail)(1), [maildir](/man/maildir)(5), [sieve](/man/sieve)(5)
