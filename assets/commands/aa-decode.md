# TAGLINE

解码 AppArmor 日志中的十六进制编码字符串

# TLDR

**解码**单个十六进制编码字符串

```aa-decode [hexstring]```

通过标准输入解码**日志文件**中的十六进制编码路径

```aa-decode < [/var/log/audit/audit.log]```

将**内核日志**通过管道送入 aa-decode

```cat /var/log/kern.log | aa-decode```

解码**当前 journal** 中的 AppArmor 条目

```journalctl -k | aa-decode```

# SYNOPSIS

**aa-decode** [_option_] _HEX_STRING_

# DESCRIPTION

**aa-decode** 用于解码 AppArmor 日志输出中出现的十六进制编码字符串。它处理来自标准输入的审计日志，并将其中所有十六进制编码的 AppArmor 条目转换成可读格式，写到标准输出。

AppArmor 会把日志条目中的某些字符（如空格和特殊字符）以十六进制格式编码，以避免解析问题。此工具将这些内容还原为可读文本。

# PARAMETERS

**--help**
> 显示用法信息

# CAVEATS

该工具只能解码 AppArmor 日志所用特定格式的十六进制字符串。其他十六进制编码的数据可能无法正确解码。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-logprof](/man/aa-logprof)(8), [aa-notify](/man/aa-notify)(8), [aa-status](/man/aa-status)(8), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Homepage](https://apparmor.net/)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-10 -->
