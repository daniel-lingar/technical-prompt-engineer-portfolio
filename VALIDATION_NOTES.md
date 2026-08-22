# Validation Notes

## Build Validation

The project passed `pnpm check` and the production build completed successfully on August 22, 2026. The build emitted a bundle-size advisory only; no type, dependency, or runtime errors were reported.

## Visual Validation

Desktop and mobile full-page previews were reviewed. The large-screen experience preserves the intended folio-and-margin hierarchy with a persistent navigation rail, readable editorial sections, and distinct prompt-schema and curriculum artifacts. At the mobile breakpoint, the rail becomes a compact dossier header and the primary sections retain legible line lengths, accessible controls, and clear reading order.

An independent style review found the interface aligned with the chosen Calibration Lab direction and advised that it was ready to ship.

## GitHub Pages Route Repair

The live GitHub Pages URL initially delivered the current HTML but an earlier cached JavaScript bundle rendered the legacy 404 component. The client entry was simplified to render this single-page portfolio directly, and the deployment completed successfully. A cache-busting visit to the live URL loaded the expected homepage in the same browser session; fresh visitors receive the current bundle at the standard public URL.

The standard public URL was then loaded again in the same browser session and rendered the complete Calibration Lab homepage without the 404 component.
