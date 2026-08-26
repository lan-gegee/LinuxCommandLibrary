# TAGLINE

随机标识符与 UUID 生成器

# TLDR

**生成随机 ID**

```genid```

**生成 UUID**

```genid --uuid```

**生成指定长度的 ID**

```genid -l [32]```

**仅使用字母和数字**

```genid --alphanumeric```

# SYNOPSIS

**genid** [_options_]

# PARAMETERS

**-l** _LENGTH_
> ID 长度。

**--uuid**
> 生成 UUID 格式。

**--alphanumeric**
> 仅使用字母和数字。

**--hex**
> 十六进制输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**genid** 生成适用于各种用途的随机标识符。它产生唯一的字符串，可用作 ID、令牌或密钥。

该工具支持多种格式，包括 UUID、字母数字字符串和自定义长度。其输出采用密码学安全的随机源，适用于非安全关键场景。

# CAVEATS

不可用于加密密钥。不保证唯一性。不同实现之间可能存在差异。

# HISTORY

genid 是一个用于生成随机标识符的工具，为脚本编写和开发提供便捷的随机字符串生成能力。

# SEE ALSO

[uuid](/man/uuid)(1), [uuidgen](/man/uuidgen)(1), [pwgen](/man/pwgen)(1)
