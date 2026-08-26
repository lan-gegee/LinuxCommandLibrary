# TAGLINE

依据策略校验密码强度

# TLDR

**检查密码强度**

```echo "[password]" | pwqcheck```

**连同旧密码一起检查**

```pwqcheck -1 [old_password] [new_password]```

**从标准输入检查**

```pwqcheck < [password_file]```

**自定义配置**

```pwqcheck config=[/path/to/pwquality.conf]```

# SYNOPSIS

**pwqcheck** [_options_] [_check_params_]

# PARAMETERS

**-1**
> 从标准输入读取旧密码、新密码。

**-2**
> 只读取新密码。

**config=**_file_
> 使用指定的配置文件。

**min=**_n_
> 密码最小长度。

**max=**_n_
> 密码最大长度。

# DESCRIPTION

**pwqcheck** 依照可配置的规则检查密码质量。它是 passwdqc 的一部分，用于强制执行密码策略。

返回 OK 或描述弱点的错误信息。

# EXAMPLES

```bash
# Check single password
echo "mypassword" | pwqcheck

# With old password (change validation)
echo -e "oldpass\nnewpass" | pwqcheck -1

# Custom policy
echo "Test123!" | pwqcheck min=8 max=40

# In script
if echo "$password" | pwqcheck > /dev/null 2>&1; then
    echo "Password OK"
fi
```

# ERROR MESSAGES

```
Bad passphrase (too short)
Bad passphrase (not enough classes)
Bad passphrase (based on dictionary word)
Bad passphrase (too similar to old)
```

# CAVEATS

属于 passwdqc 软件包。与 pwquality/pam_pwquality 不同。应通过返回码判断校验结果。

# HISTORY

pwqcheck 是 **Solar Designer** 的 **passwdqc** 的一部分，提供主动式的密码质量检查。

# INSTALL

```apt: sudo apt install passwdqc```

```dnf: sudo dnf install passwdqc```

```zypper: sudo zypper install passwdqc```

```brew: brew install passwdqc```

```nix: nix profile install nixpkgs#passwdqc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwqgen](/man/pwqgen)(1), [passwd](/man/passwd)(1)
