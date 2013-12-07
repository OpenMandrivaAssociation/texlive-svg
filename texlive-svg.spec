# revision 27643
# category Package
# catalog-ctan /graphics/svg
# catalog-date 2012-09-09 19:10:52 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-svg
Version:	1.0
Release:	5
Summary:	Include and extract SVG pictures using Inkscape
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/svg
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a command similar to \includegraphics
command of the graphicx package, which enables the inclusion of
SVG images using Inkscape. \includesvg[options]{svg filename} A
variety of options is available, including width, height, and
path of the SVG. The image is converted to an appropriate
format, using the \write18 mechanism to execute a shell
command, and the package also offers the means of saving a PDF,
EPS, or PNG copy of the image, at the same time. The
documentation shows an example using an SVG created from the
high energy particle physics analysis package ROOT.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/svg/svg.sty
%doc %{_texmfdistdir}/doc/latex/svg/Fig.1a.pdf
%doc %{_texmfdistdir}/doc/latex/svg/Fig.1b.eps
%doc %{_texmfdistdir}/doc/latex/svg/Fig.2.pdf
%doc %{_texmfdistdir}/doc/latex/svg/Fig.2.png
%doc %{_texmfdistdir}/doc/latex/svg/README
%doc %{_texmfdistdir}/doc/latex/svg/example.pdf
%doc %{_texmfdistdir}/doc/latex/svg/example.pdf_tex
%doc %{_texmfdistdir}/doc/latex/svg/example.svg
%doc %{_texmfdistdir}/doc/latex/svg/preamble.tex
%doc %{_texmfdistdir}/doc/latex/svg/root.C
%doc %{_texmfdistdir}/doc/latex/svg/root.pdf
%doc %{_texmfdistdir}/doc/latex/svg/root.pdf_tex
%doc %{_texmfdistdir}/doc/latex/svg/root.svg
%doc %{_texmfdistdir}/doc/latex/svg/svg.pdf
#- source
%doc %{_texmfdistdir}/source/latex/svg/svg.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
