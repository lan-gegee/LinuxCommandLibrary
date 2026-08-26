# TAGLINE

支持本地化的假数据生成库 CLI

# TLDR

生成假姓名

```faker name```

生成假邮箱

```faker email```

指定地区生成

```faker -l [de_DE] address```

多条输出

```faker -r [10] name```

生成特定类型的数据

```faker phone_number```

# SYNOPSIS

**faker** [_options_] _provider_ [_method_]

# PARAMETERS

_PROVIDER_
> 数据提供者：name、address、email、phone_number 等。

**-l** _LOCALE_, **--locale** _LOCALE_
> 生成数据所用地区（如 en_US、de_DE、ja_JP）。

**-r** _COUNT_, **--repeat** _COUNT_
> 要生成的值的数量。

**-s** _SEED_, **--seed** _SEED_
> 用于可复现性的随机种子。

**-o** _FORMAT_, **--output** _FORMAT_
> 输出格式：csv、json、tab。

**--help**
> 显示帮助信息。

# DESCRIPTION

**faker** 是一个生成假数据的命令行工具，如姓名、地址、邮箱和电话号码。它是 Faker Python 库的一部分，支持许多国家地区的本地化数据。

该工具提供众多数据提供者，涵盖个人信息、公司详情、互联网数据、日期等。本地化功能确保生成的数据符合相应地区的格式和命名习惯。

faker 广泛用于测试、数据库填充和开发场景，适合需要逼真但不含敏感数据的场合。

# CAVEATS

生成的数据可能碰巧与真实信息相同。质量因地区而异。某些提供者在特定区域可能不完整。

# HISTORY

Faker 起源于一个受 Perl 的 Data::Faker 启发的 **PHP 库**。**joke2k** 开发的 Python 版本广受欢迎，提供了 faker CLI 和庞大的提供者生态用于生成测试数据。

# INSTALL

```apk: sudo apk add py3-faker```

```brew: brew install faker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [pip](/man/pip)(1)
