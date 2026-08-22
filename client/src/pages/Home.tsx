/**
 * Calibration Lab design reminder: present evidence as an inspectable folio—
 * left-rail navigation, editorial reading field, fine graphite rules, vermilion annotations.
 */
import {
  ArrowDownRight,
  ArrowUpRight,
  Brackets,
  CheckCheck,
  ClipboardCheck,
  FileText,
  FolderGit2,
  GitBranch,
  Menu,
  SearchCheck,
  ShieldCheck,
  Sparkles,
} from "lucide-react";

const competencies = [
  {
    code: "01",
    name: "Prompt logic & evaluation",
    detail: "Structural tagging, pseudo-JSON parameters, system-role framing, constraint enforcement, and edge-case stress tests.",
  },
  {
    code: "02",
    name: "Technical writing & SOPs",
    detail: "Markdown-first procedures, training frameworks, documentation systems, and clear operational handoffs.",
  },
  {
    code: "03",
    name: "Systems & environments",
    detail: "Linux/Ubuntu, Bash, Git, GitHub Pages, JSON log parsing, and flat-file repository architecture.",
  },
  {
    code: "04",
    name: "Operational diagnostics",
    detail: "Root-cause analysis, preventive cycles, compliance documentation, quality audits, and autonomous execution.",
  },
];

const curriculum = [
  ["01–15", "Frame the record", "Scope, sources, provenance, and unresolved questions."],
  ["16–30", "Extract evidence", "Normalized observations, evidence labels, and source boundaries."],
  ["31–45", "Test the narrative", "Conflicts, alternatives, uncertainty, and edge-case review."],
  ["46–60", "Document judgment", "Annotated synthesis, method notes, and audit-ready writing."],
  ["61–75", "Publish the trail", "Static portfolio structure, quality checks, and reviewer access."],
];

const schemaLines = [
  ["<system_role>", "evidence-focused evaluator", "</system_role>"],
  ["<inputs>", "rubric · response · context", "</inputs>"],
  ["<constraint>", "do not invent evidence", "</constraint>"],
  ["<output>", "PASS | FAIL | INSUFFICIENT", "</output>"],
];

const links = {
  profile: "https://github.com/daniel-lingar",
  portfolioHome: "https://daniel-lingar.github.io/technical-prompt-engineer-portfolio/",
  portfolioRepo: "https://github.com/daniel-lingar/technical-prompt-engineer-portfolio",
  application: "https://github.com/daniel-lingar/technical-prompt-engineer-portfolio/blob/main/APPLICATION_PROFILE.md",
  schemas: "https://github.com/daniel-lingar/technical-prompt-engineer-portfolio/blob/main/PROMPT_SCHEMAS.md",
  curriculum: "https://daniel-lingar.github.io/wrh-master-curriculum/curriculum/",
};

const isGitHubPagesBuild = import.meta.env.BASE_URL !== "/";

function RailMark() {
  return (
    <div className="relative grid h-12 w-12 place-items-center border border-[#202523] bg-[#d64e32] shadow-[4px_4px_0_#202523]" aria-hidden="true">
      {isGitHubPagesBuild ? <span className="font-mono text-2xl font-medium leading-none text-[#fffaf2]">⊙</span> : <img src="/manus-storage/calibration-aperture-logo_8b5fc95a.png" alt="" className="h-9 w-9 object-contain brightness-0 invert" />}
    </div>
  );
}

function SectionMarker({ index, label }: { index: string; label: string }) {
  return (
    <div className="mb-6 flex items-center gap-3 font-mono text-[10px] font-medium uppercase tracking-[0.16em] text-[#63706c]">
      <span className="grid h-6 min-w-6 place-items-center bg-[#d64e32] px-1 text-[10px] text-[#fffaf2]">{index}</span>
      <span>{label}</span>
      <span className="h-px flex-1 bg-[#202523]/15" />
    </div>
  );
}

export default function Home() {
  return (
    <div className="min-h-screen overflow-x-hidden">
      <a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-[100] focus:bg-[#202523] focus:px-4 focus:py-2 focus:font-sans focus:text-sm focus:text-[#fffaf2]">
        Skip to portfolio content
      </a>

      <header className="border-b border-[#202523]/15 bg-[#f5f0e6]/95 px-5 py-4 backdrop-blur lg:hidden">
        <div className="flex items-center justify-between gap-4">
          <a href="#top" className="flex items-center gap-3 font-display text-sm font-extrabold tracking-tight">
            <RailMark />
            <span>CALIBRATION<br />LAB</span>
          </a>
          <a href="#main-content" className="grid h-10 w-10 place-items-center border border-[#202523]/20 bg-[#fbf9f4]" aria-label="Open portfolio content">
            <Menu size={18} />
          </a>
        </div>
      </header>

      <div className="mx-auto grid max-w-[1680px] lg:grid-cols-[285px_minmax(0,1fr)]">
        <aside className="sticky top-0 hidden h-screen flex-col border-r border-[#202523]/15 bg-[#f5f0e6]/85 px-8 py-8 lg:flex">
          <a href="#top" className="group mb-16 flex items-center gap-4">
            <RailMark />
            <span className="font-display text-[13px] font-extrabold leading-[1.02] tracking-[-0.04em]">CALIBRATION<br />LAB</span>
          </a>

          <div className="space-y-1 font-mono text-[10px] uppercase tracking-[0.12em] text-[#63706c]">
            <p className="mb-5 text-[#202523]">Portfolio index</p>
            {[
              ["01", "Method", "#method"],
              ["02", "Schemas", "#schemas"],
              ["03", "Curriculum", "#curriculum"],
              ["04", "Systems work", "#systems"],
              ["05", "Application", "#application"],
            ].map(([number, label, href]) => (
              <a key={number} href={href} className="group flex items-center gap-3 py-2 transition-colors hover:text-[#d64e32] focus-visible:text-[#d64e32]">
                <span className="w-5 text-[#d64e32]">{number}</span>
                <span>{label}</span>
                <span className="h-px flex-1 origin-left scale-x-0 bg-[#d64e32] transition-transform duration-200 group-hover:scale-x-100" />
              </a>
            ))}
          </div>

          <div className="mt-auto border-t border-[#202523]/15 pt-5 font-mono text-[10px] uppercase leading-relaxed tracking-[0.1em] text-[#63706c]">
            <p className="mb-2 flex items-center gap-2 text-[#202523]"><span className="signal-dot h-2 w-2 rounded-full bg-[#d64e32]" /> Available for async review work</p>
            <p>Method-first portfolio</p>
            <p>Markdown / Git-ready</p>
          </div>
        </aside>

        <main id="main-content" className="min-w-0">
          <section id="top" className="relative isolate min-h-[730px] overflow-hidden border-b border-[#202523]/15 px-5 pb-12 pt-8 sm:px-8 sm:pt-10 md:px-12 lg:min-h-screen lg:px-16 lg:pt-14 xl:px-20">
            <div className="calibration-grid pointer-events-none absolute inset-y-0 right-0 z-[-2] w-[55%] opacity-55" />
            {!isGitHubPagesBuild && <div className="absolute inset-y-0 right-0 z-[-1] hidden w-[54%] overflow-hidden lg:block">
              <img src="/manus-storage/calibration-hero_7228e298.jpg" alt="Abstract calibration materials arranged on a research surface" className="h-full w-full object-cover mix-blend-multiply opacity-95" />
              <div className="absolute inset-0 bg-gradient-to-r from-[#f5f0e6] via-[#f5f0e6]/55 to-transparent" />
            </div>}
            <div className="absolute right-5 top-8 font-mono text-[10px] uppercase tracking-[0.16em] text-[#63706c] sm:right-8 lg:right-12">Field note / 2026</div>

            <div className="relative flex max-w-[790px] flex-col pt-20 sm:pt-28 lg:pt-[18vh]">
              <div className="animate-ledger-rise mb-6 flex items-center gap-3 font-mono text-[10px] uppercase tracking-[0.14em] text-[#63706c]">
                <span className="h-px w-9 bg-[#d64e32]" />
                <span>Technical Prompt Engineer</span>
              </div>
              <h1 className="animate-ledger-rise [animation-delay:80ms] font-display text-[clamp(3rem,6.1vw,6.9rem)] font-extrabold leading-[0.92] tracking-[-0.075em] text-[#202523]">
                Open the rubric<br />before the model.
              </h1>
              <p className="animate-ledger-rise [animation-delay:160ms] mt-8 max-w-[550px] font-body text-[1.25rem] leading-[1.42] text-[#44504c] sm:text-[1.45rem]">
                I design prompts, documentation, and evaluation pathways that make a judgment <em className="font-semibold text-[#202523]">reproducible</em>—for remote AI operations teams that value careful reasoning over noise.
              </p>
              <div className="animate-ledger-rise [animation-delay:240ms] mt-10 flex flex-wrap gap-3 font-display text-sm font-bold">
                <a href="#schemas" className="group flex items-center gap-2 border border-[#202523] bg-[#202523] px-5 py-3 text-[#fffaf2] transition-transform duration-200 hover:-translate-y-0.5 focus-visible:-translate-y-0.5 active:scale-[0.97]">
                  Inspect schemas <ArrowDownRight size={16} className="transition-transform duration-200 group-hover:translate-y-0.5 group-hover:translate-x-0.5" />
                </a>
                <a href={links.application} target="_blank" rel="noreferrer" className="group flex items-center gap-2 border border-[#202523]/25 bg-[#f5f0e6]/75 px-5 py-3 transition-colors hover:border-[#d64e32] hover:text-[#d64e32] focus-visible:border-[#d64e32] focus-visible:text-[#d64e32] active:scale-[0.97]">
                  Read application profile <FileText size={16} />
                </a>
              </div>
            </div>

            <div className="absolute bottom-0 left-5 right-5 flex border-t border-[#202523]/15 py-5 sm:left-8 sm:right-8 md:left-12 md:right-12 lg:left-16 lg:right-16 xl:left-20 xl:right-20">
              <p className="max-w-sm font-mono text-[10px] uppercase leading-relaxed tracking-[0.12em] text-[#63706c]">Prompt architecture · rubric evaluation · SOP systems · independent diagnostics</p>
              <p className="ml-auto hidden font-mono text-[10px] uppercase tracking-[0.12em] text-[#63706c] sm:block">Scroll to inspect / ↓</p>
            </div>
          </section>

          <section id="method" className="px-5 py-20 sm:px-8 md:px-12 lg:px-16 lg:py-28 xl:px-20">
            <SectionMarker index="01" label="Working method" />
            <div className="grid gap-12 xl:grid-cols-[0.85fr_1.15fr] xl:gap-20">
              <div>
                <h2 className="max-w-md font-display text-[clamp(2.2rem,4vw,4.5rem)] font-extrabold leading-[0.98] tracking-[-0.065em]">Clarity is a<br /><span className="text-[#d64e32]">testable</span> output.</h2>
                <p className="mt-7 max-w-md text-[1.1rem] leading-[1.55] text-[#52605b]">I translate loose requirements into a visible task boundary: what is allowed, what must be checked, where evidence ends, and how a reviewer can verify the result. The goal is not ornate prompting. It is reliable judgment under constraints.</p>
              </div>
              <div className="border-y border-[#202523]/15">
                {competencies.map((competency, index) => (
                  <article key={competency.code} className={`group grid gap-4 py-6 sm:grid-cols-[52px_1fr] ${index !== competencies.length - 1 ? "border-b border-[#202523]/15" : ""}`}>
                    <span className="font-mono text-[11px] text-[#d64e32]">{competency.code}</span>
                    <div>
                      <h3 className="font-display text-lg font-extrabold tracking-[-0.03em]">{competency.name}</h3>
                      <p className="mt-2 max-w-2xl text-[1.03rem] leading-relaxed text-[#52605b]">{competency.detail}</p>
                    </div>
                  </article>
                ))}
              </div>
            </div>
          </section>

          <section id="schemas" className="border-y border-[#202523]/15 bg-[#202523] px-5 py-20 text-[#f5f0e6] sm:px-8 md:px-12 lg:px-16 lg:py-28 xl:px-20">
            <SectionMarker index="02" label="Inspectable prompt schema" />
            <div className="grid gap-12 xl:grid-cols-[0.85fr_1.15fr] xl:gap-20">
              <div>
                <h2 className="max-w-md font-display text-[clamp(2.2rem,4.2vw,4.6rem)] font-extrabold leading-[0.98] tracking-[-0.065em]">Structure the task.<br /><span className="text-[#e97b61]">Protect the decision.</span></h2>
                <p className="mt-7 max-w-md text-[1.1rem] leading-[1.55] text-[#c6cbc7]">This evaluator schema makes roles, inputs, constraints, and output conditions explicit. It gives the reviewer a way to examine failure paths before they appear in production.</p>
                <a href={links.schemas} target="_blank" rel="noreferrer" className="mt-8 inline-flex items-center gap-2 border-b border-[#e97b61] pb-1 font-mono text-[10px] uppercase tracking-[0.12em] text-[#f5f0e6] transition-colors hover:text-[#e97b61] focus-visible:text-[#e97b61]">Open full schema file <ArrowUpRight size={14} /></a>
              </div>
              <div className="relative overflow-hidden border border-[#f5f0e6]/20 bg-[#16201d] p-6 shadow-[8px_8px_0_rgba(214,78,50,0.8)] sm:p-9">
                {!isGitHubPagesBuild && <div className="absolute inset-0 opacity-20" style={{ backgroundImage: "url('/manus-storage/schema-cards_2e9551e4.jpg')", backgroundPosition: "center", backgroundSize: "cover", mixBlendMode: "screen" }} />}
                <div className="relative">
                  <div className="mb-7 flex items-center gap-2 font-mono text-[10px] uppercase tracking-[0.14em] text-[#9ba8a2]"><Brackets size={14} className="text-[#e97b61]" /> schema / evaluator-v1</div>
                  <div className="space-y-4 font-mono text-[clamp(0.71rem,1.2vw,0.9rem)] leading-relaxed">
                    {schemaLines.map(([open, content, close]) => (
                      <div key={open} className="grid grid-cols-[max-content_1fr_max-content] gap-x-3">
                        <span className="text-[#e97b61]">{open}</span>
                        <span className="truncate text-[#f5f0e6]">{content}</span>
                        <span className="text-[#8c9994]">{close}</span>
                      </div>
                    ))}
                  </div>
                  <div className="mt-9 grid gap-3 border-t border-[#f5f0e6]/15 pt-6 sm:grid-cols-3">
                    {["Role clarity", "Evidence boundary", "Output check"].map((item, index) => (
                      <div key={item} className="flex gap-2 font-mono text-[10px] uppercase leading-snug tracking-[0.08em] text-[#b9c0bb]"><span className="text-[#e97b61]">0{index + 1}</span>{item}</div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </section>

          <section id="curriculum" className="px-5 py-20 sm:px-8 md:px-12 lg:px-16 lg:py-28 xl:px-20">
            <SectionMarker index="03" label="Asynchronous curriculum" />
            <div className="grid gap-12 xl:grid-cols-[0.8fr_1.2fr] xl:gap-20">
              <div>
                <div className="mb-5 flex items-end gap-4">
                  <span className="font-display text-7xl font-extrabold leading-none tracking-[-0.08em] text-[#d64e32]">75</span>
                  <span className="mb-2 font-mono text-[10px] uppercase tracking-[0.14em] text-[#63706c]">sessions<br />mapped</span>
                </div>
                <h2 className="max-w-md font-display text-[clamp(2.2rem,4vw,4.5rem)] font-extrabold leading-[0.98] tracking-[-0.065em]">Build an audit trail that a reviewer can follow.</h2>
                <p className="mt-7 max-w-md text-[1.1rem] leading-[1.55] text-[#52605b]">“What Really Happened” is a Markdown-native curriculum architecture. It progresses from source boundaries to a published dossier, showing the same information-design habits that support reliable evaluation work.</p>
                <a href={links.curriculum} target="_blank" rel="noreferrer" className="mt-8 inline-flex items-center gap-2 border-b border-[#d64e32] pb-1 font-mono text-[10px] uppercase tracking-[0.12em] text-[#202523] transition-colors hover:text-[#d64e32] focus-visible:text-[#d64e32]">Open published curriculum <ArrowUpRight size={14} /></a>
              </div>
              <div className="border-t border-[#202523]/15">
                {curriculum.map(([range, title, detail]) => (
                  <article key={range} className="grid gap-3 border-b border-[#202523]/15 py-5 sm:grid-cols-[74px_1fr_auto] sm:items-baseline">
                    <span className="font-mono text-[10px] tracking-[0.08em] text-[#d64e32]">{range}</span>
                    <h3 className="font-display text-lg font-extrabold tracking-[-0.025em]">{title}</h3>
                    <p className="max-w-[270px] font-body text-[0.98rem] leading-snug text-[#63706c]">{detail}</p>
                  </article>
                ))}
              </div>
            </div>
          </section>

          <section id="systems" className="relative overflow-hidden border-y border-[#202523]/15 bg-[#e2eaf0] px-5 py-20 sm:px-8 md:px-12 lg:px-16 lg:py-28 xl:px-20">
            {!isGitHubPagesBuild && <div className="absolute inset-y-0 right-0 hidden w-[42%] overflow-hidden lg:block">
              <img src="/manus-storage/rubric-margins_c79a1453.jpg" alt="Annotated research notebook with review markers" className="h-full w-full object-cover mix-blend-multiply opacity-80" />
              <div className="absolute inset-0 bg-gradient-to-r from-[#e2eaf0] via-[#e2eaf0]/70 to-transparent" />
            </div>}
            <div className="relative max-w-3xl">
              <SectionMarker index="04" label="Systems work" />
              <h2 className="max-w-2xl font-display text-[clamp(2.2rem,4.2vw,4.7rem)] font-extrabold leading-[0.98] tracking-[-0.065em]">Independent operations made <span className="text-[#d64e32]">legible.</span></h2>
              <div className="mt-10 grid gap-4 sm:grid-cols-3">
                {[
                  [ShieldCheck, "20+ years", "Solo operations, compliance, and critical shift continuity."],
                  [SearchCheck, "Root-cause", "Symptoms separated from assumptions before correction."],
                  [FolderGit2, "Flat-file", "Portable systems built to remain usable without platform lock-in."],
                ].map(([Icon, metric, detail]) => {
                  const Component = Icon as typeof ShieldCheck;
                  return <article key={metric as string} className="border border-[#202523]/20 bg-[#f5f0e6]/70 p-5 backdrop-blur-sm"><Component size={20} className="text-[#d64e32]" /><p className="mt-7 font-display text-xl font-extrabold tracking-[-0.04em]">{metric as string}</p><p className="mt-2 font-body text-[0.98rem] leading-snug text-[#52605b]">{detail as string}</p></article>;
                })}
              </div>
            </div>
          </section>

          <section id="application" className="px-5 py-20 sm:px-8 md:px-12 lg:px-16 lg:py-28 xl:px-20">
            <SectionMarker index="05" label="Application packet" />
            <div className="grid gap-12 xl:grid-cols-[1.15fr_0.85fr] xl:gap-20">
              <div>
                <h2 className="max-w-2xl font-display text-[clamp(2.3rem,4.4vw,5rem)] font-extrabold leading-[0.98] tracking-[-0.07em]">A portfolio designed to be <span className="text-[#d64e32]">checked</span>, not just scanned.</h2>
                <p className="mt-7 max-w-xl text-[1.12rem] leading-[1.55] text-[#52605b]">The application profile is plain-text compatible for remote assessment systems. The underlying Markdown files expose the curriculum structure, prompt logic, and documentation habits behind the summary.</p>
                <div className="mt-9 flex flex-wrap gap-3 font-display text-sm font-bold">
                  <a href={links.application} target="_blank" rel="noreferrer" className="group flex items-center gap-2 bg-[#d64e32] px-5 py-3 text-[#fffaf2] shadow-[4px_4px_0_#202523] transition-all duration-200 hover:-translate-y-0.5 hover:shadow-[6px_6px_0_#202523] focus-visible:-translate-y-0.5 active:scale-[0.97]">Open application profile <FileText size={16} /></a>
                  <a href={links.portfolioRepo} target="_blank" rel="noreferrer" className="group flex items-center gap-2 border border-[#202523]/25 bg-[#fbf9f4] px-5 py-3 transition-colors hover:border-[#d64e32] hover:text-[#d64e32] focus-visible:border-[#d64e32] focus-visible:text-[#d64e32] active:scale-[0.97]">View repository source <GitBranch size={16} /></a>
                </div>
              </div>
              <aside className="border-t-2 border-[#202523] bg-[#fbf9f4] p-6 sm:p-8">
                <p className="font-mono text-[10px] uppercase tracking-[0.14em] text-[#63706c]">Review route</p>
                <ol className="mt-7 space-y-6">
                  {[
                    ["01", "Start with the resume", "A plain-text compatible profile for application fields."],
                    ["02", "Inspect the schemas", "Prompt constraints and edge-case patterns in Markdown."],
                    ["03", "Follow the curriculum", "A 75-session example of durable information architecture."],
                  ].map(([number, title, detail]) => <li key={number} className="grid grid-cols-[35px_1fr] gap-4"><span className="font-mono text-[10px] text-[#d64e32]">{number}</span><div><p className="font-display font-extrabold tracking-[-0.025em]">{title}</p><p className="mt-1 text-[0.98rem] leading-snug text-[#63706c]">{detail}</p></div></li>)}
                </ol>
              </aside>
            </div>
          </section>

          <footer className="border-t border-[#202523]/15 bg-[#202523] px-5 py-8 text-[#f5f0e6] sm:px-8 md:px-12 lg:px-16 xl:px-20">
            <div className="flex flex-col justify-between gap-6 sm:flex-row sm:items-end">
              <div>
                <div className="flex items-center gap-3">{isGitHubPagesBuild ? <span className="grid h-8 w-8 place-items-center border border-[#e97b61] font-mono text-xl text-[#e97b61]">⊙</span> : <img src="/manus-storage/calibration-aperture-logo_8b5fc95a.png" alt="" className="h-8 w-8 brightness-0 invert" />}<p className="font-display text-lg font-extrabold tracking-[-0.04em]">CALIBRATION LAB</p></div>
                <p className="mt-3 max-w-xl font-body text-[0.98rem] leading-relaxed text-[#b9c0bb]">Technical prompt engineering, evaluation architecture, and documentation systems for asynchronous AI operations.</p>
              </div>
              <a href={links.profile} target="_blank" rel="noreferrer" className="flex items-center gap-2 font-mono text-[10px] uppercase tracking-[0.12em] text-[#b9c0bb] transition-colors hover:text-[#e97b61] focus-visible:text-[#e97b61]"><CheckCheck size={14} className="text-[#e97b61]" /> GitHub / Daniel Lingar</a>
            </div>
          </footer>
        </main>
      </div>
    </div>
  );
}
