# Profile Contract · IP 配置契约

## 用途

Profile Contract 是 IP 的身份、参考资产、模式校准和质量失败信号的统一接口。

它是 profile 的索引契约，不替代现有的 `profile.md`、`character.md` 或 persona 文件：

- `profile.md`：入口、读取顺序、资产索引和边界。
- `character.md`：主角色身份、`{IP_DESC}`、`{IP_STYLE_ADAPT}` 和 Character Lock。
- persona 文件：真人 / 作者形象的身份与模式适配。
- 本契约：声明这些模块如何被路由、组装和验收。

## Profile 实例最小字段

每个 `ip-profiles/<ip-id>/profile.md` 至少应能回答以下问题：

```yaml
id: <ip-id>
display_name: <显示名称>
identity:
  canonical_asset: <用户提供的真实参考图路径，若为 none 则为空>
  reference_source: user_provided | generated_draft | none
  anchors: [<3-6 个身份锚点>]
  temperament: <一句话气质>
  description_source: character.md | profile.md
references:
  ref_mode: none | single | dual
  ref_mode_policy: <默认模式与升级条件>
  calibration:
    <mode-id>: <模式校准图路径或 none>
behavior:
  actions: [<可执行动作动词>]
  sequence_guide: <连续场景中的角色行为规则>
qa:
  failure_signals: [<识别失败信号>]
privacy:
  public_assets: [<可公开资产>]
  private_assets: [<仅本地 / 用户授权资产>]
input_kind: brand_mark | character_art | generated_draft
```

字段可以用 Markdown 表格或自然语言表达，但不能让 Prompt 临时发明身份规则。

## 参考图协议

`ref_mode` 描述当前运行真正可用的参考协议：

- `none`：无固定 IP，使用 `ip-profiles/none`，不传角色设定图。
- `single`：只有身份锚点，身份图回答“这是谁”。
- `dual`：身份锚点 + 当前模式校准图；身份图回答“这是谁”，校准图回答“在这个模式下怎么画”。

不能只有一张身份图却声称使用 `dual`。当前模式没有校准图时，运行降级为 `single`，并记录“可懒加载该模式校准图”，不阻塞普通内容任务。

profile 文件可以声明默认值，例如 `single`；当当前模式存在并实际传入校准图时，本次运行可以升级为 `dual`。因此 profile 的默认参考模式不等于每次运行的最终参考模式，最终值必须写入 Render Card / QA Card。

```text
Profile Identity → 角色是谁、主色、比例、核心特征
Mode Calibration → 该模式下的线条、材质、比例和表达方式
Scene Plan        → 当前画面画什么、做什么、写什么
```

## 输入类型（input_kind）

| input_kind | 含义 | Canonical 规则 |
| --- | --- | --- |
| brand_mark | Logo / App Icon / 扁平标识（**主路径**） | 原件即身份锚点；方标可用，不要求全身立绘 |
| character_art | 已有角色立绘 | 半身/胸像标记待补全，不得直接冒充全身 canonical |
| generated_draft | 无原件临时代绘 | 须用户明确同意；不得冒充 user_provided |

用户说「用这个 Logo / Icon / 品牌标 / App 图标做 IP」时，默认 `input_kind=brand_mark`。
品牌录入与 `logo-safety` 分工：logo-safety 管「默认流程不要乱出真 Logo」；Enrollment brand_mark 管「客户主动用自家标当 IP 身份」。

**brand_mark 录入硬规则：**

- brand_mark 录入不是「把 Logo 贴到小石头身上」；客户标即 IP 身份，不是给默认角色换皮。
- `brand_mark` 录入或切换 profile 期间，以及客户 profile 未进入 `AVAILABLE` 前，默认 profile `default-little-stone`（小石头）不得出镜、不得作为当前 IP 使用。
- Agent 必须创建或切换到客户 profile（`ip-profiles/<客户-ip-id>/`），进入 `profile_enrollment`；不得沿用默认小石头执行录入或配图。

客户真标默认 `private_assets`；公开仓不得分发第三方商标。

## IP 录入状态机

用户出现“录入 IP / 新建 IP / 上传形象 / 用这套形象”等意图时，进入独立的 `profile_enrollment` 路由，不进入普通内容生成。推荐路径是用户先提供一张真实图，系统将其作为身份锚点。

```text
REQUESTED → USER_REFERENCE → IDENTITY_PLAN → CONFIRMED → CANONICAL_ASSET
          → MODE_CALIBRATION（lazy）→ AVAILABLE
```

录入首轮规则：

1. 优先接收用户提供的真实图，并记录 `reference_source: user_provided`。
2. 建立 Profile Enrollment Card，只提取身份信息和缺口。
3. 用户没有确认身份方案前，不调用图片生成工具。
4. 半身 / 胸像可以先作为输入参考，但不能直接标记为全身 canonical asset；需标记为“待补全”。
5. 如果用户没有真实图，文字方案或生成草图只能标记为 `generated_draft`，必须得到用户明确同意后才能作为临时参考，不能默认替代真实图。
6. 参考图确认后，按需生成 **拟人 identity_sheet**（Layer 2，用户确认），再生成当前模式校准样张（Layer 3）。
7. 只有进入 `AVAILABLE` 后，才允许把该 IP 用于普通 Task Card。
8. `brand_mark`：方标/Icon 可作为 canonical，不要求全身立绘；**拟人化必须从头生长**——从 Icon/Logo 提取脸、发型、主色、气质，画完整场景角色；**禁止**把 App Icon 圆角方标直接当脑袋（icon-as-head）、禁止 stick figure 贴方图。须先有 **identity_sheet**（拟人设定图）再进模式校准，详见 `references/brand-mark-mode.md`。
9. `brand_mark` 模式校准与正式配图：**非必要不要纯黑白**——手绘/白板默认保留 Icon 主色与少量功能色（橙路径、红重点、蓝补充，见 `handdrawn-style-dna.md`）；只有用户明确要求「纯线稿 / 黑白」时才全 monochrome。

Profile Enrollment Card 至少包含：

```text
状态：REQUESTED / USER_REFERENCE / IDENTITY_PLAN / CONFIRMED / CANONICAL_ASSET / AVAILABLE
用户原话：
IP ID / 名称：
input_kind：brand_mark / character_art / generated_draft
原件类型：logo | app_icon | flat_mark | character_sheet | other
授权确认：已确认可本地使用 / 未确认（阻塞公开分发）
身份锚点：
一句话气质：
设定图：缺失 / 用户真实图-半身待补全 / 用户真实图-全身可用 / 生成草图-待授权
拟人设定图 identity_sheet：缺失 / 已确认 / 待确认（brand_mark 必填）
当前模式校准：none / single / dual
待确认项：
下一动作：
```

## 行为、QA 与发布

`actions` 供 Plan Card 选择主角色动作；`sequence_guide` 约束连续场景中的角色是否沿故事路径行动，避免复制角色或让角色站桩装饰。

`failure_signals` 供 QA Card 做 Profile / Character Lock 检查。失败应定位到 Profile / 资产 / QA 层，不应通过修改当前场景内容掩盖身份漂移。

公共仓库只分发 `public_assets`。真人参考图、品牌 Logo 和用户上传的自定义 IP 默认属于 `private_assets`，未经授权不得进入公开示例、Prompt 模板或提交历史。
