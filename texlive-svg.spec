%global tl_name svg
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.02k
Release:	%{tl_revision}.1
Summary:	Include and extract SVG pictures in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/svg
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(graphics)
Requires:	texlive(iftex)
Requires:	texlive(koma-script)
Requires:	texlive(pdftexcmds)
Requires:	texlive(tools)
Requires:	texlive(trimspaces)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle contains the two packages svg and svg-extract. The svg
package is intended for the automated integration of SVG graphics into
LaTeX documents. Therefore the capabilities provided by Inkscape -- or
more precisely its command line tool -- are used to export the text
within an SVG graphic to a separate file, which is then rendered by
LaTeX. For this purpose the two commands \includesvg and
\includeinkscape are provided which are very similar to the
\includegraphics command of the graphicx package. In addition, the
package svg-extract allows the extraction of these graphics into
independent files in different graphic formats, exactly as it is
rendered within the LaTeX document, using either ImageMagick or
Ghostscript.

