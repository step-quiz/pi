/* ============================================================================
   comu/js/cursos.js · the course registry: the ONLY file that names the courses
   ----------------------------------------------------------------------------
   id    the course folder at the repository root (it also appears in every URL)
   nom   the label the teacher reads on the home page and in every header

   The anonymity check (CURS/eines/comprova.py, section ANONIMAT) forbids the
   course name anywhere else: pages, scripts and data get it from here at run time.
   To add a course: add one line here and create its folder (comu/docs/SITE-MAP.md,
   «Adding a course»).
   ========================================================================== */

window.PI = window.PI || {};
window.PI.CURSOS = [
  { id: "1eso", nom: "1ESO" },
  { id: "4eso", nom: "4ESO Aplicades" }
];
