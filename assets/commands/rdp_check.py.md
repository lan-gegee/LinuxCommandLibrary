# TAGLINE

测试 RDP 身份验证凭据

# TLDR

对目标**测试 RDP 凭据**

```rdp_check.py [domain]/[username]:[password]@[target_ip]```

**使用 NTLM 哈希测试凭据**

```rdp_check.py [domain]/[username]@[target_ip] -hashes [LMHASH]:[NTHASH]```

**带调试输出测试**

```rdp_check.py [domain]/[username]:[password]@[target_ip] -debug```

**通过 IPv6 测试**

```rdp_check.py [domain]/[username]:[password]@[target_ip] -6```

# SYNOPSIS

**rdp_check.py** [**-h**] [**-hashes** _LMHASH:NTHASH_] [**-6**] [**-debug**] _target_

# PARAMETERS

_target_
> 目标格式：[[domain/]username[:password]@]<hostname or IP>

**-hashes** _LMHASH:NTHASH_
> 使用 NTLM 哈希而非密码进行身份验证

**-6**, **--ipv6**
> 使用 IPv6 连接

**-debug**
> 启用调试输出

**-ts**
> 在日志输出中加入时间戳

**-h**, **--help**
> 显示帮助消息

# DESCRIPTION

**rdp_check.py** 是一款 Impacket 工具，通过 RDP（远程桌面协议）测试凭据对 Windows 主机是否有效。它实现了 MS-RDPBCGR 和 MS-CREDSSP 的部分内容来执行 CredSSP 身份验证。

该工具适用于在获授权的安全评估中验证凭据、确认 RDP 访问能力，以及针对启用了 RDP 的系统测试哈希传递攻击。

它只执行身份验证，不会建立完整的 RDP 会话。身份验证成功表明凭据有效，但不保证能获得交互式桌面访问（这可能受组策略或用户权限限制）。

# CAVEATS

**必须获得授权**：只能对你有明确许可的系统使用此工具。未经授权的访问尝试属于违法行为。

该工具不完成完整的 RDP 握手，因此身份验证成功并不保证能访问 GUI。网络级身份验证（NLA）设置和用户权限分配仍可能阻止实际登录。

哈希传递攻击（**-hashes**）要求目标接受 NTLM 身份验证。现代配置可能限制 NTLM 而改用 Kerberos。

Impacket 工具需要 Python 和 impacket 库。通过 **pip install impacket** 安装，或使用自带 impacket-scripts 的 Kali Linux。

# INSTALL

```apk: sudo apk add py3-impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xfreerdp](/man/xfreerdp)(1), [rdesktop](/man/rdesktop)(1), [nmap](/man/nmap)(1), [crackmapexec](/man/crackmapexec)(1)
