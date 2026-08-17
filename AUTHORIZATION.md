# Automated Publishing Authorization

This file is the single durable switch that controls whether the **`daily-literature-post`**
skill publishes its daily literature-connection post to WordPress **live** (immediately
visible) or as a **draft**. The skill reads this file at run time and publishes live only
when the authorization marker is present exactly.

**Current state: PAUSED (draft-only).** The marker line below ends in `PAUSED`, so the
skill currently falls back to publishing **drafts**. Live publishing has been approved
(see sign-off below) but is intentionally held off until a human flips the marker. **To
activate live publishing:** on the marker line below, replace the trailing word `PAUSED`
with the word `AUTHORIZED` (so the line reads `AUTOMATED PUBLISHING:` followed by
`AUTHORIZED`), then commit.

## Authorization marker

> AUTOMATED PUBLISHING: AUTHORIZED

The skill searches this file for the authorized marker — the line `AUTOMATED PUBLISHING:`
ending in the word `AUTHORIZED`. If that exact line is present anywhere in the file, the
daily post is published **live**. If this file is missing, unreadable, or the marker ends
in anything else (as it does now — `PAUSED`), the skill automatically falls back to
publishing a **draft** — no live post goes out. Do not change the wording of the marker
unless you intend to switch live publishing on or off.

**Important:** while paused, the fully-spelled authorized marker phrase must not appear
*anywhere* in this file — not even in these instructions — because the skill matches it as
a plain substring. That is why this document spells the trailing word as a separate token
(`AUTHORIZED`) rather than writing the whole marker out. The marker line is the single
place its wording decides behavior; edit only that line to switch live publishing on or
off, and never paste the complete authorized phrase into the surrounding prose.

## What is authorized

- **Scope:** live (immediate) publishing of the automated daily post produced by the
  `daily-literature-post` skill, tagged with the `auto-literature-connections` category.
- **Not authorized by this file:** any other skill or script. The weekly / full lab
  digest pipeline (`full-lab-digest`, `weekly-lab-digest`, `wordpress-publisher`) is
  unaffected and continues to publish as it did before. `scripts/publish_digest.py`
  still defaults to `--status draft` for every caller; live publishing requires an
  explicit `--status publish`, which only the `daily-literature-post` skill passes, and
  only when this file authorizes it.

## Who approved it and when

_Fill in the actual names and date before relying on this authorization._

- **Approved by (lab member):** `Cas Daniel (ckdan19@uw.edu)`  (e.g., ckdan19@uw.edu)
- **Signed off by (PI / professor):** `Steven Roberts`
- **Date of sign-off:** `2026-08-13`
- **Reason:** Approval so the daily literature pipeline can keep running through the future and can be used to the lab's benefit.

## Safety rails

Live publishing is deliberately hard to trigger by accident. Two independent rails,
both enforced by the `daily-literature-post` skill, protect it:

1. **Draft fallback (this file).** Live publishing happens **only** while this file
   exists and contains the exact authorization marker (the quoted line in the
   "Authorization marker" section above). If the file is deleted, renamed, made
   unreadable, or the marker is edited/removed, the skill reverts to publishing a
   **draft** and says so in its report. There is no other path to live publishing.
2. **One post per day.** The skill publishes at most **one** post per calendar day
   (live or draft). It records each publish in `digests/.literature-state.json` under
   `publish_log`. If an entry already exists for today, the skill refuses to publish
   again and reports why, so a double-trigger cannot produce duplicate posts.

If either rail is unclear or the state file looks wrong, the safe action is always to
remove this file — the skill will fall back to drafts, which are private until a human
reviews and publishes them.

## How to pause or disable this (for a future lab member)

### Pause live publishing (keep the automation running as drafts)

Do **either** of these — both immediately revert the skill to draft-only on its next run,
with no code changes:

- **Delete this file:** `git rm AUTHORIZATION.md` (or just remove/rename it), or
- **Neutralize the marker:** edit the marker line in the "Authorization marker" section
  so it no longer reads exactly as the authorized phrase (for example, change the word
  `AUTHORIZED` to `PAUSED`).

The daily post keeps being generated, but as a private draft for a human to review.
Commit the change so it persists for everyone.

### Fully disable the automation (stop it running at all)

The skill only runs unattended if a cron job invokes it. To stop that, edit the crontab:

1. Open the crontab for editing:

   ```
   crontab -e
   ```

2. Find the line that runs the daily literature pipeline. It is the line that changes
   into this repo and calls `claude -p "..."` with `scripts/publish_digest.py` in its
   `--allowedTools`, e.g. a line beginning with:

   ```
   0 8 * * 1 cd /home/catda/LabNotebook-Summarizer && claude -p "Fetch the lab posts, ... publish the digest draft. ..."
   ```

   > Note (as of this file's writing): the only automation entry installed is the
   > **weekly** job shown above (`0 8 * * 1` = every Monday at 08:00). There is **no**
   > separate daily entry yet. If a dedicated `daily-literature-post` cron line is added
   > later, it will look similar — identify it by the `cd /home/catda/LabNotebook-Summarizer`
   > path and the `claude -p` invocation — and the same steps apply to it.

3. **To pause temporarily:** put a `#` at the very start of that line to comment it out.
   **To disable permanently:** delete the whole line.

4. Save and exit the editor (in `nano`: `Ctrl-O`, `Enter`, then `Ctrl-X`; in `vim`:
   `:wq`, `Enter`). `cron` reloads automatically.

5. Verify the change took effect:

   ```
   crontab -l
   ```

   Confirm the line is gone (or now starts with `#`). With no cron job, the skill only
   runs when a person triggers it by hand, and even then this file's draft/live rail and
   the one-post-per-day cap still apply.


