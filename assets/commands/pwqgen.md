# TAGLINE

创建安全的基于词典的口令短语

# TLDR

**生成口令短语**

```pwqgen```

**以指定的单词数量生成**

```pwqgen random=5```

**生成多个**

```pwqgen count=5```

# SYNOPSIS

**pwqgen** [_options_]

# PARAMETERS

**random=N**
> 随机单词的数量。

**count=N**
> 口令短语的数量。

# DESCRIPTION

**pwqgen** 通过将词典单词与分隔符组合来生成随机口令短语，产生的密码既强大又易于记忆。**random** 参数控制使用的单词数量，单词越多熵越高。

该工具是 **passwdqc**（密码质量检查）套件的一部分，是 **pwqcheck** 的配套工具。生成的口令短语遵循 passwdqc 密码策略所强制执行的质量规则，适合有严格密码要求的环境使用。

# CAVEATS

属于 passwdqc。可能默认未安装。

# HISTORY

pwqgen 是 **passwdqc** 密码质量检查套件的一部分。

# INSTALL

```apt: sudo apt install passwdqc```

```dnf: sudo dnf install passwdqc```

```zypper: sudo zypper install passwdqc```

```brew: brew install passwdqc```

```nix: nix profile install nixpkgs#passwdqc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwgen](/man/pwgen)(1), [apg](/man/apg)(1), [pwqcheck](/man/pwqcheck)(1)
