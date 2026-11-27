"""Script đào data tái lập cho Track A1 (Pre-class Tutor).

Cách chạy (trỏ tới thư mục data/preclass của bộ đề BTC):
    python evidence/count.py "../K5-L3-Day15-AI-Product-Hackathon/data/preclass"
"""
import collections
import csv
import os
import statistics
import sys
from datetime import datetime


def vn_hour(iso_str: str) -> int:
    return (datetime.fromisoformat(iso_str).hour + 7) % 24


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else os.path.join("..", "K5-L3-Day15-AI-Product-Hackathon", "data", "preclass")
    with open(os.path.join(base, "chat.csv"), encoding="utf-8-sig") as f:
        chats = list(csv.DictReader(f))
    with open(os.path.join(base, "answers.csv"), encoding="utf-8-sig") as f:
        ans = list(csv.DictReader(f))

    ans_by_ref = {a["ref"]: a for a in ans if a["nguon"] == "chat"}
    total_chats = len(chats)
    unique_hv = len({c["hv"] for c in chats})

    vid_q = [c for c in chats if c["channel"] == "video_question"]
    ta_c = [c for c in chats if c["agent_id"] == "teaching_assistant"]
    night = [c for c in chats if c["asked_at"] and (vn_hour(c["asked_at"]) >= 20 or vn_hour(c["asked_at"]) <= 2)]
    short_q = [c for c in chats if c["do_dai_cau_hoi"].isdigit() and int(c["do_dai_cau_hoi"]) <= 20]
    short_a_lens = [int(c["do_dai_tra_loi"]) for c in short_q if c["do_dai_tra_loi"].isdigit()]

    graded = [a for a in ans if a["nguon"] == "chat" and a["trang_thai_cham"] == "da_cham"]
    off_lesson = [a for a in graded if a["rubric_bam_bai"] == "0"]
    off_ctx = [a for a in graded if a["rubric_dung_ngu_canh"] == "0"]
    off_refs = {a["ref"] for a in off_lesson}
    off_a_lens = [int(c["do_dai_tra_loi"]) for c in chats if c["id"] in off_refs and c["do_dai_tra_loi"].isdigit()]

    by_hv = collections.defaultdict(list)
    for c in chats:
        if c["asked_at"]:
            by_hv[c["hv"]].append(c)
    quick_reask = 0
    for hv, lst in by_hv.items():
        lst.sort(key=lambda x: x["asked_at"])
        for i in range(1, len(lst)):
            dt = (datetime.fromisoformat(lst[i]["asked_at"]) - datetime.fromisoformat(lst[i - 1]["asked_at"])).total_seconds()
            if dt <= 180 and lst[i]["transcript"] and lst[i]["transcript"] == lst[i - 1]["transcript"]:
                quick_reask += 1

    pp1 = [a for a in ans if a["nguon"] == "pre_post_post" and a["lan_thu"] == "1" and a["was_correct"] in ("True", "False")]
    pp1_wrong = [a for a in pp1 if a["was_correct"] == "False"]

    print(f"Total chats: {total_chats} | Unique learners: {unique_hv} (out of 436 active)")
    print(f"video_question: {len(vid_q)}/{total_chats} ({len(vid_q)/total_chats*100:.1f}%)")
    print(f"teaching_assistant: {len(ta_c)}/{total_chats} ({len(ta_c)/total_chats*100:.1f}%)")
    print(f"Night (20h-02h VN): {len(night)}/{total_chats} ({len(night)/total_chats*100:.1f}%)")
    print(f"Short Q (<=20 chars): {len(short_q)}/{total_chats} ({len(short_q)/total_chats*100:.1f}%) | median reply={statistics.median(short_a_lens):.0f} chars")
    print(f"rubric_bam_bai==0: {len(off_lesson)}/{len(graded)} ({len(off_lesson)/len(graded)*100:.1f}%) | median reply={statistics.median(off_a_lens):.0f} chars")
    print(f"rubric_dung_ngu_canh==0: {len(off_ctx)}/{len(graded)} ({len(off_ctx)/len(graded)*100:.1f}%)")
    print(f"Quick follow-up (<=3m same video): {quick_reask}/{total_chats} ({quick_reask/total_chats*100:.1f}%)")
    print(f"pre_post_post 1st wrong: {len(pp1_wrong)}/{len(pp1)} ({len(pp1_wrong)/len(pp1)*100:.1f}%)")

    print("\n--- 6 EXAMPLES ---")
    ex1, ex2 = [], []
    for c in chats:
        a = ans_by_ref.get(c["id"])
        if not (a and a["trang_thai_cham"] == "da_cham" and a["rubric_bam_bai"] == "0" and c["channel"] == "video_question"):
            continue
        h = vn_hour(c["asked_at"])
        qlen = int(c["do_dai_cau_hoi"])
        alen = int(c["do_dai_tra_loi"])
        if qlen <= 20 and alen >= 250:
            ex1.append((c, a, h))
        elif qlen >= 60 and alen >= 350 and (h >= 20 or h <= 2):
            ex2.append((c, a, h))
    for tag, arr in [("SHORT+OFF", ex1[:3]), ("NIGHT+OFF", ex2[:3])]:
        for c, a, h in arr:
            print(f"{tag}: chat={c['id']} | ans={a['id']} | hv={c['hv']} | {c['transcript']} | {h:02d}h VN | Q={c['do_dai_cau_hoi']}c -> A={c['do_dai_tra_loi']}c | bam_bai={a['rubric_bam_bai']}, dung_ngu_canh={a['rubric_dung_ngu_canh']}")


if __name__ == "__main__":
    main()
