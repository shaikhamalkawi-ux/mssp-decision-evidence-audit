# Building the author-review manuscript

This repository supplies only original author-controlled `.tex` and PDF figure
files. It does **not** redistribute MDPI's third-party class/logo/template
files. Obtain the appropriate MDPI article LaTeX template from the publisher at
https://www.mdpi.com/authors/latex and put its unmodified `Definitions/`
directory next to `main.tex`, then compile with `latexmk -pdf main.tex`.

This is an *author manuscript prepared for Systems*, not a formally submitted
article, publisher proof or accepted work. Its internal draft footer deliberately
suppresses the dummy DOI that MDPI's template might otherwise synthesize from
unassigned volume/issue/article-number metadata.

`main.tex` still includes unconfirmed human author declarations and a private
original-source availability restriction. Update them truthfully before
journal submission; do not infer author contributions, funding, conflicts or
permission to release original industrial Excel/PDF data.
