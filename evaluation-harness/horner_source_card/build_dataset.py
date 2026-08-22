#!/usr/bin/env python3
"""Build a 50-case source-card dataset from immutable public Horner Archive sources.

Design note — Calibration Lab / evidence-first portfolio:
Every source excerpt is downloaded from a pinned public commit. The case definitions
and their expected checks were manually selected from public archive wording; no
synthetic historical passages or fabricated outcomes are introduced.
"""

from __future__ import annotations

import json
import pathlib
import urllib.request


REPO = "daniel-lingar/horner-archive"
COMMIT = "1ce7f7062559b2e132d9690f6f91df8f4452784e"
ROOT = pathlib.Path(__file__).resolve().parent
DATASET = ROOT / "datasets" / "horner_source_cards_v1.jsonl"


def check(field: str, contains: str | None = None, equals: str | None = None) -> dict:
    payload: dict[str, str] = {"field": field}
    if contains is not None:
        payload["contains"] = contains
    if equals is not None:
        payload["equals"] = equals
    return payload


def case(
    case_id: str,
    path: str,
    anchor: str,
    status: str,
    checks: list[dict],
    label: str,
    forbidden: list[str] | None = None,
) -> dict:
    return {
        "id": case_id,
        "source_repository": REPO,
        "source_commit": COMMIT,
        "source_path": path,
        "anchor": anchor,
        "excerpt_radius_chars": 700,
        "gold": {
            "research_status": status,
            "checks": checks,
            "forbidden_verified_claims": forbidden or [],
            "human_review_note": label,
        },
    }


# The 50 configurations below are derived from real, public source passages at COMMIT.
# They deliberately cover direct facts, source-tier qualifiers, open questions, and
# evidence boundaries—not only easy extraction examples.
CASES = [
    # CMSR — OQ-12 / OQ-13 (12)
    case("HA-001", "sources/cmsr-oq12-oq13.md", "# CMSR Research — OQ-12 / OQ-13 (June 2026)", "not_stated", [check("source_title", contains="CMSR Research"), check("verified_claims", contains="OQ-12")], "Document title and research identifiers are explicit."),
    case("HA-002", "sources/cmsr-oq12-oq13.md", "**Archive version:** v20.6", "not_stated", [check("verified_claims", contains="v20.6")], "Archive version is explicit; no case status is stated in this line."),
    case("HA-003", "sources/cmsr-oq12-oq13.md", "**Collection:** NARA M317", "not_stated", [check("record_type", contains="Compiled Service Records"), check("verified_claims", contains="NARA M317")], "Collection and record type are explicit."),
    case("HA-004", "sources/cmsr-oq12-oq13.md", "## OQ-12 — William Gordon Acord — CLOSED", "closed", [check("people_named", contains="William Gordon Acord"), check("research_status", equals="closed")], "OQ-12 is explicitly closed."),
    case("HA-005", "sources/cmsr-oq12-oq13.md", "| Name | William Gordon Acord", "closed", [check("people_named", contains="William Gordon Acord"), check("verified_claims", contains="44903963"), check("verified_claims", contains="Private")], "Name, card number, and rank are in the finding table."),
    case("HA-006", "sources/cmsr-oq12-oq13.md", "| Unit | **Co. H, 10th Arkansas Militia (CSA)** |", "closed", [check("verified_claims", contains="10th Arkansas Militia"), check("verified_claims", contains="Co. H")], "Unit placement is explicit for OQ-12."),
    case("HA-007", "sources/cmsr-oq12-oq13.md", "**Resolves the 11th Arkansas Infantry question:**", "closed", [check("verified_claims", contains="not the 11th Arkansas Infantry"), check("verified_claims", contains="10th Arkansas Militia")], "The source explicitly resolves the unit question."),
    case("HA-008", "sources/cmsr-oq12-oq13.md", "### Union service note", "not_stated", [check("not_established", contains="Union CMSR"), check("not_established", contains="service")], "The source requires treating the tombstone as a family memorial claim, not proved service.", ["confirmed Union service"]),
    case("HA-009", "sources/cmsr-oq12-oq13.md", "## OQ-13 — Henry Stewart — PARTIAL CLOSE", "partial", [check("people_named", contains="Henry Stewart"), check("research_status", equals="partial")], "OQ-13 is explicitly partial, not closed."),
    case("HA-010", "sources/cmsr-oq12-oq13.md", "| Full name | Joseph Henry \"Henry\" Stewart |", "partial", [check("people_named", contains="Joseph Henry"), check("verified_claims", contains="December 1840"), check("verified_claims", contains="17 August 1930")], "Identity fields are explicit; unit remains unresolved elsewhere."),
    case("HA-011", "sources/cmsr-oq12-oq13.md", "### Confederate alignment — documented; unit — OPEN", "open", [check("research_status", equals="open"), check("not_established", contains="unit")], "The source distinguishes documented alignment from an open unit designation.", ["confirmed unit"]),
    case("HA-012", "sources/cmsr-oq12-oq13.md", "| OQ-12 | William Gordon Acord unit", "partial", [check("verified_claims", contains="OQ-12"), check("verified_claims", contains="OQ-13"), check("not_established", contains="pending M317")], "Status summary marks OQ-12 closed and OQ-13 partial."),

    # PPAN / parcel research (11)
    case("HA-013", "sources/oq-ppan-001.md", "# OQ-PPAN-001 — Modern Parcel / PPAN Identification", "not_stated", [check("source_title", contains="Modern Parcel"), check("record_type", contains="PPAN")], "The title names the modern-parcel research task."),
    case("HA-014", "sources/oq-ppan-001.md", "| **Status** | **Closed v20.13**", "closed", [check("research_status", equals="closed"), check("verified_claims", contains="primary gate confirmed")], "The metadata table explicitly marks the work closed."),
    case("HA-015", "sources/oq-ppan-001.md", "| **Source verification** | [ARCountyData — Johnson County]", "not_stated", [check("verified_claims", contains="ARCountyData"), check("place", contains="Johnson")], "Public verification source and county are explicit."),
    case("HA-016", "sources/oq-ppan-001.md", "Identify the modern Johnson County PPAN", "not_stated", [check("verified_claims", contains="modern Johnson County PPAN"), check("record_type", contains="parcel")], "The purpose explains the limited modern-parcel task."),
    case("HA-017", "sources/oq-ppan-001.md", "**Rule:** Use this description in formal clerk", "not_stated", [check("verified_claims", contains="Modern PPANs may not match"), check("not_established", contains="historic patent")], "The source warns against treating a modern PPAN as the historical controlling reference.", ["PPAN proves patent boundary"]),
    case("HA-018", "sources/oq-ppan-001.md", "| Tract size | 160 acres |", "not_stated", [check("verified_claims", contains="160 acres"), check("verified_claims", contains="Certificate 19B")], "Historic legal-anchor fields are explicit."),
    case("HA-019", "sources/oq-ppan-001.md", "| Spencer Horner homestead (attack site) |", "not_stated", [check("people_named", contains="Spencer Horner"), check("verified_claims", contains="35.6681")], "The source gives a site label and coordinates."),
    case("HA-020", "sources/oq-ppan-001.md", "| Moore Cemetery | 35.6666", "not_stated", [check("verified_claims", contains="Moore Cemetery"), check("verified_claims", contains="35.6666")], "The cemetery coordinate is explicit."),
    case("HA-021", "sources/oq-ppan-001.md", "| Locked gate / cable (Jimmie SSE — **primary**) |", "closed", [check("verified_claims", contains="001-03571-000"), check("verified_claims", contains="confirmed")], "The primary gate is explicitly confirmed."),
    case("HA-022", "sources/oq-ppan-001.md", "1. **ARCountyData:** Johnson County", "not_stated", [check("verified_claims", contains="Search Real Estate Records"), check("verified_claims", contains="T12N R24W")], "The passage is a lookup workflow, not a resolved ownership conclusion."),
    case("HA-023", "sources/oq-ppan-001.md", "| Horner Homestead | 35.6681, -93.4981", "not_stated", [check("verified_claims", contains="001-06308-000"), check("verified_claims", contains="182.66")], "The deliverable matrix provides the PPAN and acreage for this listed row."),

    # Audience-evidence matrix (11)
    case("HA-024", "sources/audience-evidence-matrix.md", "# Audience Evidence Matrix — Horner Civil War Archive", "not_stated", [check("source_title", contains="Audience Evidence Matrix"), check("verified_claims", contains="What you can say safely")], "The document purpose is explicitly an evidence-communication guide."),
    case("HA-025", "sources/audience-evidence-matrix.md", "**Legend:** ✅ Safe to state", "not_stated", [check("verified_claims", contains="Safe to state"), check("verified_claims", contains="Do not state as fact")], "The legend defines claim tiers."),
    case("HA-026", "sources/audience-evidence-matrix.md", "| Spencer Horner murdered **2 Aug 1864**", "not_stated", [check("people_named", contains="Spencer Horner"), check("date_or_year", contains="2 Aug 1864"), check("verified_claims", contains="Tombstone")], "The matrix identifies the date and source basis."),
    case("HA-027", "sources/audience-evidence-matrix.md", "| Attack at homestead / potato patch", "not_stated", [check("verified_claims", contains="Sturges"), check("verified_claims", contains="1942 transcript")], "The matrix requires oral-history qualification in some settings."),
    case("HA-028", "sources/audience-evidence-matrix.md", "| Patent 19B — 160 acres, T12N R24W, 1857", "not_stated", [check("verified_claims", contains="Patent 19B"), check("verified_claims", contains="160 acres"), check("date_or_year", contains="1857")], "Patent fields and source tier are explicit."),
    case("HA-029", "sources/audience-evidence-matrix.md", "| Permelia sold farm for horse and wagon", "open", [check("not_established", contains="Oral only"), check("not_established", contains="OQ-20")], "The matrix prohibits treating the oral tradition as confirmed until OQ-20.", ["confirmed sale"]),
    case("HA-030", "sources/audience-evidence-matrix.md", "| Gordon Acord — **10th AR Militia", "closed", [check("verified_claims", contains="10th AR Militia"), check("verified_claims", contains="OQ-12 closed")], "Gordon Acord’s unit conclusion is marked closed."),
    case("HA-031", "sources/audience-evidence-matrix.md", "| Henry Stewart — CSA unit", "open", [check("research_status", equals="open"), check("not_established", contains="Open")], "The matrix says the unit is open and must not be stated as fact.", ["confirmed CSA unit"]),
    case("HA-032", "sources/audience-evidence-matrix.md", "| \"17 of 20\" body count", "not_stated", [check("not_established", contains="1942 sole source"), check("not_established", contains="Do not")], "The matrix prevents presenting the body count as verified fact.", ["verified body count"]),
    case("HA-033", "sources/audience-evidence-matrix.md", "| GPS-verified sites |", "not_stated", [check("verified_claims", contains="GPS-verified sites"), check("verified_claims", contains="Field work June 2026")], "The institutional-claims table labels this statement safe for funders."),
    case("HA-034", "sources/audience-evidence-matrix.md", "- **Funders:** Lead with primary pillars", "not_stated", [check("verified_claims", contains="primary pillars"), check("verified_claims", contains="oral and open OQs")], "The final guidance requires explicit qualification of oral and open evidence."),

    # GLO field-notes research (9)
    case("HA-035", "sources/glo-field-notes-oq22.md", "# OQ-22 — GLO Field Notes T12N R24W — CLOSED", "closed", [check("research_status", equals="closed"), check("verified_claims", contains="T12N R24W")], "The source title and status are explicit."),
    case("HA-036", "sources/glo-field-notes-oq22.md", "**Patent:** 19B — Sections **19** and **22**", "closed", [check("verified_claims", contains="Patent"), check("verified_claims", contains="160 acres"), check("people_named", contains="Spencer Horner")], "Patent, sections, acreage, assignee, and year are explicit."),
    case("HA-037", "sources/glo-field-notes-oq22.md", "| Book **913A** / Bundle **BD0164**", "closed", [check("verified_claims", contains="Book 913A"), check("verified_claims", contains="24 pages")], "The retrieval table specifies the book, bundle, and page count."),
    case("HA-038", "sources/glo-field-notes-oq22.md", "1. **Terrain split:** Upland lines consistently", "closed", [check("verified_claims", contains="hilly"), check("verified_claims", contains="1st rate soil")], "Terrain descriptions are source findings, not broader conclusions."),
    case("HA-039", "sources/glo-field-notes-oq22.md", "2. **Mulberry corridor:**", "closed", [check("verified_claims", contains="Mulberry 110 links"), check("date_or_year", contains="1845")], "The field-note wording and date are explicit."),
    case("HA-040", "sources/glo-field-notes-oq22.md", "3. **Water / roads:** Multiple brooks", "closed", [check("verified_claims", contains="15–40 links"), check("verified_claims", contains="roads crossing")], "The source describes brooks and roads as landscape evidence."),
    case("HA-041", "sources/glo-field-notes-oq22.md", "4. **Pre-patent occupancy:** Surveyor entries name", "closed", [check("verified_claims", contains="G. Homers field"), check("not_established", contains="not title")], "The passage distinguishes occupation evidence from title.", ["title ownership"]),
    case("HA-042", "sources/glo-field-notes-oq22.md", "5. **Corners:** Standard 1844–1845", "closed", [check("verified_claims", contains="witness trees"), check("verified_claims", contains="Oak")], "Corner markers and witness-tree types are explicit."),
    case("HA-043", "sources/glo-field-notes-oq22.md", "LiDAR bluff/cave correlation remains interpretive", "closed", [check("not_established", contains="interpretive"), check("not_established", contains="do not name caves")], "The source explicitly retains the bluff/cave correlation as interpretive.", ["cave confirmed"]),

    # Estate/research-status notes (7)
    case("HA-044", "sources/estate-oq20-research.md", "# OQ-20 — Post-1864 Land Disposition", "open", [check("research_status", equals="open"), check("source_title", contains="Land Disposition")], "OQ-20 is explicitly open."),
    case("HA-045", "sources/estate-oq20-research.md", "**Status:** Open · Reframed v20.8 · June 2026", "open", [check("research_status", equals="open"), check("date_or_year", contains="June 2026")], "Status and version/date are explicit."),
    case("HA-046", "sources/estate-oq20-research.md", "Family oral history (1942 transcript) says Permelia Turner Horner", "open", [check("people_named", contains="Permelia Turner Horner"), check("not_established", contains="oral history")], "The horse-and-wagon proposition is an oral-history lead, not a verified transaction.", ["confirmed sale"]),
    case("HA-047", "sources/estate-oq20-research.md", "The following is **index-only** until retrieval.", "index_only", [check("research_status", equals="index_only"), check("not_established", contains="Physical")], "The estate information is index-only pending retrieval."),
    case("HA-048", "sources/estate-oq20-research.md", "### Spencer Horner Estate, 1865", "index_only", [check("people_named", contains="John Turner Horner"), check("verified_claims", contains="Administrator")], "The index table names the administrator for Spencer Horner Estate."),
    case("HA-049", "sources/estate-oq20-research.md", "### William R. Horner Estate, 1865", "index_only", [check("people_named", contains="Mary Ann Horner"), check("verified_claims", contains="widow")], "The index table names Mary Ann Horner as administrator/widow."),
    case("HA-050", "sources/estate-oq20-research.md", "## What success looks like", "open", [check("not_established", contains="buyer identity"), check("not_established", contains="corroboration")], "The table presents future success criteria, not already established findings.", ["buyer identified"]),
]


def fetch_source(path: str) -> str:
    url = f"https://raw.githubusercontent.com/{REPO}/{COMMIT}/{path}"
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8")


def make_excerpt(text: str, anchor: str, radius: int) -> str:
    position = text.casefold().find(anchor.casefold())
    if position < 0:
        raise ValueError(f"Anchor not found: {anchor!r}")
    start = max(0, position - radius)
    end = min(len(text), position + len(anchor) + radius)
    return text[start:end].strip()


def main() -> None:
    source_cache: dict[str, str] = {}
    output: list[dict] = []
    for definition in CASES:
        path = definition["source_path"]
        if path not in source_cache:
            source_cache[path] = fetch_source(path)
        record = dict(definition)
        record["source_url"] = f"https://github.com/{REPO}/blob/{COMMIT}/{path}"
        record["source_excerpt"] = make_excerpt(
            source_cache[path], record.pop("anchor"), record.pop("excerpt_radius_chars")
        )
        output.append(record)

    DATASET.parent.mkdir(parents=True, exist_ok=True)
    with DATASET.open("w", encoding="utf-8") as handle:
        for record in output:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"Wrote {len(output)} real source-card cases to {DATASET}")


if __name__ == "__main__":
    main()
