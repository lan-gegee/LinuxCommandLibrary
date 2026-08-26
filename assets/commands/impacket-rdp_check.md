# TAGLINE

验证给定凭据能否访问 Windows 系统的 RDP

# TLDR

**检查 RDP 凭据是否有效**

```impacket-rdp_check '[domain]/[user]:[password]@[192.168.1.100]'```

**使用 NTLM 哈希检查 RDP 访问**

```impacket-rdp_check -hashes ':[nthash]' '[domain]/[user]@[192.168.1.100]'```

**在非标准端口上检查 RDP**

```impacket-rdp_check '[domain]/[user]:[password]@[192.168.1.100]:3390'```

# SYNOPSIS

**impacket-rdp_check** [_-h_] [_-hashes LMHASH:NTHASH_] _target_

# PARAMETERS

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证

# DESCRIPTION

**impacket-rdp_check** 验证给定的凭据能否通过 RDP（远程桌面协议）访问 Windows 系统。它尝试完成 RDP 身份验证但不建立完整会话，因此在渗透测试中适合用来验证凭据。

该工具执行初始的 RDP 握手和身份验证交换，并报告目标系统是否接受这些凭据。

# CAVEATS

仅验证凭据；不建立完整的 RDP 会话。目标上的网络级身份验证（NLA）设置会影响行为。目标必须启用且可访问 RDP。反复使用错误凭据可能触发账户锁定策略。

# HISTORY

属于 SecureAuth 的 **Impacket** 库。适用于在不承担建立完整图形会话开销的情况下，对 RDP 服务验证凭据。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xfreerdp](/man/xfreerdp)(1), [rdesktop](/man/rdesktop)(1), [nmap](/man/nmap)(1)
