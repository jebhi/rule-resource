# rule-resource

个人代理规则与相关资源的集中仓库。

## 目录结构

```text
.
├── rules/
│   └── classical/
│       ├── apple.yaml
│       ├── f1tv.yaml
│       ├── instagram.yaml
│       ├── meta.list
│       ├── n26.yaml
│       └── openai.yaml
├── config/
│   ├── surge.conf
│   └── clash.yaml
├── scripts/
│   └── sync-legacy.sh
├── .github/workflows/
│   └── validate-rules.yml
├── apple.yaml                  # 旧 Raw URL 兼容文件
├── openai.yaml                 # 旧 Raw URL 兼容文件
└── instagram (2).list          # 旧 Raw URL 兼容文件
```

## 规则文件

`rules/classical/` 中的文件均为可独立使用的 Clash/Mihomo classical rule-provider，包含顶层 `payload:` 字段。

推荐在配置中引用规范路径：

- `rules/classical/apple.yaml`
- `rules/classical/f1tv.yaml`
- `rules/classical/instagram.yaml`
- `rules/classical/n26.yaml`
- `rules/classical/openai.yaml`

### 纯文本规则（Surge / Mihomo 通用）

`.list` 文件为纯文本 classical 格式（每行一条规则，无 `payload:`），可同时用于 Surge 和 Mihomo：

- `rules/classical/meta.list`：Meta、Meta AI / Muse、Messenger、WhatsApp、Threads

Surge：

```ini
[Rule]
RULE-SET,https://raw.githubusercontent.com/jebhi/rule-resource/main/rules/classical/meta.list,Proxy
```

Mihomo（必须声明 `format: text`）：

```yaml
rule-providers:
  meta:
    type: http
    behavior: classical
    format: text
    url: https://raw.githubusercontent.com/jebhi/rule-resource/main/rules/classical/meta.list
    path: ./ruleset/meta.list
    interval: 86400

rules:
  - RULE-SET,meta,Proxy
```

## 完整配置

`config/` 中是完整的客户端配置，两份的策略组和规则保持一致：

- `config/surge.conf`：Surge
- `config/clash.yaml`：Mihomo（Clash Meta），由 Surge 配置转换而来

两份都不包含节点订阅，也不包含 MITM 证书私钥。真实订阅链接请在本地填写，不要提交到本仓库。

## 兼容策略

根目录中的 Apple、OpenAI 和 Instagram 文件暂时保留，避免现有 Raw URL 失效。规范目录是主要维护入口。

修改规范文件后，运行：

```bash
bash scripts/sync-legacy.sh
```

该脚本会同步更新根目录兼容文件。GitHub Actions 会检查两份内容是否一致。

## 维护约定

1. 文件名统一使用小写英文和连字符，避免空格、括号及自动生成的重复编号。
2. 可独立作为 rule-provider 使用的规则统一放入 `rules/classical/`。
3. 新增或修改兼容文件时，同步更新脚本和 CI 校验表。
4. 不在本仓库混放无关网页项目；独立网页或程序使用单独仓库。
