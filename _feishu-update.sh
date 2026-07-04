#!/bin/bash
set -euo pipefail
DOC="UZaWdBpyLoQi6Hx37TKcWx2rnmd"
ROOT="/Users/vincentyangmbp/Documents/github/xiaoshitou-scenes"
cd "$ROOT"

# 示例：数字标题 + 干嘛用 + prompt + 图
append_example() {
  local num="$1"
  local title="$2"
  local use="$3"
  local prompt="$4"
  lark-cli docs +update --api-version v2 --doc "$DOC" --command append \
    --doc-format markdown \
    --content "$(cat <<EOF

### ${num}. ${title}

**干嘛用**：${use}

\`\`\`text
${prompt}
\`\`\`

EOF
)"
}

insert_img() {
  local relpath="$1"
  local caption="$2"
  lark-cli docs +media-insert --doc "$DOC" \
    --file "$relpath" --align center --caption "$caption" --width 720
  sleep 0.4
}

append_text_only() {
  local num="$1"
  local title="$2"
  local use="$3"
  local prompt="$4"
  local output="$5"
  lark-cli docs +update --api-version v2 --doc "$DOC" --command append \
    --doc-format markdown \
    --content "$(cat <<EOF

### ${num}. ${title}

**干嘛用**：${use}

\`\`\`text
${prompt}
\`\`\`

**会得到**（不生图）：

\`\`\`text
${output}
\`\`\`

EOF
)"
}

echo "==> overwrite intro"
lark-cli docs +update --api-version v2 --doc "$DOC" --command overwrite \
  --content @_feishu-doc-intro.xml

# --- 小石头单 IP · 四种模式 ---

append_example "1" "实物图 · 处境正文" \
  "文章/观点配图；未指定模式时，处境类内容自动走实物图。" \
  "小石头实物图：权限卡挡住了新消息，出一张 16:9 正文配图。"
insert_img "assets/examples/gallery/physical-illustration-low-density.png" "出图效果"

append_example "2" "实物图 · 设备巡检" \
  "白底真实物件小现场：麦克风、充电座、消毒巾等；只有小石头，无老杨。" \
  "小石头实物图：麦克风要充电、还一支、先消毒。"
insert_img "assets/test-output/17-microphone-maintenance.png" "出图效果"

append_example "3" "手绘图 · 工作流解释" \
  "流程、结构、方法论；未指定模式时，结构类内容自动走手绘图。" \
  "小石头手绘图：解释这个 Agent 工作流。"
insert_img "assets/examples/gallery/handdrawn-illustration-medium.png" "出图效果"

append_example "4" "知识卡 · 四步方法" \
  "竖版 3:4 / 4:5 收藏传播图；步骤、对比、课程总览。" \
  "小石头知识卡：把四步内容复用做成 4:5 收藏图。"
insert_img "assets/examples/gallery/knowledge-card-high-density.png" "出图效果"

append_example "5" "知识卡 · 行动清单" \
  "诊断 + 今日行动；适合图文号、朋友圈转发。" \
  "小石头知识卡：诊断清单 + 今日行动，竖版传播。"
insert_img "assets/test-output/test-knowledge-card-action-checklist.png" "出图效果"

append_example "6" "知识卡 · 观点海报（9:16）" \
  "一句话反常识判断；手机海报 / 直播切片引流。" \
  "小石头知识卡：一句反常识判断，9:16 手机海报。"
insert_img "assets/test-output/test-knowledge-card-opinion-poster.png" "出图效果"

append_example "7" "PPT · 封面页" \
  "整套 16:9 演讲页；先出导演规划卡，再分批出图。" \
  "我要做 10 页直播分享 PPT，主题是 Agent 工作流，先出导演规划卡。"
insert_img "assets/examples/ppt-mode/01-cover.png" "出图效果 · 封面"

append_example "8" "PPT · 方法页" \
  "演讲中段拆步骤、讲方法。" \
  "按大纲逐页出图：第 5 页，方法拆解。"
insert_img "assets/examples/ppt-mode/05-method.png" "出图效果 · 方法页"

append_example "9" "PPT · 收尾页" \
  "总结、行动号召、下一步。" \
  "按大纲逐页出图：最后一页，收尾。"
insert_img "assets/examples/ppt-mode/08-closing.png" "出图效果 · 收尾"

append_example "10" "彩蛋长卷 · 项目复盘" \
  "超横版 2.6:1 故事线；个人经历、产品演化、成长路径。" \
  "彩蛋长卷：项目复盘与成长路径，5–8 个物件节点一条线讲完。"
insert_img "assets/examples/gallery/capabilities/capability-long-scroll.png" "出图效果"

append_example "11" "实物图 · 值班工单" \
  "工牌 + 服务工单类现场；批量出图时每张仍是独立物件小现场，只有小石头。" \
  "小石头实物图：值班工牌挂着服务工单，标签：值班中 / 先处理 / 去现场。"
insert_img "assets/test-output/18-employee-badge.png" "出图效果"

append_example "12" "多人协作 · 多 Agent" \
  "2–4 个小石头同图协作；形体一致锁，动作分工不同。" \
  "小石头实物图：3 个 Agent 递卡、接卡、贴标签，16:9 白底真实物件小现场。"
insert_img "assets/examples/gallery/gallery-physical-multi-agent-handoff.png" "出图效果"

# --- 老杨 × 小石头 双 IP ---

append_text_only "13" "老杨 · 先推荐方案" \
  "长文粘贴后不确定怎么配；只出方案，不逼你先选模式。" \
  "老杨：这篇 2000 字长文讲 Agent 工作流，想配图，请先推荐，不要生图。" \
  "推荐 3 张 · 手绘图 1 张（工作流总览，双 IP 白板拆解）
       · 实物图 2 张（痛点处境 + 返工卡点）
互动：老杨画结构批注，小石头拉线搬模块
尺寸：16:9"

append_example "14" "双 IP · 白板手绘" \
  "触发「老杨 / 老杨和小石头」；老杨讲结构，小石头执行。" \
  "老杨和小石头：把这个 Agent 工作流画成一张白板图。"
insert_img "assets/test-output/test-author-persona-handdrawn-routing.png" "出图效果"

append_example "15" "双 IP · 知识卡主讲" \
  "老杨指向结论，小石头在模块里分工执行。" \
  "老杨：把这套四步方法做成 4:5 知识卡，我主讲，小石头执行。"
insert_img "assets/examples/gallery/gallery-dual-ip-knowledge-card.png" "出图效果"

append_example "16" "实物图 · 服务票现场" \
  "K 歌 / 门店服务类道具气味；小石头单 IP，真实票卡 + 麦克风小现场。" \
  "小石头实物图：优先处理下一首、有呼叫的服务票，16:9 正文配图。"
insert_img "assets/test-output/16-karaoke-service-ticket.png" "出图效果"

append_example "17" "双 IP · 手绘分镜对比" \
  "踩坑复盘、前后变化；同一小石头两格表情靠动作/汗滴，不靠换眼法或加嘴。" \
  "老杨和小石头：把这次失败到修正的过程画成分镜对比白板图。"
insert_img "assets/examples/gallery/gallery-dual-ip-handdrawn-comic-compare.png" "出图效果"

append_example "18" "双 IP · 手绘系统拆解" \
  "Agent 结构解释；2 个小石头同胶囊比例，A 拉反馈 B 送上下文，仅缩放/动作不同。" \
  "老杨和小石头：拆解这个 Agent 系统的输入、处理、输出三个模块。"
insert_img "assets/examples/gallery/gallery-dual-ip-handdrawn-system-map.png" "出图效果"

# --- 全身 IP 锚点 ---

append_example "19" "全身 · 双 IP 并列" \
  "README / 文档里展示「老杨讲，小石头干」；全身线稿，Persona + Character Lock。" \
  "老杨和小石头：出一张全身并列角色说明图，标注主讲和执行分工。"
insert_img "assets/examples/gallery/gallery-dual-ip-fullbody-handdrawn-stand.png" "出图效果"

append_example "20" "全身 · 双 IP 流程讲解" \
  "全身互动：老杨指结构，小石头拉反馈线；Confirm Gate 跨图老杨一致。" \
  "老杨和小石头：全身出镜，讲解输入→处理→输出，小石头负责拉反馈。"
insert_img "assets/examples/gallery/gallery-dual-ip-fullbody-handdrawn-walkthrough.png" "出图效果"

append_example "21" "全身 · 双 IP 递卡协作" \
  "全身动态协作：老杨蹲身递卡，小石头接卡执行。" \
  "老杨和小石头：全身递卡协作，白底线稿风。"
insert_img "assets/examples/gallery/gallery-dual-ip-fullbody-handdrawn-handoff.png" "出图效果"

append_example "22" "全身 · 实物同框" \
  "实物模式双 IP：风格化 3D 老杨 + flat 2D 小石头，全身同框。" \
  "老杨和小石头：白底实物小现场，全身同框，小石头拿执行卡。"
insert_img "assets/examples/gallery/gallery-dual-ip-fullbody-physical-stand.png" "出图效果"

append_example "23" "全身 · 小石头动作锚点" \
  "小石头单 IP 全身五动作：站/跑/拉/接/倔；同胶囊比例，无嘴。" \
  "小石头手绘图：出一排全身动作锚点，五格同形体只改姿态。"
insert_img "assets/examples/gallery/gallery-little-stone-fullbody-actions-row.png" "出图效果"

echo "==> done"
