# TAGLINE

Ruby 测试框架，提供完整的测试设施

# TLDR

**运行所有测试**

```ruby -Ilib:test [test/test_*.rb]```

**运行指定测试文件**

```ruby -Ilib:test [test/test_example.rb]```

**以详细输出运行测试**

```ruby -Ilib:test [test/test_example.rb] --verbose```

**运行指定测试方法**

```ruby -Ilib:test [test/test_example.rb] --name [test_method_name]```

**按模式运行**

```ruby -Ilib:test [test/test_example.rb] --name /[pattern]/```

# SYNOPSIS

**ruby** -Ilib:test _test_file_ [_options_]

# PARAMETERS

**--verbose**
> 详细输出。

**--name** _pattern_
> 运行匹配的测试。

**--seed** _n_
> 随机种子。

**--pride**
> 彩虹输出。

# DESCRIPTION

**Minitest** 是一个 Ruby 测试框架，提供完整的测试设施。它包括单元测试、spec、mock 和基准测试。

Minitest 随 Ruby 附带，以快速和简洁著称。

# TEST EXAMPLE

```ruby
require 'minitest/autorun'

class TestExample < Minitest::Test
  def setup
    @value = 1
  end

  def test_addition
    assert_equal 2, @value + 1
  end
end
```

# SPEC SYNTAX

```ruby
describe Example do
  it "works" do
    _(1 + 1).must_equal 2
  end
end
```

# CAVEATS

自 Ruby 1.9 起随 Ruby 附带。默认随机顺序运行测试。功能比 RSpec 少但速度更快。

# HISTORY

Minitest 由 **Ryan Davis**（zenspider）创建，是一个极简的测试框架，自 Ruby **1.9** 起包含在 Ruby 标准库中。

# SEE ALSO

[rspec](/man/rspec)(1), [rake](/man/rake)(1), [ruby](/man/ruby)(1)
