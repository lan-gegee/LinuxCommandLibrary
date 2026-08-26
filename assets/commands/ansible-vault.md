# TAGLINE

加密和解密敏感数据

# TLDR

**创建**新的加密文件

```ansible-vault create [secrets.yml]```

**加密**现有文件

```ansible-vault encrypt [file.yml]```

**解密**文件

```ansible-vault decrypt [secrets.yml]```

**编辑**加密文件

```ansible-vault edit [secrets.yml]```

**查看**加密文件内容

```ansible-vault view [secrets.yml]```

**加密**字符串

```ansible-vault encrypt_string '[secret_value]' --name '[variable_name]'```

**重新设密**（更改密码）

```ansible-vault rekey [secrets.yml]```

# SYNOPSIS

**ansible-vault** _command_ [_--vault-password-file file_] [_options_] _files_

# DESCRIPTION

**ansible-vault** 对 Ansible 项目中的敏感数据（如密码、密钥和凭据）进行加密。它使用 AES256 加密保护文件，同时允许这些文件直接在 playbook 中使用。

加密后的文件可以直接编辑、查看并在 playbook 中使用，无需手动解密；只要提供 vault 密码，ansible-playbook 会自动完成解密。

# PARAMETERS

**create** _file_
> 创建新的加密文件

**encrypt** _files_
> 加密现有文件

**decrypt** _files_
> 解密文件

**edit** _file_
> 就地编辑加密文件

**view** _file_
> 查看加密文件内容

**encrypt_string** _string_
> 加密一个字符串，以便嵌入 playbook 或 vars 文件

**rekey** _files_
> 使用新密码重新加密文件

**--vault-password-file** _file_
> 存放 vault 密码的文件

**--vault-id** _label@source_
> 要使用的 vault 身份（标签加密码来源）

**-J**, **--ask-vault-pass**
> 提示输入 vault 密码

**-n** _name_, **--name** _name_
> 要赋予的变量名（仅限 encrypt_string）

**--encrypt-vault-id** _id_
> 加密时使用的 vault id（当提供了多个时）

**--output** _file_
> 将输出写入指定文件而不是 stdout

**--new-vault-password-file** _file_
> 为 rekey 保存新密码的密码文件

**--new-vault-id** _id_
> 为 rekey 保存新密码的 vault id

# CONFIGURATION

**/etc/ansible/ansible.cfg**
> 系统级 Ansible 配置，包含 vault 密码文件路径和 vault 身份设置。

**~/.ansible.cfg**
> 每用户 Ansible 配置，覆盖系统默认值。

**ansible.cfg**
> 当前目录中的项目级配置，优先级最高。

# CAVEATS

运行 playbook 期间必须能获取 vault 密码。加密文件应提交到版本控制，但绝不能提交密码。需要多个密码时请使用 vault-id。

# HISTORY

**ansible-vault** 在 Ansible 1.5（**2014 年**）中引入，用于满足自动化过程中安全处理敏感数据的需求。多 vault 密码支持在 Ansible 2.4 中加入。

# INSTALL

```dnf: sudo dnf install ansible-core```

```pacman: sudo pacman -S ansible-core```

```apk: sudo apk add ansible-core```

```zypper: sudo zypper install ansible-core```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ansible-playbook](/man/ansible-playbook)(1), [ansible](/man/ansible)(1), [gpg](/man/gpg)(1)

# RESOURCES

```[Source code](https://github.com/ansible/ansible)```

```[Documentation](https://docs.ansible.com/ansible/latest/cli/ansible-vault.html)```

<!-- verified: 2026-06-11 -->
