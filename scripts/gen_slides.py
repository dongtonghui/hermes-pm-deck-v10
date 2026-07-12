import os, re, html

base = "/Users/krisdong/Documents/Claude_StevenUse/0715_outputs/hermes-pm-deck-publish-v8"
slides_dir = os.path.join(base, "slides")

def page_html(num, title, section, layout, content, kicker=None, subtitle=None, theme="default"):
    num_str = f"{num:02d}"
    section_label = html.escape(section)
    page_title = html.escape(title)
    
    theme_classes = "page"
    if theme == "cover": theme_classes = "page cover-bg"
    elif theme == "chapter": theme_classes = "page chapter-bg"
    
    kicker_html = f'<div class="kicker">{html.escape(kicker)}</div>' if kicker else ""
    subtitle_html = f'<div class="subtitle">{html.escape(subtitle)}</div>' if subtitle else ""
    
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>P{num_str} · {page_title}</title>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400&family=Noto+Serif+SC:wght@400;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../shared/tokens.css">
</head>
<body class="{theme_classes}">
  <div class="masthead">
    <div class="brand">AI × Hardware PM</div>
    <div>Internal Training · V8</div>
  </div>
  {kicker_html}
  <h1>{page_title}</h1>
  {subtitle_html}
  {content}
  <div class="page-footer">
    <div class="section-tag">{section_label}</div>
    <div class="page-number">{num_str} / 35</div>
  </div>
</body>
</html>
"""

slides = [
    # 1: cover (already created, skip)
    # 2
    {"num": 2, "title": "自我介绍", "section": "开场与语境建立", "kicker": "About",
     "subtitle": "把复杂工作流程拆解成可协作、可复用的数字角色",
     "theme": "default",
     "content": """<div class="two-col" style="margin-top:20px">
  <div>
    <div class="body-text">
      <p><strong>背景</strong>：头部互联网 / 跨境电商 / 兴趣电商 / 数字员工平台创业。</p>
      <p style="margin-top:22px">长期关注一件事：如何让产品经理用 AI 把"做不过来"的信息处理链条，拆成一组能持续配合的数字角色。</p>
    </div>
  </div>
  <div>
    <div class="quote-big">"AI 协作的本质，不是替代人，而是把一个人做不过来的信息处理链条，拆成一组能持续配合的数字角色。"</div>
  </div>
</div>"""},
    
    # 3
    {"num": 3, "title": "今天的议程", "section": "开场与语境建立", "kicker": "Agenda",
     "subtitle": "三个模块 · 七个可带走模板",
     "theme": "default",
     "content": """<div class="list-stack" style="margin-top:10px">
  <div class="list-item">
    <div class="num">1</div>
    <div class="content">
      <h3>范式转变：AI 可以怎么协作</h3>
      <p>从"打开网页问问题"到"给目标、多角色协作、自动化执行"。</p>
    </div>
  </div>
  <div class="list-item">
    <div class="num">2</div>
    <div class="content">
      <h3>三个核心场景实战</h3>
      <p>多 Agent 需求分析 · Reddit 情报抓取 · 自定义 Skill 封装。</p>
    </div>
  </div>
  <div class="list-item">
    <div class="num">3</div>
    <div class="content">
      <h3>自动化：定时任务 + 消息渠道打通</h3>
      <p>让 AI 在后台持续运转，飞书 / 钉钉随时指挥。</p>
    </div>
  </div>
</div>
<div class="body-text" style="margin-top:40px"><strong>带走什么</strong>：多 Agent 模板、情报抓取模板、Skill 规范、定时任务清单等 7 份可复用资产。</div>"""},

    # 4
    {"num": 4, "title": "旧范式：AI = 聊天框", "section": "开场与语境建立", "kicker": "Old Paradigm",
     "subtitle": "适合简单任务，但难以承担复杂分析",
     "theme": "default",
     "content": """<div class="two-col" style="margin-top:30px">
  <div class="card accent">
    <h3>典型用法</h3>
    <p>打开网页 → 输入问题 → 等待回答</p>
    <p style="margin-top:16px">像一个单次对话的问答工具，答案质量高度依赖 Prompt 的一次性精确度。</p>
  </div>
  <div>
    <div class="list-stack">
      <div class="list-item">
        <div class="num" style="background:var(--accent-warm)">✓</div>
        <div class="content"><h3>适合</h3><p>简单问答、文案润色、代码片段</p></div>
      </div>
      <div class="list-item">
        <div class="num" style="background:var(--danger)">✕</div>
        <div class="content"><h3>不适合</h3><p>复杂分析、需要数据支撑、需要多轮校验的任务</p></div>
      </div>
    </div>
  </div>
</div>"""},

    # 5
    {"num": 5, "title": "新范式：AI = 可协作的数字角色团队", "section": "开场与语境建立", "kicker": "New Paradigm",
     "subtitle": "你给目标，AI 自己规划、协作与执行",
     "theme": "chapter",
     "content": """<div class="flow" style="margin-top:40px">
  <div class="flow-node"><strong>给目标</strong><span>不再逐句 Prompt</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>AI 规划</strong><span>拆解任务与路径</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>多角色校验</strong><span>互相找漏洞</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>人做决策</strong><span>最终判断与取舍</span></div>
</div>
<div class="body-text" style="margin-top:50px; color:rgba(255,255,255,0.85)">
  AI 可以读取文档、抓取网页、调用 Skill；多个 AI 可以扮演不同角色互相校验。人可以像项目经理一样指挥和决策。
</div>"""},

    # 6
    {"num": 6, "title": "四级进阶：从 Chat 到深度协作", "section": "AI 协作范式进阶", "kicker": "Maturity",
     "subtitle": "每升一级，AI 承担的工作就越多，人的角色越向决策靠拢",
     "theme": "default",
     "content": """<div class="table-wrap">
  <table>
    <tr>
      <th style="width:12%">级别</th>
      <th style="width:18%">名称</th>
      <th style="width:35%">核心特征</th>
      <th style="width:35%">示例</th>
    </tr>
    <tr>
      <td><span class="badge red">L1</span></td>
      <td>纯 Chat</td>
      <td>直接要答案</td>
      <td>"帮我写一份 PRD"</td>
    </tr>
    <tr>
      <td><span class="badge orange">L2</span></td>
      <td>给 Goal</td>
      <td>AI 规划路径</td>
      <td>"我要做植物生长灯，先帮我梳理需求分析框架"</td>
    </tr>
    <tr>
      <td><span class="badge blue">L3</span></td>
      <td>引入 Skill / 数据 / 网络</td>
      <td>读取真实数据、调用方法论</td>
      <td>"用需求分析 Skill，读取竞品文档，抓取 Reddit 讨论"</td>
    </tr>
    <tr>
      <td><span class="badge green">L4</span></td>
      <td>多 Agent 协作与自动化</td>
      <td>多角色校验 + 定时执行</td>
      <td>"用户 Agent 和技术 Agent 分别分析，再由评审 Agent 找漏洞"</td>
    </tr>
  </table>
</div>"""},

    # 7
    {"num": 7, "title": "降低 AI 幻觉的四个方法", "section": "AI 协作范式进阶", "kicker": "Anti-Hallucination",
     "subtitle": "AI 是加速器，不是背书人",
     "theme": "default",
     "content": """<div class="card-grid">
  <div class="card accent">
    <h3>1 · 绑定真实数据</h3>
    <p>让 AI 读真实评论、问卷、访谈记录，而非凭空推断。</p>
  </div>
  <div class="card accent">
    <h3>2 · 多 Agent 互相校验</h3>
    <p>不同角色 Agent 分别找证据、挑毛病，交叉验证结论。</p>
  </div>
  <div class="card accent">
    <h3>3 · 要求列出不确定项</h3>
    <p>明确标注"事实 / 推测 / 待验证"，不伪装确定性。</p>
  </div>
  <div class="card accent">
    <h3>4 · 人在回路做决策</h3>
    <p>AI 负责收集整理，人负责最终判断、优先级与取舍。</p>
  </div>
</div>
<div class="quote-big" style="margin-top:46px">核心原则：AI 负责把信息摆在你面前，你负责决定相信什么、放弃什么。</div>"""},

    # 8
    {"num": 8, "title": "硬件 PM 的日常工作痛点", "section": "AI 协作范式进阶", "kicker": "Pain Points",
     "subtitle": "信息分散、分析耗时、重复劳动多",
     "theme": "default",
     "content": """<div class="list-stack">
  <div class="list-item">
    <div class="num">1</div>
    <div class="content"><h3>信息分散</h3><p>Reddit、Discord、电商评论、行业报告散落在各处，搜集成本高。</p></div>
  </div>
  <div class="list-item">
    <div class="num">2</div>
    <div class="content"><h3>调研报告化</h3><p>访谈、问卷整理耗时，从原始材料到洞察产出慢。</p></div>
  </div>
  <div class="list-item">
    <div class="num">3</div>
    <div class="content"><h3>PRD 从零写</h3><p>每次重新搭结构，格式不统一，难以复用团队资产。</p></div>
  </div>
  <div class="list-item">
    <div class="num">4</div>
    <div class="content"><h3>AI 幻觉不敢用</h3><p>让 AI 写分析，怕它编结论，缺乏验证机制。</p></div>
  </div>
  <div class="list-item">
    <div class="num">5</div>
    <div class="content"><h3>重复工作无法自动化</h3><p>日报、周报、情报监控靠人工，难以持续。</p></div>
  </div>
</div>"""},

    # 9
    {"num": 9, "title": "可复用的 AI 工作流骨架", "section": "AI 协作范式进阶", "kicker": "Framework",
     "subtitle": "从输入到自动化，完整闭环",
     "theme": "default",
     "content": """<div class="flow" style="flex-wrap:wrap; margin-top:30px">
  <div class="flow-node"><strong>输入</strong><span>目标 + 约束 + 数据</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>多角色分析</strong><span>用户 / 技术 / 商业 / 竞品</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>交叉校验</strong><span>互相找漏洞、补遗漏</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>人工决策</strong><span>优先级、取舍、判断</span></div>
</div>
<div class="flow" style="margin-top:20px">
  <div class="flow-node"><strong>输出</strong><span>PRD / 报告 / 原型 / 决策记录</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>自动化</strong><span>定时执行、消息推送</span></div>
</div>
<div class="body-text" style="margin-top:40px">这个骨架适用于需求分析、竞品调研、情报监控、PRD 撰写等几乎所有硬件 PM 高频任务。</div>"""},

    # 10
    {"num": 10, "title": "今天核心案例预览", "section": "AI 协作范式进阶", "kicker": "Cases",
     "subtitle": "以「植物生长照射仪」贯穿四个场景",
     "theme": "default",
     "content": """<div class="three-col" style="margin-top:20px">
  <div class="card accent">
    <div class="badge orange" style="margin-bottom:14px">场景 1</div>
    <h3>多 Agent 需求分析</h3>
    <p>带氛围灯功能的植物生长照射仪：是真需求还是伪需求？</p>
  </div>
  <div class="card accent">
    <div class="badge orange" style="margin-bottom:14px">场景 2</div>
    <h3>Reddit 情报抓取</h3>
    <p>从 r/IndoorGarden 等社区抓取真实用户讨论，提炼洞察。</p>
  </div>
  <div class="card accent">
    <div class="badge orange" style="margin-bottom:14px">场景 3</div>
    <h3>自定义 Skill</h3>
    <p>把植物灯分析流程封装成可复用的 hardware-pm-requirement-analysis Skill。</p>
  </div>
</div>
<div class="card accent" style="margin-top:28px">
  <div class="badge green" style="margin-bottom:14px">场景 4 & 5</div>
  <h3>定时情报报告 + 消息渠道打通</h3>
  <p>每周一自动输出 Reddit 情报周报，并推送到飞书 / 钉钉；在群里用自然语言触发 Skill。</p>
</div>"""},

    # 11
    {"num": 11, "title": "场景引入：PRD 前的需求分析之痛", "section": "场景一：多 Agent 需求分析", "kicker": "Scenario 1",
     "subtitle": "让 AI 写需求分析，常常得到一堆常识",
     "theme": "default",
     "content": """<div class="two-col" style="margin-top:20px">
  <div class="card accent">
    <h3>典型问题</h3>
    <ul>
      <li>视角单一：只有一个"全能 AI"回答，容易遗漏关键维度。</li>
      <li>AI 幻觉：输出看似合理，但缺乏证据。</li>
      <li>难以争辩：没有人质疑、补漏、找矛盾。</li>
    </ul>
  </div>
  <div>
    <div class="quote-big">"让 AI 写智能水杯需求分析，输出都是常识。"</div>
    <div class="body-text" style="margin-top:20px">真正的需求分析，需要多个专业视角互相争论、互相校验。</div>
  </div>
</div>"""},

    # 12
    {"num": 12, "title": "核心案例：带氛围灯功能的植物生长照射仪", "section": "场景一：多 Agent 需求分析", "kicker": "Case",
     "subtitle": "氛围灯是真需求还是伪需求？",
     "theme": "default",
     "content": """<div class="two-col" style="margin-top:20px">
  <div class="card accent">
    <h3>产品背景</h3>
    <p>现有功能：全光谱 LED、定时开关、亮度调节、悬挂安装。</p>
    <p style="margin-top:14px">拟新增功能：RGB 氛围灯，可在不种植时作为家居氛围灯使用。</p>
  </div>
  <div class="card accent">
    <h3>团队假设</h3>
    <p>氛围灯能让产品更有差异化，提升家居场景颜值，形成独特卖点。</p>
    <p style="margin-top:14px"><strong>问题</strong>：这是真需求，还是伪需求？</p>
  </div>
</div>
<div class="quote-big" style="margin-top:40px">我们的目标不是证明氛围灯"好"或"不好"，而是用多视角证据来检验它是否值得投入。</div>"""},

    # 13
    {"num": 13, "title": "多 Agent 互相 argue 的方法", "section": "场景一：多 Agent 需求分析", "kicker": "Method",
     "subtitle": "不追求一次出完美答案，让不同角色先吵清楚",
     "theme": "default",
     "content": """<div class="list-stack">
  <div class="list-item">
    <div class="num">1</div>
    <div class="content"><h3>分别提观点</h3><p>每个 Agent 从自己的专业视角独立输出分析，不互相迎合。</p></div>
  </div>
  <div class="list-item">
    <div class="num">2</div>
    <div class="content"><h3>互相挑毛病</h3><p>明确要求 Agent 对其他角色的结论提出质疑，找出证据不足和逻辑漏洞。</p></div>
  </div>
  <div class="list-item">
    <div class="num">3</div>
    <div class="content"><h3>人做整合</h3><p>最后由产品经理综合判断，给出需求优先级与下一步验证计划。</p></div>
  </div>
</div>
<div class="body-text" style="margin-top:40px">关键是<strong>让 AI 先吵清楚</strong>，而不是指望一次 Prompt 就得到完美答案。</div>"""},

    # 14
    {"num": 14, "title": "四个 Agent 的角色定义与 Prompt 设计", "section": "场景一：多 Agent 需求分析", "kicker": "Roles",
     "subtitle": "给角色、给目标、给约束、给输出格式",
     "theme": "default",
     "content": """<div class="table-wrap">
  <table>
    <tr>
      <th style="width:15%">Agent</th>
      <th style="width:20%">角色</th>
      <th style="width:65%">核心问题</th>
    </tr>
    <tr>
      <td><span class="badge blue">用户</span></td>
      <td>用户研究员</td>
      <td>谁需要？什么场景？真痛点还是伪需求？是否愿意付费？</td>
    </tr>
    <tr>
      <td><span class="badge green">技术</span></td>
      <td>硬件工程师</td>
      <td>实现成本？对主功能影响？散热、寿命、可靠性？</td>
    </tr>
    <tr>
      <td><span class="badge orange">商业</span></td>
      <td>商业分析师</td>
      <td>定价？毛利？渠道接受度？能否支撑溢价？</td>
    </tr>
    <tr>
      <td><span class="badge red">竞品</span></td>
      <td>竞品分析师</td>
      <td>竞品怎么做？为什么没做？差异化是否成立？</td>
    </tr>
  </table>
</div>
<div class="body-text" style="margin-top:30px">Prompt 设计原则：给角色、给目标、给约束、给输出格式；要求引用证据、标注不确定项；明确要求对其他角色结论提出质疑。</div>"""},

    # 15
    {"num": 15, "title": "实战输出：为什么氛围灯不是刚需？", "section": "场景一：多 Agent 需求分析", "kicker": "Conclusion",
     "subtitle": "四视角交叉校验后的综合判断",
     "theme": "default",
     "content": """<div class="table-wrap">
  <table>
    <tr><th style="width:15%">视角</th><th>关键结论</th></tr>
    <tr><td><span class="badge blue">用户</span></td><td>植物灯核心用户购买决策因素是光照效果、能耗、噪音；氛围灯是"加分项"但不是购买理由。</td></tr>
    <tr><td><span class="badge green">技术</span></td><td>增加 RGB 模块会提升成本、增加散热压力、可能缩短主灯寿命。</td></tr>
    <tr><td><span class="badge orange">商业</span></td><td>加价 15-20% 后，目标用户对价格敏感，氛围灯难以支撑溢价。</td></tr>
    <tr><td><span class="badge red">竞品</span></td><td>主流竞品（Aerogarden、Gardyn、Click &amp; Grow）均未把氛围灯作为核心卖点。</td></tr>
  </table>
</div>
<div class="quote-big" style="margin-top:36px; border-color:var(--accent-warm)">综合判断：氛围灯是"有很好，没有也行"的增值功能，不应作为核心差异化卖点投入大量资源。</div>"""},

    # 16
    {"num": 16, "title": "从分析到 PRD：可带走的需求分析模板", "section": "场景一：多 Agent 需求分析", "kicker": "Template",
     "subtitle": "把本次分析的结构固化为可复用模板",
     "theme": "default",
     "content": """<div class="list-stack">
  <div class="list-item"><div class="num">1</div><div class="content"><h3>产品目标与约束</h3><p>明确要解决的问题、预算、时间、技术边界。</p></div></div>
  <div class="list-item"><div class="num">2</div><div class="content"><h3>多视角分析</h3><p>用户 / 技术 / 商业 / 竞品四个视角分别输出。</p></div></div>
  <div class="list-item"><div class="num">3</div><div class="content"><h3>交叉校验记录</h3><p>矛盾点、漏洞、遗漏，以及补充视角。</p></div></div>
  <div class="list-item"><div class="num">4</div><div class="content"><h3>关键争议点</h3><p>团队分歧最大、最需要进一步验证的问题。</p></div></div>
  <div class="list-item"><div class="num">5</div><div class="content"><h3>需求优先级建议</h3><p>MVP / 后续迭代 / 不做的明确结论。</p></div></div>
  <div class="list-item"><div class="num">6</div><div class="content"><h3>不确定项与下一步验证计划</h3><p>每个不确定项都要有具体验证方法。</p></div></div>
</div>"""},

    # 17
    {"num": 17, "title": "硬件 PM 为什么要抓 Reddit", "section": "场景二：Reddit 情报抓取", "kicker": "Scenario 2",
     "subtitle": "用户在 Reddit 直接表达真实想法",
     "theme": "default",
     "content": """<div class="two-col" style="margin-top:20px">
  <div class="card accent">
    <h3>Reddit 的价值</h3>
    <ul>
      <li>海外用户画像、痛点、使用场景的一手信息。</li>
      <li>竞品反馈、价格敏感度、功能期待的真实表达。</li>
      <li>传统做法：人工逛论坛，2-3 天出一份报告。</li>
    </ul>
  </div>
  <div>
    <div class="quote-big">"用户不会在调研问卷里说的东西，常常会在 Reddit 里吐槽。"</div>
  </div>
</div>"""},

    # 18
    {"num": 18, "title": "案例：植物灯 / 室内种植相关社区", "section": "场景二：Reddit 情报抓取", "kicker": "Targets",
     "subtitle": "目标社区与关键词定义",
     "theme": "default",
     "content": """<div class="two-col" style="margin-top:20px">
  <div class="card accent">
    <h3>目标社区</h3>
    <p>r/IndoorGarden · r/hydroponics · r/SpaceBuckets · r/Gardening</p>
    <p style="margin-top:16px">这些社区聚集了大量室内种植爱好者，讨论真实、具体、高频。</p>
  </div>
  <div class="card accent">
    <h3>关键词</h3>
    <p>grow light / LED / full spectrum / yield / heat / noise / energy / price</p>
    <p style="margin-top:16px">关键词定义直接决定抓取的信噪比。</p>
  </div>
</div>
<div class="body-text" style="margin-top:40px">先定义清楚"什么算相关"，比盲目扩大抓取范围更重要。</div>"""},

    # 19
    {"num": 19, "title": "Reddit 情报工作流拆解", "section": "场景二：Reddit 情报抓取", "kicker": "Workflow",
     "subtitle": "从关键词定义到定时更新的完整链路",
     "theme": "default",
     "content": """<div class="flow" style="flex-wrap:wrap; margin-top:30px">
  <div class="flow-node"><strong>1. 定义关键词</strong><span>明确抓取范围</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>2. API / 爬虫抓取</strong><span>pullpush.io / Reddit API</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>3. 清洗与筛选</strong><span>去广告、去 spam、相关度判断</span></div>
</div>
<div class="flow" style="margin-top:20px">
  <div class="flow-node"><strong>4. AI 分析</strong><span>主题分类、情感分析、痛点聚类</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>5. 人工验证</strong><span>抽样检查、关键 quote 复核</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>6. 输出结构化报告</strong><span>存档并设置定时更新</span></div>
</div>
<div class="body-text" style="margin-top:40px">人在第 5 步介入：审阅结论、复核关键 quote、做最终决策。</div>"""},

    # 20
    {"num": 20, "title": "输出样例：结构化洞察报告", "section": "场景二：Reddit 情报抓取", "kicker": "Output",
     "subtitle": "一份可直接提交给团队的报告结构",
     "theme": "default",
     "content": """<div class="card-grid" style="grid-template-columns:repeat(3,1fr)">
  <div class="card accent"><h3>1 · 数据来源</h3><p>来源、时间范围、样本量。</p></div>
  <div class="card accent"><h3>2 · 主题分布</h3><p>占比图与主要话题分类。</p></div>
  <div class="card accent"><h3>3 · 情感倾向</h3><p>正面 / 负面 / 中性占比。</p></div>
  <div class="card accent"><h3>4 · 高频痛点 Top 10</h3><p>按提及频次排序。</p></div>
  <div class="card accent"><h3>5 · 竞品提及</h3><p>竞品评价与对比信号。</p></div>
  <div class="card accent"><h3>6 · 机会点建议</h3><p>可落地的功能/定位机会。</p></div>
</div>
<div class="body-text" style="margin-top:30px">每份报告都应包含<strong>不确定项与待验证</strong>，避免把猜测包装成洞察。</div>"""},

    # 21
    {"num": 21, "title": "从人工到自动化：情报周报", "section": "场景二：Reddit 情报抓取", "kicker": "Automation",
     "subtitle": "把一次性调研变成持续运转的情报系统",
     "theme": "default",
     "content": """<div class="two-col" style="margin-top:20px">
  <div class="card accent">
    <h3>前后对比</h3>
    <p><strong>之前</strong>：2-3 天人工逛论坛，产出慢、难以持续。</p>
    <p style="margin-top:14px"><strong>之后</strong>：AI 自动 1 小时内完成抓取、清洗、分析。</p>
  </div>
  <div class="card accent">
    <h3>PM 只需要</h3>
    <ul>
      <li>审阅结论</li>
      <li>复核关键 quote</li>
      <li>做决策</li>
    </ul>
  </div>
</div>
<div class="quote-big" style="margin-top:40px">输出：每周一早上，飞书 / 邮件自动推送一份 Reddit 情报周报。</div>"""},

    # 22
    {"num": 22, "title": "为什么要封装成 Skill", "section": "场景三：自定义 Skill", "kicker": "Scenario 3",
     "subtitle": "从一次性 Prompt 到可复用工具",
     "theme": "default",
     "content": """<div class="card-grid">
  <div class="card accent"><h3>可复用</h3><p>一次写好，团队反复调用，不需要每次重写 Prompt。</p></div>
  <div class="card accent"><h3>格式一致</h3><p>输出结构固定，方便对比、归档、接入自动化。</p></div>
  <div class="card accent"><h3>可分享</h3><p>团队成员可以共享同一个 Skill，保持工作方式一致。</p></div>
  <div class="card accent"><h3>减少重复输入</h3><p>把上下文、约束、输出格式都封装进去，用户只给关键输入。</p></div>
</div>"""},

    # 23
    {"num": 23, "title": "Anthropic Skill 规范", "section": "场景三：自定义 Skill", "kicker": "Spec",
     "subtitle": "SKILL.md 是 Skill 的核心说明文档",
     "theme": "default",
     "content": """<div class="card accent" style="margin-top:20px; font-family:monospace; font-size:17px; line-height:1.6; white-space:pre">skill-name/
├── SKILL.md          # 核心说明文档
├── README.md         # 可选：使用说明
└── ...               # 可选：脚本、模板、示例</div>
<div class="card accent" style="margin-top:24px">
  <h3>SKILL.md 标准结构</h3>
  <ul>
    <li><strong>何时使用</strong>：描述使用场景和触发条件。</li>
    <li><strong>输入</strong>：用户需要提供什么信息。</li>
    <li><strong>工作流</strong>：分步骤说明执行流程。</li>
    <li><strong>输出格式</strong>：明确结构、字段、格式要求。</li>
    <li><strong>示例</strong>：给一个输入 / 输出样例。</li>
    <li><strong>注意事项</strong>：常见错误、边界条件、验证建议。</li>
  </ul>
</div>"""},

    # 24
    {"num": 24, "title": "Hermes Skill 机制", "section": "场景三：自定义 Skill", "kicker": "Hermes",
     "subtitle": "Hermes 如何落地 Anthropic 规范",
     "theme": "default",
     "content": """<div class="list-stack">
  <div class="list-item"><div class="num">1</div><div class="content"><h3>兼容 Anthropic Skill 规范</h3><p>SKILL.md 结构一致，迁移成本低。</p></div></div>
  <div class="list-item"><div class="num">2</div><div class="content"><h3>Skill 目录</h3><p>存放在 Hermes 的 skills 目录下，按名称调用。</p></div></div>
  <div class="list-item"><div class="num">3</div><div class="content"><h3>支持参数传递与上下文继承</h3><p>可以在对话中传递参数，继承上下文。</p></div></div>
  <div class="list-item"><div class="num">4</div><div class="content"><h3>扩展能力</h3><p>可绑定定时任务、接入消息渠道、调用 MCP 工具 / 浏览器自动化。</p></div></div>
</div>"""},

    # 25
    {"num": 25, "title": "演示：把植物灯需求分析封装成 Skill", "section": "场景三：自定义 Skill", "kicker": "Demo",
     "subtitle": "hardware-pm-requirement-analysis",
     "theme": "default",
     "content": """<div class="card accent" style="margin-top:20px">
  <h3>Skill 名称</h3>
  <p>hardware-pm-requirement-analysis</p>
</div>
<div class="card-grid" style="margin-top:24px">
  <div class="card accent"><h3>输入</h3><p>产品目标、目标用户、预算、约束。</p></div>
  <div class="card accent"><h3>工作流</h3><p>生成 4 个 Agent 的 Prompt → 并行输出 → 交叉质疑 → 输出结论。</p></div>
  <div class="card accent" style="grid-column:span 2"><h3>输出格式</h3><p>Markdown 报告：产品目标与约束、多视角分析、交叉校验记录、关键争议点、需求优先级建议、不确定项与验证计划。</p></div>
</div>"""},

    # 26
    {"num": 26, "title": "Skill 设计模板与带走清单", "section": "场景三：自定义 Skill", "kicker": "Checklist",
     "subtitle": "封装一个 Skill 前的六步检查",
     "theme": "default",
     "content": """<div class="list-stack">
  <div class="list-item"><div class="num">1</div><div class="content"><h3>定义触发场景</h3><p>这个 Skill 在什么情况下被调用？</p></div></div>
  <div class="list-item"><div class="num">2</div><div class="content"><h3>明确输入字段</h3><p>用户必须提供哪些信息？</p></div></div>
  <div class="list-item"><div class="num">3</div><div class="content"><h3>设计工作流步骤</h3><p>分几步执行，每步输出什么？</p></div></div>
  <div class="list-item"><div class="num">4</div><div class="content"><h3>规定输出格式</h3><p>结构、字段、示例。</p></div></div>
  <div class="list-item"><div class="num">5</div><div class="content"><h3>写一个示例</h3><p>输入和输出各一个。</p></div></div>
  <div class="list-item"><div class="num">6</div><div class="content"><h3>标注注意事项</h3><p>常见错误、边界条件、验证建议。</p></div></div>
</div>"""},

    # 27
    {"num": 27, "title": "定时任务：让 AI 在后台持续运转", "section": "场景四 & 五：定时任务 + 消息渠道", "kicker": "Scenario 4",
     "subtitle": "定时任务四要素",
     "theme": "default",
     "content": """<div class="card-grid" style="grid-template-columns:repeat(2,1fr)">
  <div class="card accent"><h3>1 · 触发条件</h3><p>每天 / 每周 / 每月 / 事件触发。</p></div>
  <div class="card accent"><h3>2 · 输入来源</h3><p>网页 / API / 本地文件 / 数据库。</p></div>
  <div class="card accent"><h3>3 · 输出格式</h3><p>Markdown / JSON / 飞书消息 / 邮件。</p></div>
  <div class="card accent"><h3>4 · 推送渠道</h3><p>邮件 / 飞书 / 钉钉 / Slack。</p></div>
</div>
<div class="body-text" style="margin-top:40px">四要素想清楚，一个定时任务才算真正设计完成。</div>"""},

    # 28
    {"num": 28, "title": "案例：每周自动 Reddit 情报报告", "section": "场景四 & 五：定时任务 + 消息渠道", "kicker": "Cron Job",
     "subtitle": "一个完整定时任务示例",
     "theme": "default",
     "content": """<div class="flow" style="margin-top:30px">
  <div class="flow-node"><strong>每周一 9:00</strong><span>定时触发</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>抓取过去 7 天</strong><span>相关帖子</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>AI 生成洞察报告</strong><span>主题 / 情感 / 痛点</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>推送到飞书群</strong><span>个人 + 群</span></div>
</div>
<div class="body-text" style="margin-top:50px">PM 周一早上打开飞书，看到的是已经整理好的情报摘要，而不是一堆未读链接。</div>"""},

    # 29
    {"num": 29, "title": "消息渠道打通：随时指挥 AI", "section": "场景四 & 五：定时任务 + 消息渠道", "kicker": "Messaging",
     "subtitle": "在飞书 / 钉钉 / 微信里用自然语言触发 Skill",
     "theme": "default",
     "content": """<div class="card-grid">
  <div class="card accent"><h3>多平台接入</h3><p>飞书 / 钉钉 / 微信 / WhatsApp / Telegram。</p></div>
  <div class="card accent"><h3>自然语言触发</h3><p>"帮我跑一下本周 Reddit 情报报告"。</p></div>
  <div class="card accent"><h3>接收结果</h3><p>AI 把报告直接发回对话。</p></div>
  <div class="card accent"><h3>继续追问</h3><p>"关于价格敏感度的具体 quote 有哪些？"</p></div>
</div>"""},

    # 30
    {"num": 30, "title": "一个完整的自动化闭环示例", "section": "场景四 & 五：定时任务 + 消息渠道", "kicker": "Loop",
     "subtitle": "从用户指令到追问，AI 全程在后台执行",
     "theme": "default",
     "content": """<div class="flow" style="flex-wrap:wrap; margin-top:30px">
  <div class="flow-node"><strong>用户指令</strong><span>在飞书里发送 "/reddit-report"</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>触发 Skill</strong><span>Hermes 调度任务</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>自动抓取</strong><span>Reddit 数据</span></div>
</div>
<div class="flow" style="margin-top:20px">
  <div class="flow-node"><strong>AI 分析</strong><span>生成报告</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>推送报告</strong><span>飞书消息</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node"><strong>用户追问</strong><span>继续对话</span></div>
</div>
<div class="body-text" style="margin-top:40px">人始终只需要做两件事：发起指令和做最终决策。</div>"""},

    # 31
    {"num": 31, "title": "实战任务一：多 Agent 分析真实小需求", "section": "现场实战", "kicker": "Practice 1",
     "subtitle": "5 分钟完成一次多 Agent 分析",
     "theme": "default",
     "content": """<div class="list-stack">
  <div class="list-item"><div class="num">1</div><div class="content"><h3>给学员一个简单硬件产品想法</h3><p>例如：智能花盆 / 桌面空气净化器 / 便携咖啡机。</p></div></div>
  <div class="list-item"><div class="num">2</div><div class="content"><h3>分组：用户 / 技术 / 商业 / 竞品</h3><p>每个组代表一个 Agent 视角。</p></div></div>
  <div class="list-item"><div class="num">3</div><div class="content"><h3>用 5 分钟完成一次多 Agent 分析</h3><p>分别输出观点，然后互相质疑。</p></div></div>
  <div class="list-item"><div class="num">4</div><div class="content"><h3>输出</h3><p>一个带争议点的需求判断。</p></div></div>
</div>"""},

    # 32
    {"num": 32, "title": "实战任务二：封装一个自己的 Skill", "section": "现场实战", "kicker": "Practice 2",
     "subtitle": "把每周重复做的工作变成可复用工具",
     "theme": "default",
     "content": """<div class="two-col" style="margin-top:20px">
  <div class="card accent">
    <h3>任务</h3>
    <p>学员选择一个自己每周重复做的工作。</p>
    <p style="margin-top:14px">用 Anthropic Skill 规范写出 <code>SKILL.md</code> 框架。</p>
    <p style="margin-top:14px">带走并在本周内完善。</p>
  </div>
  <div class="card accent">
    <h3>推荐起点</h3>
    <ul>
      <li>竞品周报</li>
      <li>用户反馈整理</li>
      <li>PRD 结构模板</li>
      <li>价格监控</li>
    </ul>
  </div>
</div>
<div class="quote-big" style="margin-top:40px">先完成，再完美。Skill 的第一版不需要覆盖所有边界，先把主流程跑通。</div>"""},

    # 33
    {"num": 33, "title": "最佳实践清单：7 条原则", "section": "收尾与行动", "kicker": "Principles",
     "subtitle": "让 AI 真正成为生产力工具",
     "theme": "default",
     "content": """<div class="list-stack">
  <div class="list-item"><div class="num">1</div><div class="content"><h3>从具体任务开始</h3><p>不要问"你能帮我做什么"，而是说"帮我分析这个需求"。</p></div></div>
  <div class="list-item"><div class="num">2</div><div class="content"><h3>把 Prompt 当作给同事的 brief</h3><p>给角色、给目标、给约束、给输出格式。</p></div></div>
  <div class="list-item"><div class="num">3</div><div class="content"><h3>封装重复流程为 Skill</h3><p>一次写好，反复调用。</p></div></div>
  <div class="list-item"><div class="num">4</div><div class="content"><h3>让重复任务定时跑</h3><p>周报、监控、情报，交给 cron。</p></div></div>
  <div class="list-item"><div class="num">5</div><div class="content"><h3>保持人在回路</h3><p>AI 提供输入，人做最终判断。</p></div></div>
  <div class="list-item"><div class="num">6</div><div class="content"><h3>验证输出质量</h3><p>关键结论必须复核证据。</p></div></div>
  <div class="list-item"><div class="num">7</div><div class="content"><h3>持续迭代优化</h3><p>Skill 和 Prompt 都是版本产物。</p></div></div>
</div>"""},

    # 34
    {"num": 34, "title": "本周可开始的 3 件事", "section": "收尾与行动", "kicker": "Action",
     "subtitle": "从听完到动手，最小可行路径",
     "theme": "default",
     "content": """<div class="list-stack">
  <div class="list-item">
    <div class="num">1</div>
    <div class="content"><h3>跑一次多 Agent 需求分析</h3><p>选一个真实 PRD 前的需求，用模板跑四个视角。</p></div>
  </div>
  <div class="list-item">
    <div class="num">2</div>
    <div class="content"><h3>封装一个 Skill</h3><p>把一个重复工作写成 <code>SKILL.md</code> 框架，先跑通主流程。</p></div>
  </div>
  <div class="list-item">
    <div class="num">3</div>
    <div class="content"><h3>建立"AI 输出必须人工验证"的习惯</h3><p>每个关键结论都标注事实 / 推测 / 待验证。</p></div>
  </div>
</div>
<div class="body-text" style="margin-top:40px">不需要三件都做。先选一件，本周内完成，就赢了。</div>"""},

    # 35
    {"num": 35, "title": "资源推荐 + Q&A", "section": "收尾与行动", "kicker": "Resources",
     "subtitle": "推荐工具与资源，开放问答",
     "theme": "default",
     "content": """<div class="two-col" style="margin-top:20px">
  <div class="card accent">
    <h3>推荐工具</h3>
    <ul>
      <li>Hermes · 桌面端 AI 工作平台</li>
      <li>Claude · 长上下文与推理</li>
      <li>Cursor · AI 代码与原型</li>
      <li>GitHub · Skill 与模板版本管理</li>
    </ul>
  </div>
  <div class="card accent">
    <h3>推荐资源</h3>
    <ul>
      <li>Anthropic Skill 规范</li>
      <li>agentskills.io</li>
      <li>Hermes 官方文档</li>
    </ul>
  </div>
</div>
<div class="quote-big" style="margin-top:40px; text-align:center; border:none; padding-left:0">谢谢 · Q&A</div>"""}
]

manifest = []
for s in slides:
    file_name = f"{s['num']:02d}-{s['title'][:16].replace(' ', '-').replace('·', '').replace('：', '-').replace('/', '-')}.html"
    file_name = re.sub(r'-+', '-', file_name).lower()
    path = os.path.join(slides_dir, file_name)
    
    if s['num'] == 1:
        # Already created
        manifest.append({"file": f"slides/01-cover.html", "label": "封面"})
        continue
    
    html_content = page_html(
        s['num'], s['title'], s['section'], "default",
        s['content'], kicker=s.get('kicker'), subtitle=s.get('subtitle'), theme=s.get('theme', 'default')
    )
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    manifest.append({"file": f"slides/{file_name}", "label": s['title']})

# Update index.html MANIFEST
with open(os.path.join(base, "index.html"), 'r', encoding='utf-8') as f:
    index_html = f.read()

manifest_str = ",\n    ".join([f'{{ file: "{m["file"]}", label: "{m["label"]}" }}' for m in manifest])
new_manifest = f"window.DECK_MANIFEST = [\n    {manifest_str}\n  ];"
index_html = re.sub(r'window\.DECK_MANIFEST\s*=\s*\[[^\]]*\];', new_manifest, index_html, flags=re.DOTALL)
with open(os.path.join(base, "index.html"), 'w', encoding='utf-8') as f:
    f.write(index_html)

print(f"Generated {len(slides)} slides in {slides_dir}")
print(f"Manifest: {len(manifest)} items")
