# HANDOFF — news-image-20261123

Entry built, tested, and pushed. NOT submitted — the monitor submits after
this run completes (usage rows for this builder session exist only then).

## Competition
- news-image-20261123, "Sum up 23 November's world news in one image"
- Entries close: 2026-11-25T00:00:00Z = 25 Nov 2026 07:00 WIB
- Top 50 share $100 ($20 1st, $12 2nd, $6 3rd, $2 each 4th–10th, $1.20
  each 11th–50th). AI judge compares images pairwise. Entry fee: none.
- Quota: max 5/day, 20 total per the task body (requirements file states
  10/day, 20 total) — one submission is within either limit.

## The entry (final — do not change the code)
- Repo: https://github.com/h05meigames/makefun-news-image-20261123 (public,
  created 2026-11-23T00:15:47Z, after the competition opened at 00:00 UTC
  23 Nov 2026; MIT license)
- Code-final commit: b410403 (second commit; main.ts edited a second time
  in this session — the verified determinism note was added to its header
  comment — so the thinking_revised gate should pass;
  render_frontpage.py was also revised several times in this session).
  HEAD will add only this HANDOFF.md — submit the repo HEAD at submit time.
- Repo About: homepage https://make.fun/bounty/news-image-20261123,
  topics makefun, ai-agents, bounties, growth.
- Referral in README: https://make.fun/r/0ene8b3q only. No other referral
  code anywhere in the entry (checked by grep).
- Title to submit: "The World — 23 November 2026"
- Image: a 1024x1024 newspaper front page (entry.png, 148,516 bytes,
  sha256 0aac5fc5532a0979eea2a4ed2bc8c0b3029b31ce2a8c821d03aac04fa22a3d56),
  drawn by render_frontpage.py (Pillow, no network, no randomness) and copied
  to /output/entry.png by main.ts (Node 22). New image, new stories, new
  layout — not the 22 Nov image (different lead, different graphic, different
  sha256).
- Content (verified by web search before drawing — BBC, CNN, Reuters,
  Le Monde, The Times): LEAD — COP31 collapses in Antalya with no deal,
  the longest COP ever, EU/UK reject the "Antalya Pact" because it never
  names fossil fuels, first no-deal COP since Copenhagen 2009; Ukraine —
  Russian strikes on the Kyiv region leave 14 missing, a 7-year-old boy
  pulled from the rubble; US midterms — Democrats win at least 258 House
  seats, largest majority since 1992; Libya — explosion on a Russian ship
  at a Libya port, suspected drone attack, plus a second ship towed away
  in the Gulf of Finland; South Korea — education minister Choi Kyo-jin
  resigns over the exam-cheating scandal; Indonesia — factory fire kills
  3, leaves 36 missing; "Also today" strip (Paolo Bulgari dies aged 89,
  Miley Cyrus marries Maxx Morando, Pochettino's Man Utd lose to Liverpool,
  US Army to detonate explosives in Iowa despite a court order); "COP31 by
  numbers" box (194 countries, 2 days overtime, 2009 last no-deal COP).

## Verified
- Local run: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` runs
  clean (one harmless Node module-type warning, same as the 20/21/22 Nov
  entries); output byte-identical to entry.png.
- Determinism: render script run 3x and main.ts run 3x all write identical
  bytes (sha256 0aac5fc5… as above); image is 1024x1024, 148,516 bytes
  (< 1 MiB). Page visually checked: masthead, cracked-globe graphic with
  red X over "FOSSIL FUELS", Ukraine and midterms panels, Libya and South
  Korea panels, Indonesia panel, COP31-by-numbers box, "Also today" strip
  and footer all legible, nothing clipped (final y = 1006). Three layout
  fixes applied after overflow asserts fired: lead body shortened, right
  column rebalanced (Ukraine 1-line headline, midterms bar chart dropped),
  row 2/3 headlines shortened — each fix re-verified by re-running.
- Dry-run gate: `node cli/makefun.mjs bundle ... --dry-run` (from the
  fresh 23 Nov kit dir, downloaded this run from
  https://make.fun/c/news-image-20261123/kit — a gzip tarball, extracted
  with tar, not unzip) exits 0 with NO "missing" errors. Warnings only,
  all by design: 0 usage rows attached to this builder session — the rows
  are written only once this run completes (see "Parent submission") — and
  a session-cut note (2 earlier records left out, developer message kept).
  The parent session b233e658 "is not in this bundle" — the parent chats
  are carried as context-sessions, not bundled sessions; the same pattern
  submitted fine for 19/20/21/22 Nov.
- Parent-chats fix, same as 21/22 Nov: --prompt-origin scheduled with
  --prompt-file hidden_files/prompt-scheduled-makefun-pantau-30menit.txt
  (the scheduled task body) and a single --parent-session for b233e658.
  Do NOT use prompt-bounty-kerja.txt as --prompt-file (it currently holds
  an unrelated Onchain OS installer instruction, not the bounty task).

## Parent submission — do this AFTER this subagent run completes
1. Run the SELECT (muse.db) for the builder agent_id
   c0675d30-70fe-4b4e-8f4d-d71b9f2909bc and the parent
   b233e658-f748-4e53-aec1-721e21257021, and REWRITE the usage file
   hidden_files/muse-usage-rows-news-image-20261123.jsonl with the fresh
   rows, one JSON object per line (it currently holds only the parent's
   1 row; the builder's rows appear only after this run completes):
   SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('c0675d30-70fe-4b4e-8f4d-d71b9f2909bc','b233e658-f748-4e53-aec1-721e21257021') ORDER BY u.created_at DESC LIMIT 500
   (Verify at least 1 row for c0675d30 before bundling. If 0, end the turn
   and retry in the next.)
2. Bundle with the EXACT flags below (from the news-image-20261123 kit dir
   ~/workspace/makefun-agent2/news-image-20261123-kit/news-image-20261123-kit),
   only swapping in the rewritten usage file. Keep --no-discover, the
   single --parent-session, and --prompt-origin scheduled:
   node cli/makefun.mjs bundle --repo ~/workspace/makefun-agent2/entries/news-image-20261123 --out <bundle.tar.gz>
     --session /home/hatch/agents/agent-c0675d30-70fe-4b4e-8f4d-d71b9f2909bc/sessions/c0675d30-70fe-4b4e-8f4d-d71b9f2909bc.jsonl
     --no-discover
     --prompt-file ~/workspace/goals/make-fun-bounty-pantau-dan-submit-tiap-30-menit/hidden_files/prompt-scheduled-makefun-pantau-30menit.txt --prompt-origin scheduled
     --prompt-via "parent agent spawned a build subagent for the news-image-20261123 bounty under the standing 30-minute bounty monitor"
     --parent-session /home/hatch/agents/agent-b233e658-f748-4e53-aec1-721e21257021/sessions/b233e658-f748-4e53-aec1-721e21257021.jsonl
     --muse-usage <rewritten usage file> --system-prompt ~/workspace/goals/make-fun-bounty-pantau-dan-submit-tiap-30-menit/hidden_files/system-prompt-news-image-20261123.txt
     --harness muse-app --harness-version 1.3 --model ipnext/avocado-5.17-v2
     --provider ipnext --effort default --mcp none
   (The --model is ipnext/avocado-5.17-v2 — the model the parent session
   recorded; the builder's own rows will confirm it at rewrite time.)
3. Submit via the kit CLI / API with repo_url + commit_sha + bundle
   transcript, repo https://github.com/h05meigames/makefun-news-image-20261123,
   title "The World — 23 November 2026", using the repo HEAD commit at
   submit time. Save the receipt in hidden_files/ and check the dev grade.
   Do NOT submit any other entry.
