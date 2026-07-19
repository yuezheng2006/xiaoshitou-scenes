# IP Profile: none（无品牌角色）

## 定位

无固定品牌 IP。画面以物件、结构、标签为主；需要信息演员时可用功能性简笔人，不绑定小石头或老杨。

```text
主角色 = 无
可选演员 = 简笔用户 / 简笔 AI（按需，非强制）
```

## Profile ID

`none`

## Profile Contract

契约模板：`../../references/contracts/profile-contract.md`。

```yaml
id: none
display_name: 无固定 IP
identity:
  canonical_asset: none
  anchors: []
references:
  ref_mode: none
  calibration: {}
behavior:
  actions: [指向, 搬运, 连接, 分拣]
qa:
  failure_signals: [误加入默认 IP, 误加入品牌资产]
privacy:
  public_assets: [通用物件与结构]
  private_assets: []
```

## 何时启用

用户说以下任一类意图时，切换到本 profile（不要再读 `default-little-stone` 的角色资产）：

- `不要人物` / `不要小石头` / `纯物件` / `无 IP` / `none`
- `只要结构图` / `只要流程图`（且明确不要角色）

未明确说 none 时，仍用默认 profile `default-little-stone`。

## 主角色

- 角色文件：`character.md`（none 语义，不是胶囊 IP）
- 无设定图、无校准图
- 触发词：见上

## 可选 Persona

无。禁止自动出现老杨或任何作者肖像。

## Logo 与品牌边界

沿用通用规则 `../../references/common-logo-safety.md`。本 profile 不附带品牌 Logo 资产。

## 读取顺序

1. 读取本文件确认 `$IP=none`。
2. 读取 `character.md` 获取 `{IP_DESC}` 与演员规则。
3. 跳过默认 profile 的 character / persona 资产。
4. 进入 `references/` 通用模式、母版、QA 与 `common-prompt-slots.md`（`{IP_STYLE_ADAPT}` 留空；`{REF_IMAGE}` 不传角色图）。

## 与默认 profile 的关系

本目录是**最小可运行 stub**，证明「换 IP / 不要 IP」只动 `ip-profiles/`。不要把 none 规则写回 `default-little-stone`。
