Name:		texlive-crop
Version:	55424
Release:	1
Summary:	Support for cropmarks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crop
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crop.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crop.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crop.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package providing corner marks for camera alignment as well
as for trimming paper stacks, and additional page information
on every page if required. Most macros are easily adaptable to
personal preferences. An option is provided for selectively
suppressing graphics or text, which may be useful for printing
just colour graphics on a colour laser printer and the rest on
a cheap mono laser printer. A page info line contains the time
and a new cropmarks index and is printed at the top of the
page. A configuration command is provided for the info line
font. Options for better collaboration with dvips, pdftex and
vtex are provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/crop
%doc %{_texmfdistdir}/doc/latex/crop
#- source
%doc %{_texmfdistdir}/source/latex/crop

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
