# TAGLINE

Perl 正则表达式文档，它是最强大的正则表达式之一

# TLDR

**查看 Perl 正则表达式文档**

```perldoc perlre```

**查看快速参考**

```perldoc perlreref```

**查看正则表达式教程**

```perldoc perlretut```

**查看字符类**

```perldoc perlrecharclass```

# SYNOPSIS

**perldoc perlre**

# DESCRIPTION

**perlre** 介绍了 Perl 正则表达式——最强大的正则表达式实现之一。Perl 的正则语法影响了众多其他语言和工具（PCRE）。

# BASIC PATTERNS

```perl
/pattern/       # Match
s/old/new/      # Substitute
m/pattern/i     # Case insensitive
/pattern/g      # Global

# Character classes
\d  - Digit
\w  - Word character
\s  - Whitespace
.   - Any character
```

# MODIFIERS

```perl
/i  - Case insensitive
/g  - Global match
/m  - Multiline mode
/s  - Single line (. matches \n)
/x  - Extended (allow whitespace)
/o  - Compile once
```

# CAPTURES

```perl
# Match and capture
if ($text =~ /(\d+)/) {
    print "Found: $1\n";
}

# Named captures
/(?<name>\w+)/;
print $+{name};

# Non-greedy
/.*?/
```

# ADVANCED FEATURES

```perl
(?:...)   - Non-capturing group
(?=...)   - Positive lookahead
(?!...)   - Negative lookahead
(?<=...)  - Positive lookbehind
(?<!...)  - Negative lookbehind
(?>...)   - Atomic group
```

# CAVEATS

复杂的正则表达式可能很慢。使用 /x 提高可读性。PCRE 与 Perl 正则略有差异。

# HISTORY

Perl 正则表达式由 **Larry Wall** 设计，并随 Perl 各个版本不断演进，成为现代正则表达式的标杆。

# SEE ALSO

[perl](/man/perl)(1), [perldoc](/man/perldoc)(1)
