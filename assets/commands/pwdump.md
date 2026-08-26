# TAGLINE

提取 Windows 密码哈希用于审计

# TLDR

**转储 Windows 密码哈希**

```pwdump [system] [sam]```

**从本地 SAM 转储**

```pwdump localhost```

**输出到文件**

```pwdump [target] > [hashes.txt]```

**使用特定用户**

```pwdump [target] -u [administrator] -p [password]```

# SYNOPSIS

**pwdump** [_options_] _target_

# DESCRIPTION

**pwdump** 从 SAM 数据库中提取 Windows 密码哈希。这些哈希随后可被离线破解。用于安全审计和渗透测试。

存在多个版本（pwdump7、fgdump 等），功能各不相同。

# EXAMPLES

```bash
# Dump local hashes
pwdump localhost

# Remote system (admin required)
pwdump \\\\192.168.1.100

# Save for cracking
pwdump localhost > hashes.txt

# Then crack with John
john --format=NT hashes.txt
```

# OUTPUT FORMAT

```
Username:RID:LM_Hash:NT_Hash:::
```

# HASH TYPES

```
LM Hash   - Legacy, weak (pre-Vista)
NT Hash   - NTLM hash (current)
```

# CAVEATS

需要管理员权限。仅限 Windows。只能在你拥有或获得授权测试的系统上使用。可能被杀毒软件检测到。

# HISTORY

pwdump 为 Windows 密码审计而开发。多个版本（pwdump2-7、fgdump）由不同的安全研究人员创建。

# SEE ALSO

[john](/man/john)(1), [hashcat](/man/hashcat)(1)
