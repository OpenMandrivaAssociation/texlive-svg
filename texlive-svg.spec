Name:		texlive-svg
Version:	2.02b
Release:	1
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
SVG images using Inkscape. \includesvg[<options>]{<svg
filename>} A variety of options is available, including width,
height, and path of the SVG. The image is converted to an
appropriate format, using the \write18 mechanism to execute a
shell command, and the package also offers the means of saving
a PDF, EPS, or PNG copy of the image, at the same time. The
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
%{_texmfdistdir}/tex/latex/svg
%doc %{_texmfdistdir}/doc/latex/svg
#- source
%doc %{_texmfdistdir}/source/latex/svg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
