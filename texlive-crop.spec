# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/crop
# catalog-date 2009-07-10 18:40:58 +0200
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-crop
Version:	1.5
Release:	1
Summary:	Support for cropmarks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crop
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crop.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crop.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crop.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/crop/crop.sty
%doc %{_texmfdistdir}/doc/latex/crop/crop.pdf
%doc %{_texmfdistdir}/doc/latex/crop/crop.txt
#- source
%doc %{_texmfdistdir}/source/latex/crop/Makefile
%doc %{_texmfdistdir}/source/latex/crop/crop.dtx
%doc %{_texmfdistdir}/source/latex/crop/crop.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
