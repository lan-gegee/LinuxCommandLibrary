# TAGLINE

通过 WS-Management 进行远程 Windows 管理

# TLDR

在 Windows 主机上**执行命令**（通过 pywinrm Python 库）

```python -c "import winrm; s = winrm.Session('[host]', auth=('[user]', '[pass]')); print(s.run_cmd('ipconfig').std_out)"```

在远程 Windows 主机上**执行 PowerShell 命令**

```python -c "import winrm; s = winrm.Session('[host]', auth=('[user]', '[pass]')); print(s.run_ps('Get-Process').std_out)"```

**使用 HTTPS 连接**（端口 5986）

```python -c "import winrm; s = winrm.Session('[host]', auth=('[user]', '[pass]'), transport='ssl'); print(s.run_cmd('hostname').std_out)"```

**使用 NTLM 认证连接**

```python -c "import winrm; s = winrm.Session('[host]', auth=('[domain\\user]', '[pass]'), transport='ntlm'); print(s.run_cmd('whoami').std_out)"```

# SYNOPSIS

**winrm**（通过 pywinrm Python 库）

```python
import winrm
session = winrm.Session(_host_, auth=(_user_, _password_), transport=_method_)
result = session.run_cmd(_command_, [_args_])
result = session.run_ps(_powershell_script_)
```

# PARAMETERS

**host**
> Windows 目标主机名或 IP 地址。

**auth**
> 用于认证的 (用户名, 密码) 元组。

**transport**
> 认证方式：basic、ntlm、kerberos、ssl 或 credssp。

**run_cmd**(_command_, [_args_])
> 执行 Windows 命令（cmd.exe）。

**run_ps**(_script_)
> 执行 PowerShell 脚本。

**std_out**
> 命令执行的标准输出。

**std_err**
> 命令执行的标准错误。

**status_code**
> 所执行命令的退出码。

# DESCRIPTION

**pywinrm** 是一个用于 Windows 远程管理（WinRM）的 Python 库，可以从 Linux 或其他系统在 Windows 机器上执行命令。WinRM 是 Microsoft 对 WS-Management 协议的实现，提供类似 SSH 的远程管理能力。

该库支持多种认证方式：Basic（需要 HTTPS 或非加密配置）、NTLM（适用于域账户和本地账户）、Kerberos（用于域环境）和 CredSSP（允许凭据委托）。连接使用 HTTP 端口 5985 或 HTTPS 端口 5986。

pywinrm 被 Ansible 等自动化工具广泛用于 Windows 管理。它既能执行 cmd.exe 命令（run_cmd），也能执行 PowerShell 脚本（run_ps），并返回输出、错误和退出码。

Windows 主机必须启用 WinRM（Enable-PSRemoting -Force），并配置为接受所选的认证方式。

# CAVEATS

WinRM 通过 HTTP 通信时默认不加密；出于安全考虑请使用 HTTPS 或 NTLM/Kerberos 传输方式。Windows 主机上需要显式启用 Basic 认证。Kerberos 需要正确的域配置和 kinit 初始化。防火墙规则必须放行 WinRM 端口（5985/5986）。

# HISTORY

**WinRM**（Windows Remote Management）由 **Microsoft** 在 **Windows Vista** 和 **Server 2008** 中引入，是 WS-Management 标准的一部分。**pywinrm** 的开发使得从非 Windows 系统上用 Python 访问 WinRM 成为可能。该库成为跨平台 Windows 管理的关键组件，尤其随着 **Ansible** 自 **2014 年前后**开始支持 Windows 而广受关注。

# SEE ALSO

[ssh](/man/ssh)(1), [ansible](/man/ansible)(1), [powershell](/man/powershell)(1)
